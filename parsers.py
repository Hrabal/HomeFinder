from homefinder import SitoAnnunci


class Immobiliare(SitoAnnunci):
    url = 'https://www.immobiliare.it/ricerca.php?idCategoria=1&idContratto=2&idTipologia=&sottotipologia=&idTipologiaStanza=&idFasciaPrezzo=&idNazione=IT&idRegione=&idProvincia=&idComune=&idLocalita=&idAreaGeografica=&prezzoMinimo=&prezzoMassimo=700&balcone=&balconeOterrazzo=&boxOpostoauto=&stato=&terrazzo=&bagni=&mappa=&foto=&superficie=&superficieMinima=&superficieMassima=&raggio=&locali=&localiMinimo=&localiMassimo=&criterio=rilevanza&ordine=desc&map=0&tipoProprieta=&arredato=&inAsta=&noAste=&aReddito=&fumatore=&animali=&franchising=&flagNc=&gayfriendly=&internet=&sessoInquilini=&vacanze=&categoriaStanza=&fkTipologiaStanza=&ascensore=&classeEnergetica=&verticaleAste=&occupazioneInquilini=&pag=1&vrt=44.68189734898,10.688211321831;44.646246338405,10.794641375542;44.638429488997,10.870172381401;44.637452308767,10.912057757378;44.646734856522,10.91755092144;44.663830398728,10.903131365776;44.680920901071,10.938150286675;44.722893300569,10.973855853081;44.747281869947,11.008874773979;44.762885156396,11.010934710503;44.786769523905,10.942270159721;44.807233976405,10.936776995659;44.834995553258,10.818673968315;44.88366777606,10.693017840385;44.726796162868,10.620233416557;44.699470597216,10.684778094292'
    paginator_class = '.pagination__number'
    announce_class = '.listing-item_body--content'
    prezzo_class = '.lif__pricing'
    titolo_class = '.titolo'
    titolo_full_class = '.title-detail'
    description_class = '#description'
