from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver"
driver = webdriver.Chrome()

driver.get("https://python.org")
event_times = driver.find_elements(By.CSS_SELECTOR, 'div.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, 'div.event-widget li a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text
    }

print(events)
