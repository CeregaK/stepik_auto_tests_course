from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.execute_script("document.title='Мое название страницы';alert('RМы поменяли название страницы!');")
time.sleep(10)
browser.quit()