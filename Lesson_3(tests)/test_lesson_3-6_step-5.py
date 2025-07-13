import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()

#@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    element = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[href="/lesson/236895/step/1?auth=login"]')))
    browser.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys('c----------------u')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys('d-------------g')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
    time.sleep(1)
    popup_close = WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'[type = "submit"]')))
    assert popup_close, "Поп-ап с логином не зкрылся"
    print('Вход прошел успешно.')
    answer = math.log(int(time.time()))
    print('---------------------')
    print(answer)
    print('---------------------')
    
    #---------------------------------------------------
    """try:
        browser.find_element_by_css_selector("#ctl00_PlaceHolderMain_ReportViewer1_HtmlOutputReportResults2_updateFilters_TitleAnchor").click()
    except NoSuchElementException:
        # do stuff"""
    
    time.sleep(5)
    btns = browser.find_elements(By.CSS_SELECTOR,'.again-btn.white')
    if btns:
        btns[0].click()
    else:
        pass
   
    
    time.sleep(1)
    submit = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'textarea.string-quiz__textarea')))
    submit.clear()
    time.sleep(1)
    submit.send_keys(answer)
    time.sleep(1)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.attempt__actions .submit-submission'))).click()
    time.sleep(5)
    #----------------____-------------------
    
    content = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'p.smart-hints__hint'), 'Correct!'))
    if content:
        element = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint').text
        print(f'-------------\n Текст элемента - {element}\n--------------')
  
    
    
    
    
    
