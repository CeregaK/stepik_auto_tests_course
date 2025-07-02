from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]

driver = webdriver.Chrome()
driver.get(link[0])
time.sleep(2)

driver.execute_script(f'window.open("{link[1]}", "_blank");')
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])


# Заполняем форму,используем уникальные селекторы,которые проходят в первом тесте но не проходят во втором.
time.sleep(2)
First_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first')
First_name.send_keys("Ivan")
time.sleep(2)

Last_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second')
Last_name.send_keys("Petrov")
time.sleep(2)

email = driver.find_element(By.CSS_SELECTOR, '.first_block .third')
email.send_keys("milo@milo.com")
time.sleep(2)

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(1)
# Работа с вкладками. Переходим на вторую.
driver.switch_to.window(driver.window_handles[1])

# Вторая вкладка. Заполняем форму,используем уникальные селекторы,которые проходят в первом тесте но не проходят во втором.
time.sleep(2)
First_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first')
First_name.send_keys("Ivan")
time.sleep(2)

Last_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second')
Last_name.send_keys("Petrov")
time.sleep(2)

email = driver.find_element(By.CSS_SELECTOR, '.first_block .third')
email.send_keys("milo@milo.com")
time.sleep(2)

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
driver.quit()
