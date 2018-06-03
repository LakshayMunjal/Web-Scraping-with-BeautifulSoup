import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.urbanoutfitters.com/logo-t-shirts?page=' + str(page)
        source_code = requests.get(url)
        plain_source = source_code.text
        soup = BeautifulSoup(plain_source, "html.parser")
        for link in soup.findAll('a', {'class': 'c-product-tile__title-link js-product-tile-title-link'}):
            href = "https://www.urbanoutfitters.com" + link.get('href')
            print(href)
            span = link.text
            print(span)
            page += 1


spider(1)
