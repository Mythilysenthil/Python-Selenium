import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
wait = webdriver(driver,10)
action = ActionChains(driver)

home = driver.find_element(By.XPATH,"//a[normalize-space()='Home']").is_displayed()
driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("mythily11@gmail.com")
driver.find_element(By.XPATH,"//input[@data-qa='login-email']/following-sibling::input").send_keys("mythily")
driver.find_element(By.XPATH,"//input[@data-qa='login-password']/following-sibling::button").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]").is_displayed()
product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@data-product-id='1' and contains(@class,'add-to-cart')])[1]")))
action.move_to_element(product).perform()
driver.execute_script("arguments[0].click();", product)
print("Added product to cart")
viewCart = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/view_cart']")))
driver.execute_script("arguments[0].click();", viewCart)
pro = wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td/h4/a)[1]"))).text
assert pro == "Blue Top"
print("Product added successfully")
proceed = driver.find_element(By.XPATH,"//div[@class='col-sm-6']/a").click()
