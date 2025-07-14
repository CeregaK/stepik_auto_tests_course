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



'''link = ['https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1']'''
#def step():
#'lesson/236896/step/1', 'lesson/236897/step/1', 'lesson/236898/step/1', 'lesson/236899/step/1', 'lesson/236903/step/1', 'lesson/236904/step/1', 'lesson/236905/step/1']   
#@pytest.mark.parametrize('step',['236895', '236896', '236897', '236898', '236899','236903','236904', '236905'])


@pytest.mark.parametrize('link', ['lesson/236895/step/1', 'lesson/236896/step/1', 'lesson/236897/step/1', 'lesson/236898/step/1', 'lesson/236899/step/1', 'lesson/236903/step/1', 'lesson/236904/step/1', 'lesson/236905/step/1'])
#@pytest.mark.parametrize('link', ['lesson/236895/step/1', 'lesson/236896/step/1'])
def test_login_link(browser, link):
     new_link = f'https://stepik.org/{link}'
     auth_link = f"[href='/{link}?auth=login']"
     browser.get(new_link)
     element = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, auth_link))) 
    
     if element:
         browser.execute_script("arguments[0].scrollIntoView();", element[0])
         element[0].click()
         browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys(lg())
         time.sleep(1)
         browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys(psw())
         time.sleep(1)
         browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
         time.sleep(1)
         popup_close = WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type = "submit"]')))
         assert popup_close, "Поп-ап с логином не зкрылся"
         print('Вход прошел успешно.')
     else:
         pass        
        
     #answer = math.log(int(time.time()))
     #print('---------------------')
     #print(answer)
     #print('---------------------')
    
    #---------------------------------------------------

    
     #time.sleep(3)
    
     btns = browser.find_elements(By.CSS_SELECTOR,'.again-btn.white')
     if btns:
         btns[0].click()
     else:
         pass
   
    
     time.sleep(1)
     submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'textarea.string-quiz__textarea')))
     browser.execute_script("arguments[0].scrollIntoView();", submit)
     submit.clear()
     time.sleep(1)
     answer = math.log(int(time.time()))
     
     submit.send_keys(answer)
     
     time.sleep(1)
     attempl = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.attempt__actions .submit-submission')))
     browser.execute_script("arguments[0].scrollIntoView();", attempl)
     attempl.click()
     time.sleep(5)
     #----------------____-------------------
    
     #element = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint').text
     #print(f'-------------\n Текст элемента - {element}\n--------------')
    
     
     
     element = WebDriverWait(browser, 10).until(EC.visibility_of(browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint')))
     #content = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'p.smart-hints__hint')))
     time.sleep(5)
     #element = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint').text
     element_text = element.text
     assert element_text == 'Correct!', f'Текст елемента = \033[35m{element.text}'
     print(f'==============\n Текст элемента - \033[35m{element_text}\n--------------')
    

   

    
    
    
    
    
