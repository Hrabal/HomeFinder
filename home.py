import parsers
import inspect

for _, site in inspect.getmembers(parsers, inspect.isclass):
    print(site)
    site = site()
    site.parse()
    print(site.sort_homes())
