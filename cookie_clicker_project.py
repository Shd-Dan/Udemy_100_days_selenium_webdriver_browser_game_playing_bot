from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(4)

# language selector
click_english = driver.find_element(By.ID, 'langSelect-EN')
driver.execute_script('arguments[0].click();', click_english)

# click the cookie
click_cookie = driver.find_element(By.ID, 'bigCookie')
click_cookie.click()



input("Press Enter to close the browser...")

driver.quit()


