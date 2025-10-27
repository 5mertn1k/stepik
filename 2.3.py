from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    
    # Находим числа на странице
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    
    # Получаем текст чисел и преобразуем в целые
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    
    # Считаем сумму
    total = num1 + num2
    print(f"Сумма чисел: {num1} + {num2} = {total}")
    
    # Находим выпадающий список
    dropdown = Select(browser.find_element(By.TAG_NAME, "select"))
    
    # Выбираем значение равное сумме (преобразуем в строку!)
    dropdown.select_by_value(str(total))
    
    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Даем время скопировать код
    time.sleep(30)
    browser.quit()
