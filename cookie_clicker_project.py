import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(10)

# language selector
click_english = driver.find_element(By.ID, 'langSelect-EN')
driver.execute_script('arguments[0].click();', click_english)

# click the cookie
click_cookie = driver.find_element(By.ID, 'bigCookie')


def check_balance():
    cookies_quantity = driver.find_element(By.ID, 'cookies')
    cookie_list = cookies_quantity.get_attribute('innerHTML').split()
    cookie_balance = int(cookie_list[0])

    grand_ma = driver.find_element(By.ID, "productPrice1")
    grand_ma_list = grand_ma.get_attribute('innerHTML').split()
    grand_ma_balance = int(grand_ma_list[0])

    if cookie_balance > grand_ma_balance:
        driver.find_element(By.ID, 'product1').click()


timeout = time.time() + 50
five_second = time.time()

while timeout > time.time():
    cookie_click = driver.find_element(By.ID, "bigCookie")
    cookie_click.click()

    if time.time() - five_second == 20:
        check_balance()


time.sleep(3)
driver.quit()
