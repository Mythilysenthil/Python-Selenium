from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
wait = WebDriverWait(driver,timeout=20,poll_frequency=2,ignored_exceptions=[NoSuchElementException])

driver.maximize_window()
driver.get("http://automationexercise.com")

home = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Home']")))
home.is_displayed()
signup = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Signup / Login']")))
signup.click()
driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("mythily11@gmail.com")
driver.find_element(By.XPATH,"//input[@data-qa='login-email']/following-sibling::input").send_keys("mythily")
driver.find_element(By.XPATH,"//input[@data-qa='login-password']/following-sibling::button").click()
errormsg = wait.until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Your email or password is incorrect!']")))
erromsgTxt = errormsg.text
assert erromsgTxt == "Your email or password is incorrect!"
print("Verified invalid email and password")
driver.quit()