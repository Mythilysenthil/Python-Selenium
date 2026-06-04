from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search = driver.find_element(By.ID, "APjFqb")
search.send_keys("Selenium")
search.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()