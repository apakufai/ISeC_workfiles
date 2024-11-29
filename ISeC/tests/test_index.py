from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    browser.get(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html'))

# ВВОД КОДА
    time.sleep(1.5)
    inputCode = browser.find_element(By.ID, 'inp_code') # ОКНО ВВОДА КОДА
    closeBtn_main_empty = browser.find_element(By.ID, 'closeBtn_start_empty') # ЗАКРЫТИЕ ВСПЛЫВАЮЩЕГО ОКНА С ПУСТЫМ ПОЛЕМ
    closeBtn_main_error = browser.find_element(By.ID, 'closeBtn_start_error') # ЗАКРЫТИЕ ВСПЛЫВАЮЩЕГО ОКНА С ОШИБКОЙ
    btn_main_start = browser.find_element(By.ID, 'startTest') # КНОПКА "ПРОЙТИ ТЕСТ"

    # ПОЛЕ ВВОДА ПУСТО
    btn_main_start.click()
    time.sleep(0.8)
    closeBtn_main_empty.click()
    time.sleep(0.8)

    # ВВЕДЁННЫЙ КОД НЕВЕРЕН
    inputCode.send_keys("321")
    time.sleep(0.8)
    btn_main_start.click()
    time.sleep(0.8)
    closeBtn_main_error.click()
    time.sleep(0.8)

    # ВВЕДЁН ПРАВИЛЬНЫЙ КОД
    inputCode.clear()
    inputCode.send_keys("123")
    time.sleep(0.8)
    btn_main_start.click()


except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Ожидание ввода от пользователя, чтобы браузер не закрылся
    input("Нажмите Enter, чтобы закрыть браузер...")
    browser.quit()