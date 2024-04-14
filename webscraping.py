# web scraping using beautiful soup

import requests
from bs4 import BeautifulSoup

url = "https://www.cardekho.com/used-cars+in+hyderabad"
page = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
page_text = BeautifulSoup(page.text, "html.parser")

for car in page_text.find_all("div", class_="NewUcExCard posR"):
    name = car.find('h3', class_="title")
    print(name.text)
    
    price = car.find("div", class_="Price hover")
    print(price.text)