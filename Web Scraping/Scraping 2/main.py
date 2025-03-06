import requests
from bs4 import BeautifulSoup

def fetchAndSaveFile(url, path):
    req = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(req.text)

url = "https://www.flipkart.com/mobile-phones-store?otracker=nmenu_sub_Electronics_0_Mobiles"

req = requests.get(url)
print(req)

soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())

title = soup.title.text
print(title)

all_paragraph = soup.find_all('p')
for para in all_paragraph:
    print(para.text, "\n")

import pandas as pd

titles = soup.select("h1, h2, h3")
for title in titles:
    print(title.text, "\n")