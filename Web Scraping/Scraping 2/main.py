import requests

def fetchAndSaveFile(url, path):
    req = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(req.text)

url = "https://www.flipkart.com/mobile-phones-store?otracker=nmenu_sub_Electronics_0_Mobiles"

fetchAndSaveFile(url, r"D:\Ultimate Programming\Sabudh Internship\Web Scraping\Scraping 2\flipkart.html")
