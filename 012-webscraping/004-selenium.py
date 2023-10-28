from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

driver.maximize_window()

driver.get('https://www.google.com')

actions = ActionChains(driver)

searchElement = driver.find_element(By.CSS_SELECTOR, '#APjFqb')

searchElement.send_keys('\"Allan Pereira Abrahão\"')

# searchElement.send_keys(Keys.ENTER)

searchElement.submit()

driver.implicitly_wait(5)


time.sleep(3) #sleep for 3 sec
time.sleep(0.25) #sleep for 250 milliseconds

driver.execute_script("window.history.go(-1)")

driver.back()

driver.refresh()

time.sleep(3)

driver.quit()

print(searchElement)