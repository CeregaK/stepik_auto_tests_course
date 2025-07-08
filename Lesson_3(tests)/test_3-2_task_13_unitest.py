
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
#---------Тесты--------------
class TestRegistr(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual( welcome_text, "Congratulations! You have successfully registered!", "Что то не то" )
        
#---------------Тесты---------


## Выбираем адрес страницы теста ниже. На первой странице тест проходит, на второй ошибка - "NoSuchElementException "
link_1 = "https://suninjuly.github.io/registration1.html"
link_2 = "https://suninjuly.github.io/registration2.html"


driver = webdriver.Chrome()
driver.get(link_2)
####-----Заполняем формы
First_name = driver.find_element(By.CSS_SELECTOR, '.first_block .first')
First_name.send_keys("Ivan")
time.sleep(1)

Last_name = driver.find_element(By.CSS_SELECTOR, '.first_block .second')
Last_name.send_keys("Petrov")
time.sleep(1)

email = driver.find_element(By.CSS_SELECTOR, '.first_block .third')
email.send_keys("milo@milo.com")
time.sleep(1)

#-----Кнопка отправки
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

#-----Проверка
time.sleep(1)
welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

if __name__ == "__main__":
    unittest.main()
    
#assert "Congratulations! You have successfully registered!" == welcome_text

#---------------------------
time.sleep(2)
browser.quit()


