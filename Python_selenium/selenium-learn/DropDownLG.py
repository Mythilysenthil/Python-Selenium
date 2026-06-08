from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://leafground.com/select.xhtml")
wait = WebDriverWait(driver,10)

# done the select using visible text
select1 = Select(driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']"))
select1.select_by_visible_text("Selenium")
print("Selected successfully by using visible text")

# done the select using index
select2 = Select(driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']"))
select2.select_by_index(1)
print("Selected successfully by using index")

# done the select using options
select3 = Select(driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']"))
opts = select3.options
for option in opts:
   if option.text == "Selenium":
        option.click()
        print("Selected successfully by using options")
        break
driver.quit()