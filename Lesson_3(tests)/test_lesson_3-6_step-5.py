import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from ps import psw  #Подключаем файл с паролем и логином.
from ps import lg

# Файл "conftest.py" с функцией "browser" находиться в папке с проектом.
@pytest.mark.parametrize("link", ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
def test_login_link(browser, link):
     browser.implicitly_wait(3)
     browser.get(link)
     # Проверяем есть ли кнопка "Войти",если есть жмем и входим.
     element = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#main-navbar .navbar__auth_login'))) 
     if element:
         browser.execute_script("arguments[0].scrollIntoView();", element[0]) #Скролим до кнопки на случай если она чем то перекрыта.
         element[0].click()
         browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys(lg()) #Импортируем пароль и логин с внешнего файла.
         browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys(psw())
         browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
         popup_close = WebDriverWait(browser, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type = "submit"]')))
         assert popup_close, "Поп-ап с логином не зкрылся"  #Проверяем что окно с логином закрылось и вы успешно вошли.
         print('Вход прошел успешно.') 
     else:
         pass    
     
     # Проверяем активна ли кнопка "Решить снова".Если кнопка активна то "textarea" заблокированна и ничего ввести нельзя. Тогда нажимаем кнопку.
     # Если кнопка не активна то сразу вводим данные в "textarea".
     time.sleep(2)
     btns = browser.find_elements(By.CSS_SELECTOR, '.again-btn')
     if len(btns) > 0:
         btns[0].click()
     else:
         pass         
     time.sleep(2)
     answer = math.log(int(time.time()))
     WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.textarea'))).send_keys(str(answer))
     WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.submit-submission'))).click()
     time.sleep(2)
     element = WebDriverWait(browser, 15).until(EC.visibility_of(browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint')))
     element_text = element.text
     time.sleep(2)
     assert element_text == 'Correct!', f'Текст елемента - \033[35m{element.text}' #Проверяем что текст в фидбеке = "Correct!". Если нет то выводим текст.


