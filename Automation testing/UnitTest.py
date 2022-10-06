import time
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import random


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.get("https://www.imoving.com")

        def delay():
            time.sleep(random.randint(1, 3))

        # API testing
        print("Imoving Url has", requests.get(driver.current_url).status_code, "as status Code")
        code = requests.get(driver.current_url).status_code

    def tearDown(self):
        self.driver.quit()
