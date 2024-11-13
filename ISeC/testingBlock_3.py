from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # Импортируем модуль time

# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    # Открытие HTML файла с тестом 1 и нажатие на кнопку "пройти тест"
    browser.get('file:///C:/Users/Admin/Desktop/ISeC/test_3.html')
    btn3_start = browser.find_element(By.ID, 'test_3_start')
    btn3_start.click()

# ВОПРОС 3_1
    time.sleep(0.5)

    
    btn_3_1_next = browser.find_element(By.ID, 'btn_3_1_next')
    btn_3_1_next.click()



except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Ожидание ввода от пользователя, чтобы браузер не закрылся
    input("Нажмите Enter, чтобы закрыть браузер...")
    browser.quit()



    