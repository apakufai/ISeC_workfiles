

from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # Импортируем модуль time

# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    browser.get('file:///C:/Users/Admin/Desktop/ISeC/test_1.html')
    btn_1_start = browser.find_element(By.ID, 'test_1_start')
    btn_1_start.click()

# ВОПРОС 1_1
    # Ожидание 0,1 секунды
    time.sleep(0.5)
    # Выбор отвера на вопрос 1
    ans_1_1 = browser.find_element(By.ID, '1_1_bottom_3')
    ans_1_1.click()
    # Нажатие на кнопку "Далее" вопроса 1
    btn_1_1_next = browser.find_element(By.ID, 'btn_1_1_next')
    btn_1_1_next.click()

# ВОПРОС 1_2
    time.sleep(0.5)
    ans_1_2 = browser.find_element(By.ID, '1_2_top_0')
    ans_1_2.click()
    btn_1_2_next = browser.find_element(By.ID, 'btn_1_2_next')
    btn_1_2_next.click()

# ВОПРОС 1_3
    time.sleep(0.5)
    ans_1_3 = browser.find_element(By.ID, '1_3_top_0')
    ans_1_3.click()
    btn_1_3_next = browser.find_element(By.ID, 'btn_1_3_next')
    btn_1_3_next.click()

# ВОПРОС 1_4
    time.sleep(0.5)
    ans_1_4 = browser.find_element(By.ID, '1_4_top_0')
    ans_1_4.click()
    btn_1_4_next = browser.find_element(By.ID, 'btn_1_4_next')
    btn_1_4_next.click()

# ВОПРОС 1_5
    time.sleep(0.5)
    ans_1_5 = browser.find_element(By.ID, '1_5_top_0')
    ans_1_5.click()
    btn_1_5_next = browser.find_element(By.ID, 'btn_1_5_next')
    btn_1_5_next.click()

# ВОПРОС 1_6
    time.sleep(0.5)
    ans_1_6 = browser.find_element(By.ID, '1_6_top_0')
    ans_1_6.click()
    btn_1_6_next = browser.find_element(By.ID, 'btn_1_6_next')
    btn_1_6_next.click()

# ВОПРОС 1_7
    time.sleep(0.5)
    ans_1_7 = browser.find_element(By.ID, '1_7_top_0')
    ans_1_7.click()
    btn_1_7_next = browser.find_element(By.ID, 'btn_1_7_next')
    btn_1_7_next.click()

# ВОПРОС 1_8
    time.sleep(0.5)
    ans_1_8 = browser.find_element(By.ID, '1_8_top_0')
    ans_1_8.click()
    btn_1_8_next = browser.find_element(By.ID, 'btn_1_8_next')
    btn_1_8_next.click()

# ВОПРОС 1_9
    time.sleep(0.5)
    ans_1_9 = browser.find_element(By.ID, '1_9_top_0')
    ans_1_9.click()
    btn_1_9_next = browser.find_element(By.ID, 'btn_1_9_next')
    btn_1_9_next.click()

# ВОПРОС 1_10
    time.sleep(0.5)
    ans_1_10 = browser.find_element(By.ID, '1_10_top_0')
    ans_1_10.click()
    btn_1_10_next = browser.find_element(By.ID, 'btn_1_10_next')
    btn_1_10_next.click()

# ВОПРОС 1_11
    time.sleep(0.5)
    ans_1_11 = browser.find_element(By.ID, '1_11_top_0')
    ans_1_11.click()
    btn_1_11_next = browser.find_element(By.ID, 'btn_1_11_next')
    btn_1_11_next.click()

# ВОПРОС 1_12
    time.sleep(0.5)
    ans_1_12 = browser.find_element(By.ID, '1_12_top_0')
    ans_1_12.click()
    btn_1_12_next = browser.find_element(By.ID, 'btn_1_12_next')
    btn_1_12_next.click()

# ВОПРОС 1_13
    time.sleep(0.5)
    ans_1_13 = browser.find_element(By.ID, '1_13_top_0')
    ans_1_13.click()
    btn_1_13_next = browser.find_element(By.ID, 'btn_1_13_next')
    btn_1_13_next.click()

# ВОПРОС 1_14
    time.sleep(0.5)
    ans_1_14 = browser.find_element(By.ID, '1_14_top_0')
    ans_1_14.click()
    btn_1_14_next = browser.find_element(By.ID, 'btn_1_14_next')
    btn_1_14_next.click()

# ВОПРОС 1_15
    time.sleep(0.5)
    ans_1_15 = browser.find_element(By.ID, '1_15_top_0')
    ans_1_15.click()
    btn_1_15_next = browser.find_element(By.ID, 'btn_1_15_next')
    btn_1_15_next.click()

# КОНЕЦ БЛОКА 1
    time.sleep(0.5)
    ans_1_end = browser.find_element(By.ID, 'confirm_1_end')
    ans_1_end.click()
    btn_1_end_next = browser.find_element(By.ID, 'end_test_next_1')
    btn_1_end_next.click()


except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Ожидание ввода от пользователя, чтобы браузер не закрылся
    input("Нажмите Enter, чтобы закрыть браузер...")
    browser.quit()

