import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from ps import psw
from ps import lg


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

link = "https://stepik.org/lesson/236895/step/1"
browser.get(link)

element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[href="/lesson/236895/step/1?auth=login"]')))
browser.execute_script("arguments[0].scrollIntoView();", element)
element.click()
browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys(lg())
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys(psw())
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
time.sleep(1)
popup_close = WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type = "submit"]')))
assert popup_close, "Поп-ап с логином не зкрылся"
print('Вход прошел успешно.')
answer = math.log(int(time.time()))
print('---------------------')
print(answer)
print('---------------------')
time.sleep(2)
submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'textarea.string-quiz__textarea')))
submit.clear()
time.sleep(1)
submit.send_keys(answer)
time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '.attempt__actions .submit-submission').click()
time.sleep(2)
content = browser.find_element(By.CSS_SELECTOR, '#ember541> .smart-hints__hint')
text = content.text
print(text)
  
    
