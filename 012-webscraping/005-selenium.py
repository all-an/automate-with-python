# #archive-link-link

# https://www.google.com/doodles

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.maximize_window()

driver.get('https://www.google.com/doodles')

actions = ActionChains(driver)

searchElement = driver.find_element(By.CSS_SELECTOR, '#archive-link-link')

print(searchElement.text)

searchElement = driver.find_element(By.CSS_SELECTOR, 'html')

print(searchElement.text)