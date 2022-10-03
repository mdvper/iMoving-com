from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()

driver.implicitly_wait(5)

driver.find_element(By.NAME, "q").send_keys("iMoving")
driver.find_element(By.NAME, "btnK").click()
driver.back()
driver.find_element(By.NAME, "q").send_keys("iMoving")
driver.find_element(By.NAME, "btnK").submit()


driver.find_element(By.PARTIAL_LINK_TEXT, "iMoving - Compare Moving Companies Prices and Book Online").click()
time.sleep(1)

assert "https://www.imoving.com/" in driver.current_url
if driver.current_url == "https://www.imoving.com/":
    print('Current URL is OK: ', driver.current_url)
assert "iMoving - Compare Moving Companies Prices and Book Online" in driver.title
if driver.title == 'iMoving - Compare Moving Companies Prices and Book Online':
    print('Current title is OK: ', driver.title)


# "Search Full Service Movers" elements
driver.find_element(By.XPATH, "//*[@class='btn dropdown-toggle btn-default']").click()
driver.find_element(By.XPATH, "//*[@class='1080']").click()

# "Recent Moves" section button
driver.find_element(By.XPATH, "//*[@class ='get-quite-button']").click()

RecentMovesDescription = driver.find_element(By.XPATH, "//*[@class ='popMap']")
if RecentMovesDescription:
    print(driver.get_screenshot_as_file("Recent Moves.png"))
else:
    print()
driver.quit()
