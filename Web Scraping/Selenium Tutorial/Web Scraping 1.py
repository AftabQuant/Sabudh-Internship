from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://www.scrapingcourse.com/javascript-rendering")

brand_name = driver.find_element(By.CSS_SELECTOR, ".brand-name")
time.sleep(5)

brand_name.click()
time.sleep(5)
driver.save_screenshot("homepage-screenshot.png")