import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("ASLD8550AO")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Ohio")

mylo = driver.find_element(By.NAME, "email")
mylo.send_keys("seom@mail.net")

press_signup = driver.find_element(By.TAG_NAME, 'button')
press_signup.send_keys(Keys.ENTER)


time.sleep(3)
driver.quit()
