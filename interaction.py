import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')


# click_all_portals = driver.find_element(By.LINK_TEXT, "Community portal")
# click_all_portals.click()

search_click = driver.find_element(By.NAME, "search")
search_click.send_keys("Python")
search_click.send_keys(Keys.ENTER)




time.sleep(5)
driver.quit()
