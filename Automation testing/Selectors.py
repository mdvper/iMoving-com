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
driver.set_page_load_timeout(5)
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
    print('Recemt moves data is OK ', driver.get_screenshot_as_file("Recent Moves.png"))
else:
    print("Nor recent moves data")

# Validating that "To all our movers" section works correctly. Let's check California as an example

AllMoversButton = driver.find_element(By.XPATH, "//*[@class = 'to-all-movers-link']")
AllMoversButton.click()
Cali = "California"
driver.find_element(By.XPATH, "//*[@class = 'searchMoverByState']").send_keys(Cali)
driver.find_element(By.XPATH, "//*[@class = 'searchContainer']").click()
driver.find_element(By.XPATH, "//*[@class = 'moversSearchResult']").click()
assert "Find California Movers Near you, book online | iMoving" in driver.title
if "Find California Movers Near you, book online | iMoving" in driver.title:
    print("California page title and URL are OK: ", driver.title, ",", driver.current_url)
else:
    print("Invalid title or URL. Must be checked by developer.")
driver.back()
driver.back()

# Alright then, it works good. But let's check it once again with another state. How about Maryland?

driver.get("https://www.imoving.com/california-movers/")
driver.refresh()
Mary = "Maryland"
driver.find_element(By.XPATH, "//*[@class = 'searchMoverByState']").send_keys(Mary)
driver.find_element(By.XPATH, "//*[@class = 'searchContainer']").click()
driver.find_element(By.XPATH, "//*[@class = 'moversSearchResult']").click()
assert "Find Maryland Movers Near you, book online | iMoving" in driver.title
if "Find Maryland Movers Near you, book online | iMoving" in driver.title:
    print("Maryland page title and URL are OK: ", driver.title, ",", driver.current_url)
else:
    print("Invalid title or URL. Must be checked by developer.")
time.sleep(1)

# Verifying "About US" button

driver.get("https://www.imoving.com/")
driver.find_element(By.XPATH, "//*[@class = 'state-movers-link hidden-xs']").click()
AboutUsTitle = 'iMoving - The Future of Moving is Here'
AboutUsURL = "https://www.imoving.com/about-us/"
assert AboutUsTitle in driver.title
assert AboutUsURL in driver.current_url
if AboutUsTitle in driver.title and AboutUsURL in driver.current_url:
    print('"About us" title is OK, same as URL: ', driver.title, ",", driver.current_url)
elif AboutUsTitle in driver.title and AboutUsURL not in driver.current_url:
    print("Title is OK. URL is invalid.")
elif AboutUsTitle not in driver.title and AboutUsURL in driver.current_url:
    print("Title is invalid. URL is OK.")
else:
    print("Invalid title and URL. Must be checked by developer.")
driver.back()

# Verifying "Book now" button

BookNowButton = driver.find_element(By.XPATH, "//*[@class = 'last-call-button']")
BNhref = BookNowButton.get_attribute('href')
if BNhref is None:
   print('"Book Now" button is not clickable.')
else:
   print('"Book Now" button is OK.')
driver.back()

# Verifying "MovingPedia" section

MovingPedia = driver.find_element(By.PARTIAL_LINK_TEXT, "MovingPedia")
MovingPedia.click()
iMovingBlogURL = "https://www.imoving.com/blog"
iMovingBlogTitle = "iMoving Blog"
assert iMovingBlogURL in driver.current_url and iMovingBlogTitle in driver.title
if iMovingBlogURL == driver.current_url and iMovingBlogTitle == driver.title:
    print('"iMoving Blog" URL is OK: ', driver.current_url, 'Title is ok too: ', driver.title)
elif iMovingBlogURL == driver.current_url and iMovingBlogTitle != driver.title:
    print('"iMoving Blog" URL is OK: ', driver.current_url, 'but title is invalid: ', driver.title)
elif iMovingBlogURL != driver.current_url and iMovingBlogTitle == driver.title:
    print('"iMoving Blog" URL is invalid: ', driver.current_url, ' but title is OK: ', driver.title)
driver.back()

# Clicking on "MovingPedia" hashtags on main page

driver.find_element(By.PARTIAL_LINK_TEXT, "Long Distance Moving").click()
driver.back()
driver.find_element(By.PARTIAL_LINK_TEXT, "Moving Cost").click()
driver.back()
#driver.find_element(By.PARTIAL_LINK_TEXT, "#Local Movers")
#driver.back()
print('Unable to locate "#Local Movers" element.')
#driver.find_element(By.PARTIAL_LINK_TEXT, "#Moving Tips")
#driver.back
print('Unable to locate "#Moving Tips" element.')

# Verifying "Become a Mover" section

MoverEmail = driver.find_element(By.XPATH, "//*[@id = 'becomeMoverEmailResult']")


driver.quit()



