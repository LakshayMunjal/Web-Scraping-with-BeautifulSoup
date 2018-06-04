import requests #whenever you are connecting to the internet
from bs4 import BeautifulSoup #importing BeautifulSoup4


def spider(max_pages):                                                                                   #defining function
    page = 1                                                                                             #setting value of the page to be crawled
    while page <= max_pages:                                                                                
        url = 'https://www.urbanoutfitters.com/logo-t-shirts?page=' + str(page)                          #Pasing url and converting number to string
        source_code = requests.get(url)                                                                  #getting urls from the website
        plain_source = source_code.text                                                                  #get the complete site source code and convert it into text format
        soup = BeautifulSoup(plain_source, "html.parser")                                                #creating object of the class 'BeautifulSoup' to be able to crawl where `soup` is an object
        for link in soup.findAll('a', {'class': 'c-product-tile__title-link js-product-tile-title-link'}): #specifying the the content to be scrap from the the website
            href = "https://www.urbanoutfitters.com" + link.get('href')                                   #getting the link in the href attribute 
            print(href)
            span = link.text                                                                               #printing all the string related to that crawled link
            print(span)
            page += 1                                                                                      #incrementing the page


spider(1)                                                                                                   #calling function
