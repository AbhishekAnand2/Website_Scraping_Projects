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
page_Url = "https://www.binoidcbd.com/collections/cbd?page="


def urlGenerator(Url):
    try:
        condition = True
        iteration_count = 1
        while condition:
            page = requests.get(f"{page_Url}{iteration_count}")
            soup = BeautifulSoup(page.content, 'lxml')
            containerForUrls = soup.find_all('div', attrs={'class': 'ProductItem__Wrapper'})
            if len(containerForUrls) != 0:
                for i in containerForUrls:
                    yield (f"{base_url}{i.a.get('href')}")
                iteration_count += 1
            else:
                condition = False
    except:
        pass


# <------------------ AUTOMATION PART -------------------------->

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.minimize_window()
dataNumber = 1
dataset = []
for productUrl in urlGenerator(page_Url):
    productDetails = {}
    print(f'fetching data for product Number.....{dataNumber}')
    driver.get(url=productUrl)

    # <-------------------- Data Gathering ---------------->

    try:
        productDetails['productLink'] = productUrl
    except:
        continue

    try:
        productDetails['productTitle'] = driver.find_element(By.CLASS_NAME, 'u-h2').text
    except:
        continue
    try:
        productDescription = driver.find_element(By.CLASS_NAME, 'Rte').find_element(By.CLASS_NAME, 'is-ready').text
        productDetails['productDescription'] = productDescription.split("Benefits")[0]

    except:
        continue
    try:
        productDetails['productPrice'] = driver.find_element(By.ID, 'shopify-section-product-template').find_element(By.CLASS_NAME, 'Price--compareAt').text
    except:
        continue

    try:
        productImageString = driver.find_element(By.CLASS_NAME, 'Image--lazyLoaded').get_property('srcset')
        productDetails['productImageLink(800x800px)'] = productImageString[productImageString.find("800w") + 6:productImageString.find("900w")]
    except:
        continue

    dataset.append(productDetails)
    dataNumber += 1
    waitTime = random.randint(0, 5)
    time.sleep(waitTime)

driver.close()


df = pd.DataFrame(dataset)
df.to_csv("output.csv", index=False)


