from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    
    # Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Принимаем confirm
    alert = browser.switch_to.alert
    alert.accept()
    
    # Ждем загрузки новой страницы
    time.sleep(1)
    
    # Решаем капчу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    
    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    
    # Получаем число из alert с ответом
    time.sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    answer = alert_text.split(": ")[-1]
    print(f"Ответ: {answer}")
    alert.accept()

finally:
    # Закрываем браузер
    time.sleep(10)
    browser.quit()
