from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")

wait = WebDriverWait(driver, 15)

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Signup / Login']"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name']"))).send_keys("Mythily")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("mythily_test123@gmail.com")
driver.find_element(By.XPATH, "//button[text()='Signup']").click()

try:
    actual_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//b[text()='Enter Account Information']")))
    
    actual = actual_element.text
    print("Actual Text =", actual)
    assert actual.upper() == "ENTER ACCOUNT INFORMATION"
    print("Verification Successful")
except Exception as e:
    print("ERROR: Could not find 'Enter Account Information' heading.")
    print("Possible reason: Email already registered, or page did not load.")
    print("Details:", e)
    driver.quit()
    exit()

driver.find_element(By.XPATH, "//input[@id='id_gender2']").click()
driver.find_element(By.ID, "password").send_keys("mythily@123")
driver.find_element(By.XPATH, "//select[@id='days']").click()
driver.find_element(By.XPATH, "//select[@id='days']/option[@value='11']").click()
driver.find_element(By.XPATH, "//select[@id='months']").click()
driver.find_element(By.XPATH, "//select[@id='months']/option[@value='9']").click()
driver.find_element(By.XPATH, "//select[@id='years']").click()
driver.find_element(By.XPATH, "//select[@id='years']/option[@value='2004']").click()
driver.find_element(By.XPATH, "//input[@id='newsletter']").click()
driver.find_element(By.XPATH, "//input[@id='optin']").click()
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Mythily")
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("S")
driver.find_element(By.XPATH, "//input[@id='company']").send_keys("ABC Company")
driver.find_element(By.XPATH, "//input[@id='address1']").send_keys("Anna nagar")
driver.find_element(By.XPATH, "//input[@id='state']").send_keys("Tamil nadu")
driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Salem")
driver.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("636003")
driver.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys("1234567890")
driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

accCreate_element = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']")))

accCreate = accCreate_element.text
print("Account Created Text =", accCreate)
assert accCreate.upper() == "ACCOUNT CREATED!"
print("Account created successfully")

driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()

delete = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/delete_account']")))
if delete.is_displayed():
    delete.click()
    print("Delete Button clicked")

conform = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Deleted!']")))
print("Account Deleted Text =", conform.text)
assert conform.text.upper() == "ACCOUNT DELETED!"
print("Account Deleted successfully")

driver.quit()