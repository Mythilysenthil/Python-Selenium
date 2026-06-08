from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/frame.xhtml")

frame = driver.find_element(By.XPATH,"//iframe")
driver.switch_to.frame(frame)

res=driver.find_element(By.XPATH,"(//button[text()='Click Me'])[1]")
res.click()
if res.text == "Hurray! You Clicked Me." :
    print("Frame handled successfully")
else :
    print("Nope")