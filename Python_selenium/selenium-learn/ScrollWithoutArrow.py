import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
home = driver.find_element(By.XPATH,"//a[normalize-space()='Home']").is_displayed()
sub= driver.find_element(By.XPATH, "//h2[text()='Subscription']")