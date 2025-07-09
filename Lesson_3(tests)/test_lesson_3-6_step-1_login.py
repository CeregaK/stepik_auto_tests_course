import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_should_see_login_link(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[href="/lesson/236895/step/1?auth=login"]')))
    browser.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys('cerega.kv@yandex.ru')
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys('d---____---g')
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
    time.sleep(20)
