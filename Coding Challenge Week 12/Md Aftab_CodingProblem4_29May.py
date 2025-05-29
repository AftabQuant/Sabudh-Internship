from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
url = "https://www.screener.in/screens/92669/best-long-term-stocks/"
driver.get(url)

table = driver.find_element("xpath", "//table[contains(@class, 'data-table')]")
rows = table.find_elements("tag name", "tr")

headers = [header.text for header in rows[0].find_elements("tag name", "th")]

data = []
for row in rows[1:]:
    cells = row.find_elements("tag name", "td")
    data.append([cell.text for cell in cells])

df = pd.DataFrame(data, columns=headers)

df.to_csv("best_long_term_stocks.csv", index=False)

driver.quit()

print("Data has been saved to 'best_long_term_stocks.csv'")
