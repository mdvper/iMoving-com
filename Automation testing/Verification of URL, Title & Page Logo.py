from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url_imoving = "https://www.imoving.com/"
driver.get(url_imoving)
driver.maximize_window()

# URL verification
current_url = driver.current_url
if current_url == "https://www.imoving.com/":
    print("Current URL is OK: ", current_url)

# Title verification
imoving_expectedtitle = "iMoving - Compare Moving Companies Prices and Book Online"
current_title = driver.title

if imoving_expectedtitle == current_title:
    print("Current Title is OK: ", imoving_expectedtitle)
else:
    print("Current Title is out of scope: ", current_title)

# Page Logo verification
imoving_logo = driver.find_element(By.XPATH, '//*[@class="navbar-brand"]')

if imoving_logo:
    print("Current Logo is OK", driver.get_screenshot_as_file('imoving_cuurent_logo.png'))
else:
    print("iMoving Logo is not presented, or replaced with another one")

#driver.quit()