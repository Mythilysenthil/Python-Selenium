from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("http://automationexercise.com")

driver.find_element(By.XPATH,"//a[normalize-space()='Home']").is_displayed()
driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("mythily11@gmail.com")
driver.find_element(By.XPATH,"//input[@data-qa='login-email']/following-sibling::input").send_keys("mythily")
driver.find_element(By.XPATH,"//input[@data-qa='login-password']/following-sibling::button").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]").is_displayed()
deletebtn = driver.find_element(By.XPATH, "//a[@href='/delete_account']")
# using java script for close the ads
driver.execute_script("arguments[0].click();", deletebtn)

print("Delete Button clicked")
confirm = driver.find_element(By.XPATH, "//b[text()='Account Deleted!']")
print("Account Deleted Text =", confirm.text)
assert confirm.text.upper() == "ACCOUNT DELETED!"
print("Account Deleted successfully")

driver.quit()