from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://leafground.com/select.xhtml")
wait = WebDriverWait(driver,10)
action = ActionChains(driver)

lang = driver.find_element(By.XPATH,"(//div[@class='col-12']/div/div/following-sibling::label)[3]")
lang.click()
tel = wait.until(EC.visibility_of_element_located((By.XPATH,"//li[@data-label='Telugu']")))
action.scroll_to_element(tel).perform()
tel.click()
print("Language selected successfully using scroll_to_element")

action.scroll_by_amount(0, 200).perform()
print("using scroll_by_amount")
action.scroll_by_amount(0, -200).perform()
print("using scroll amount for scroll back")

origin = ScrollOrigin.from_element(tel)
action.scroll_from_origin(origin,0,130).perform()
print("using scroll_from_origin")