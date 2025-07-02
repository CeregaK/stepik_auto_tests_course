import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

link = "http://suninjuly.github.io/execute_script.html"
driver.get(link)

#Считываем Х и считаем его
x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = str(math.log(abs(12*math.sin(int(x)))))
time.sleep(1)

 
#Вводим число в поле и пролистываем до поля ввода.
textarea = driver.find_element(By.CSS_SELECTOR, '#answer')
driver.execute_script("return arguments[0].scrollIntoView(true);", textarea)
textarea.send_keys(y)
#Отмечаем checkbox и radiobutton
Chekbx = driver.find_element(By.CSS_SELECTOR, '[for ="robotCheckbox"]')
Chekbx.click()
RoboR = driver.find_element(By.CSS_SELECTOR, '[for ="robotsRule"]')
RoboR.click()
#Пролистываем до кнопки Submit.
submit_button = driver.find_element(By.CSS_SELECTOR, "[type ='submit']")
driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()
time.sleep(15)

driver.quit()



