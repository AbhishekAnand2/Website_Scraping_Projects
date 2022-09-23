import time
import random
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

# Initial Landing Page
base_url = "https://www.binoidcbd.com"
product_page_Url = "https://www.binoidcbd.com/collections/cbd/products/binoid-cbd-gummies-mixed-berry-300mg"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.minimize_window()
driver.get(product_page_Url)
desc = driver.find_element(By.CLASS_NAME, 'Rte').find_element(By.CLASS_NAME, 'is-ready').text
print(desc.split("Benefits")[0], "\n")


imageLinkString = driver.find_element(By.CLASS_NAME, 'Image--lazyLoaded').get_property('srcset')
imageLink = imageLinkString[imageLinkString.find("800w")+6:imageLinkString.find("900w")]
print(imageLink)

