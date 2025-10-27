from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # Ждем, когда цена дома уменьшится до $100 (ожидание 15 секунд)
    wait = WebDriverWait(browser, 15)
    price = wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    # Нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    # Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)
    
    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.ID, "solve")
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
    time.sleep(2)
    browser.quit()
