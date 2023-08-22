from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
actions = ActionChains(driver)

# pop-up selecting english lan
# language_frame = driver.find_element(By.ID, "promptAnchor")
# driver.switch_to.frame(language_frame)
# english = driver.find_element(By.ID, "langSelect-EN")
# english.click()
# alert = driver.switch_to.alert
# alert.accept()





input("Press Enter to close the browser...")

driver.quit()
