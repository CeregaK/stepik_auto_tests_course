import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
time.sleep(5)

link = 'https://suninjuly.github.io/selects2.html'
driver.get(link)

#Считываем Х и считаем его
x_element = driver.find_element(By.CSS_SELECTOR, '#num1')
x = x_element.text
y_element = driver.find_element(By.CSS_SELECTOR, '#num2')
y = y_element.text
c = int(x) + int(y)
c = str(c)

#Выбираем нужноечисло в выпадающем списке ID_dropdown
select = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown"))
select.select_by_value(c) 

#Жмем кнопку отправить.
submit_button = driver.find_element(By.CSS_SELECTOR, "[type ='submit']")
submit_button.click()
time.sleep(15)

driver.quit()
