from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    # Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Иван")
    browser.find_element(By.NAME, "lastname").send_keys("Петров")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")
    
    # Загружаем файл
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
    browser.find_element(By.ID, "file").send_keys(file_path)
    
    # Нажимаем кнопку
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(30)
    browser.quit()
