from lxml import html
import urllib.request
import sys

if len(sys.argv) != 4:
    raise SystemExit('Usage: simple_webscraper.py term page_number per_page')

term = sys.argv[1]
page_number = sys.argv[2]
per_page = sys.argv[3]

u = urllib.request \
            .urlopen('https://www.ted.com/search?page={}&per_page={}&q={}'
            .format(page_number, per_page, term.replace(" ", "+")))

data = u.read()
doc = html.document_fromstring(data)

for title in doc.cssselect("article.search__result h3 a"):
    print(title.text_con())

