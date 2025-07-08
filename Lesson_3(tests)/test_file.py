
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_reg1():

    link_1 = "https://suninjuly.github.io/registration1.html"
    driver = webdriver.Chrome()
    driver.get(link_1)
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

    # -----Кнопка отправки
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert welcome_text == welcome_text_elt.text, "Поздравляем! Вы успешно зарегистировались!"


def test_reg2():


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

    # -----Кнопка отправки
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert welcome_text == welcome_text_elt.text, "Поздравляем! Вы успешно зарегистировались!"



if __name__ == "__main__":
    pytest.main()

