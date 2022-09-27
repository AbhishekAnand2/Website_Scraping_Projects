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

base_url = f"https://absolutenaturecbd.com/shop/page/"


def urlGenerator(url):
    page_no = 1
    try:
        page = requests.get(url=url + f"{page_no}")
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'lxml')
            all_products = soup.find_all('li', attrs={'class': 'purchasable'})

            for i in all_products:
                yield i.a.get('href')
            page_no += 1
    except:
        pass


#
# generator = urlGenerator("https://absolutenaturecbd.com/shop/page/1").__next__()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
for Url in urlGenerator(base_url):
    driver.get(Url)
    t = random.randint(1, 3)
    time.sleep(t)

driver.close()
