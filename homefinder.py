from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


class SitoAnnunci:
    def __init__(self):
        self.pages_to_parse = []
        self.homes = []

    def get_home(self):
        print(f'Getting home for {self.__class__.__name__}')
        r = simple_get(self.url)
        return BeautifulSoup(r, 'html.parser')

    def parse(self):
        self.pages_to_parse.append(self.get_home())
        self.pages_to_parse.extend(self.get_pages(self.pages_to_parse[0]))
        self.get_annunci()

    def get_pages(self, base_parser):
        print('Getting more pages..')
        pages = base_parser.select(self.paginator_class)[0].find_all('a', href=True)
        return [BeautifulSoup(simple_get(p["href"]), 'html.parser') for p in pages]

    def get_annunci(self):
        print('Getting homes..')
        for html in self.pages_to_parse:
            for ann in html.select(self.announce_class):
                prezzo = float(ann.select(self.prezzo_class)[0].text.replace('€', '').strip())
                link = ann.select(self.titolo_class)[0].find_all('a', href=True)[0]
                ann_get = BeautifulSoup(simple_get(link["href"]), 'html.parser')
                titolo = ann_get.select(self.titolo_full_class)[0].text
                desc = ann_get.select(self.description_class)[0].text
                self.homes.append(Annuncio(titolo, link, desc, prezzo))

    def sort_homes(self):
        return sorted(self.homes, reverse=True)


class Annuncio:
    def __init__(self, titolo, link, desc, prezzo):
        self._score = {}
        self.titolo = titolo
        self.link = link
        self.prezzo = prezzo
        self.desc = desc
        self.calculate_score()

    def calculate_score(self):
        if 'giardino' in self.all_text:
            self._score['giardino'] = 1
        if 'indipendente' in self.all_text:
            self._score['indipendente'] = 1
        if 'centro' in self.all_text:
            self._score['centro'] = -1
        self._score['prezzo'] = 1 - self.prezzo / 600
        self._score['prezzo'] += 0.5 if 600 > self.prezzo >= 450 else 0

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    @property
    def all_text(self):
        return self.desc.lower() + self.titolo.lower()

    @property
    def score(self):
        return round(sum(self._score.values()), 2)

    def __repr__(self):
        return f'<Annuncio {self.score} - {self.titolo} - {self.prezzo}>'
