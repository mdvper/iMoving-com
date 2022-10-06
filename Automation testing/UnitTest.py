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
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not OK. Current code is: ", code)

        delay()

        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//*[@class = 'header-img-container']")))
            print("Home page is ready")
        except TimeoutException:
            print("Loading took too much time!")
            driver.get_screenshot_as_file("imoving_page_loading_error.png")
            driver.save_screenshot('imoving_page_loading_error.png')

        self.assertIn("iMoving - Compare Moving Companies Prices and Book Online", driver.title)
        print("Page has", '"',driver.title,'"', "as page title.")

    def tearDown(self):
        self.driver.quit()
