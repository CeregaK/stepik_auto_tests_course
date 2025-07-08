import os 
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/explicit_wait2.html")

#Работа с явными ожиданиями. Ждем пока цена будет '100'  и только после этого жмем кнопку.
button = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), ("100")))

book = driver.find_element(By.CSS_SELECTOR, '#book')
book.click()

x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = str(math.log(abs(12*math.sin(int(x)))))
time.sleep(1)
textarea = driver.find_element(By.CSS_SELECTOR, '#answer')
driver.execute_script("return arguments[0].scrollIntoView(true);", textarea)
textarea.send_keys(y)
submit_button = driver.find_element(By.CSS_SELECTOR, "[type ='submit']")
submit_button.click()



time.sleep(10)
driver.quit()