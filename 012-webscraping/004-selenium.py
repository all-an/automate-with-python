from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.maximize_window()

browser.get('https://automatetheboringstuff.com/')

element = browser.find_element(By.CSS_SELECTOR, '.top_header > a:nth-child(4)')

print(element)