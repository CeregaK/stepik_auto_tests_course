import os 
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

link = "http://suninjuly.github.io/alert_accept.html"
driver.get(link)

submit_button = driver.find_element(By.CSS_SELECTOR, "[type ='submit']")
submit_button.click()
# Переключаемся на allert и жмем accept(соглашаемся\принимаем)
alert = driver.switch_to.alert
alert.accept()
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
