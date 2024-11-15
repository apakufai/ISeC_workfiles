from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # Импортируем модуль time

# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    browser.get('file:///C:/Users/Admin/Desktop/ISeC/test_4.html')
    btn_4_start = browser.find_element(By.ID, 'test_4_start')
    btn_4_start.click()

# ВОПРОС 4_1
    time.sleep(0.5)
    ans_4_1 = browser.find_element(By.ID, '4_1_1')
    ans_4_1.click()
    btn_4_1_next = browser.find_element(By.ID, 'btn_4_1_next')
    btn_4_1_next.click()

# ВОПРОС 4_2
    time.sleep(0.5)
    ans_4_2 = browser.find_element(By.ID, '4_2_1')
    ans_4_2.click()
    btn_4_2_next = browser.find_element(By.ID, 'btn_4_2_next')
    btn_4_2_next.click()

# ВОПРОС 4_3
    time.sleep(0.5)
    ans_4_3 = browser.find_element(By.ID, '4_3_1')
    ans_4_3.click()
    btn_4_3_next = browser.find_element(By.ID, 'btn_4_3_next')
    btn_4_3_next.click()

# ВОПРОС 4_4
    time.sleep(0.5)
    ans_4_4 = browser.find_element(By.ID, '4_4_1')
    ans_4_4.click()
    btn_4_4_next = browser.find_element(By.ID, 'btn_4_4_next')
    btn_4_4_next.click()

# ВОПРОС 4_5
    time.sleep(0.5)
    ans_4_5 = browser.find_element(By.ID, '4_5_1')
    ans_4_5.click()
    btn_4_5_next = browser.find_element(By.ID, 'btn_4_5_next')
    btn_4_5_next.click()

# ВОПРОС 4_6
    time.sleep(0.5)
    ans_4_6 = browser.find_element(By.ID, '4_6_1')
    ans_4_6.click()
    btn_4_6_next = browser.find_element(By.ID, 'btn_4_6_next')
    btn_4_6_next.click()

# ВОПРОС 4_7
    time.sleep(0.5)
    ans_4_7 = browser.find_element(By.ID, '4_7_1')
    ans_4_7.click()
    btn_4_7_next = browser.find_element(By.ID, 'btn_4_7_next')
    btn_4_7_next.click()

# ВОПРОС 4_8
    time.sleep(0.5)
    ans_4_8 = browser.find_element(By.ID, '4_8_1')
    ans_4_8.click()
    btn_4_8_next = browser.find_element(By.ID, 'btn_4_8_next')
    btn_4_8_next.click()

# ВОПРОС 4_9
    time.sleep(0.5)
    ans_4_9 = browser.find_element(By.ID, '4_9_1')
    ans_4_9.click()
    btn_4_9_next = browser.find_element(By.ID, 'btn_4_9_next')
    btn_4_9_next.click()

# ВОПРОС 4_10
    time.sleep(0.5)
    ans_4_10 = browser.find_element(By.ID, '4_10_1')
    ans_4_10.click()
    btn_4_10_next = browser.find_element(By.ID, 'btn_4_10_next')
    btn_4_10_next.click()

# ВОПРОС 4_11
    time.sleep(0.5)
    ans_4_11 = browser.find_element(By.ID, '4_11_1')
    ans_4_11.click()
    btn_4_11_next = browser.find_element(By.ID, 'btn_4_11_next')
    btn_4_11_next.click()

# ВОПРОС 4_12
    time.sleep(0.5)
    ans_4_12 = browser.find_element(By.ID, '4_12_1')
    ans_4_12.click()
    btn_4_12_next = browser.find_element(By.ID, 'btn_4_12_next')
    btn_4_12_next.click()

# ВОПРОС 4_13
    time.sleep(0.5)
    ans_4_13 = browser.find_element(By.ID, '4_13_1')
    ans_4_13.click()
    btn_4_13_next = browser.find_element(By.ID, 'btn_4_13_next')
    btn_4_13_next.click()

# ВОПРОС 4_14
    time.sleep(0.5)
    ans_4_14 = browser.find_element(By.ID, '4_14_1')
    ans_4_14.click()
    btn_4_14_next = browser.find_element(By.ID, 'btn_4_14_next')
    btn_4_14_next.click()

# ВОПРОС 4_15
    time.sleep(0.5)
    ans_4_15 = browser.find_element(By.ID, '4_15_1')
    ans_4_15.click()
    btn_4_15_next = browser.find_element(By.ID, 'btn_4_15_next')
    btn_4_15_next.click()

# ВОПРОС 4_16
    time.sleep(0.5)
    ans_4_16 = browser.find_element(By.ID, '4_16_1')
    ans_4_16.click()
    btn_4_16_next = browser.find_element(By.ID, 'btn_4_16_next')
    btn_4_16_next.click()

# КОНЕЦ БЛОКА 4
    time.sleep(0.5)
    ans_4_end = browser.find_element(By.ID, 'confirm_4_end')
    ans_4_end.click()
    btn_4_end_next = browser.find_element(By.ID, 'end_test_next_4')
    btn_4_end_next.click()


except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Ожидание ввода от пользователя, чтобы браузер не закрылся
    input("Нажмите Enter, чтобы закрыть браузер...")
    browser.quit()

