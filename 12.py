import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(3)
##  Открываем сайт и скролим на 600px вниз
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
# Нажимаем на кнопку 'Selenium Ruby' ---> REVIEWS
Ruby = driver.find_element(By.CSS_SELECTOR, '[href="https://practice.automationtesting.in/product/selenium-ruby/"]')
Ruby.click()
Rev = driver.find_element(By.CSS_SELECTOR,'[href="#tab-reviews"]')
Rev.click()
#Ставим 5 звезд
time.sleep(1)
five = driver.find_element(By.CSS_SELECTOR,'.comment-form-rating > p> span > a:nth-child(5)')
five.click()
time.sleep(1)
## Заполните поле "Review" сообщением: "Nice book!" --> Заполните поле "Name" --> Заполните "Email"
Rev_nice = driver.find_element(By.CSS_SELECTOR,'#comment')
Rev_nice.send_keys("Nice book!")
time.sleep(1)
Name = driver.find_element(By.CSS_SELECTOR,'#author')
Name.send_keys("Natali")
time.sleep(1)
email = driver.find_element(By.CSS_SELECTOR,'#email')
email.send_keys("email@email.com")
time.sleep(1)
#Нажмите на кнопку "SUBMIT"
submit = driver.find_element(By.CSS_SELECTOR,'#submit')
submit.click()
### Проверенно, работает. time.sleep()- Не именно здесь не обязательны! Это просто что бы увидеть как все работает.