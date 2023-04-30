import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

class Fetcher:
    def __init__(self, url):
        # self.driver = webdriver.PhantomJS()
        # self.driver.wait = WebDriverWait(self.driver, 5)
        # self.url = url
        # print(self.url)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url
        print(self.url)

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "gsfi")
            ))
        except:
            print("failed")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        
        
        answer = soup.select_one("div[data-attrid='wa:/description'] > span")
        if not answer:
            answer = soup.select_one("div[data-attrid='kc:/common:synonyms'] > span")
        if not answer:
            answer = soup.select_one("span[jsname='W297wb']")
        if not answer:
            answer = soup.select_one("div.zCubwf")
    
        # Save the page source for debugging purposes
        with open("test.html", "w+", encoding="utf-8") as f:
            f.write(str(soup))

        # Return the answer or "I dont know." if no answer was found
        return answer.get_text() if answer else "I dont know."
        

