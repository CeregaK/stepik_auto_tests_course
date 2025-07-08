import os 
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

link = "http://suninjuly.github.io/redirect_accept.html"
driver.get(link)

button = driver.find_element(By.CSS_SELECTOR, "[type ='submit']")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# Работа с вкладками. Переходим на новуювкладку.
driver.switch_to.window(driver.window_handles[1])

#Считываем Х и считаем его
x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = str(math.log(abs(12*math.sin(int(x)))))
time.sleep(1)
textarea = driver.find_element(By.CSS_SELECTOR, '#answer')
textarea.send_keys(y)
submit_button = driver.find_element(By.CSS_SELECTOR, "[type ='submit']")
submit_button.click()




time.sleep(15)
driver.quit()
