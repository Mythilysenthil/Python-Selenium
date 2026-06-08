from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")

wait = WebDriverWait(driver,10)
cont = driver.find_element(By.XPATH,"//a[@href='/contact_us']/i[@class]").click()
getIn = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='col-sm-12']/h2[@class='title text-center']"))).is_displayed
print("Get in touch is visible")
name = driver.find_element(By.XPATH,"//div/input[@name='name']").send_keys("Mythily")
email = driver.find_element(By.XPATH,"//div/input[@name='email']").send_keys("mythily@gmail.com")
sub = driver.find_element(By.XPATH,"//div/input[@name='subject']").send_keys("Product Inquiry")
msg = driver.find_element(By.XPATH,"//div/textarea[@name='message']").send_keys("I would like to know more about the products available on your website.")
submit = driver.find_element(By.XPATH,"//div/input[@name='submit']").click()
alrt = driver.switch_to.alert
alrt.accept()
succ = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='status alert alert-success']"))).text
assert succ == "Success! Your details have been submitted successfully."
print("Submitted successfully")
home = driver.find_element(By.XPATH,"//a[@class='btn btn-success']").click()
homePage = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/']/i"))).is_displayed
print("Again Loaded on Home page")