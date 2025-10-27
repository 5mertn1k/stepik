from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    
    # Заполняем поля формы
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    # Находим кнопку Submit с помощью XPath
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # Даем время чтобы увидеть результат
    time.sleep(10)
    # Закрываем браузер
    browser.quit()
