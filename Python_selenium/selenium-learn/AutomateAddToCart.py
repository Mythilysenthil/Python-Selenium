from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://automationexercise.com")

wait = WebDriverWait(driver,10)
action = ActionChains(driver)

home = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Home']")))
home.is_displayed()
product = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/products']")))
product.click()
firstPro = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@data-product-id='1' and contains(@class,'add-to-cart')])[1]")))
action.move_to_element(firstPro).perform()
driver.execute_script("arguments[0].click();", firstPro)
print("Clicked first product")
cont = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='modal-footer']/button")))
driver.execute_script("arguments[0].click();", cont)
secPro = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@data-product-id='2']")))
action.move_to_element(secPro).perform()
driver.execute_script("arguments[0].click();", secPro)
print("Clicked second product")
viewCart = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/view_cart']")))
driver.execute_script("arguments[0].click();", viewCart)
products = driver.find_elements(By.XPATH, "//tbody/tr")
print("Number of products in cart:", len(products))
pro1 = wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td/h4/a)[1]"))).text
pro2 = wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td/h4/a)[2]"))).text

assert pro1 == "Blue Top"
assert pro2 == "Men Tshirt"
print("Product added successfully")

price1 = driver.find_element(By.XPATH,"(//tbody/tr/td[3]/p)[1]").text
price2 = driver.find_element(By.XPATH,"(//tbody/tr/td[3]/p)[2]").text
qan1 = driver.find_element(By.XPATH,"(//tbody/tr/td[4]/button)[1]").text
qan2 = driver.find_element(By.XPATH,"(//tbody/tr/td[4]/button)[2]").text
total1 = driver.find_element(By.XPATH,"(//tbody/tr/td[5]/p)[1]").text
total2 = driver.find_element(By.XPATH,"(//tbody/tr/td[5]/p)[2]").text

assert price1 == "Rs. 500"
assert qan1 == "1"
assert total1 == "Rs. 500"

assert price2 == "Rs. 400"
assert qan2 == "1"
assert total2 == "Rs. 400"
print("Validated the cart successfully")

driver.quit()