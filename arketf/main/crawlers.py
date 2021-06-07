from abc import ABC, abstractmethod
from datetime import datetime
from selenium import webdriver 

PATH = "/Users/brianlu/side-projects/ark-etf-website/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com.tw/")
print(driver.title)
driver.quit()