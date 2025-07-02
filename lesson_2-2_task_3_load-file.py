import os 
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

link = "https://suninjuly.github.io/file_input.html"
driver.get(link)

firstname = driver.find_element(By.CSS_SELECTOR, '[name = "firstname"]')
firstname.send_keys("Ivan")
lastname = driver.find_element(By.CSS_SELECTOR, '[name = "lastname"]')
lastname.send_keys("Ivanov")
email = driver.find_element(By.CSS_SELECTOR, '[name = "email"]')
email.send_keys("Ivan@milo.com")
# Находим файл и загружаем его.
file = driver.find_element(By.CSS_SELECTOR, '#file')        # Скрипт работает толькоесли файл file.txt в тойже папке что и этот скрипт.
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
file.send_keys(file_path)

submit_button = driver.find_element(By.CSS_SELECTOR, "[type ='submit']")
driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()
time.sleep(15)

driver.quit()


