from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # Импортируем модуль time

# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    # Открытие HTML файла с тестом 1 и нажатие на кнопку "пройти тест"
    browser.get('file:///C:/Users/Admin/Desktop/ISeC/test_1.html')
    btn1_start = browser.find_element(By.ID, 'test_1_start')
    btn1_start.click()

# ВОПРОС 1_1
    # Ожидание 0,1 секунды
    time.sleep(0.5)
    # Выбор отвера на вопрос 1
    ans_1_1 = browser.find_element(By.ID, '1_1_bottom_3')
    ans_1_1.click()
    # Нажатие на кнопку "Далее" вопроса 1
    btn1_1_next = browser.find_element(By.ID, 'btn_1_1_next')
    btn1_1_next.click()

# ВОПРОС 1_2
    time.sleep(0.5)
    ans_1_2 = browser.find_element(By.ID, '1_2_top_0')
    ans_1_2.click()
    btn1_2_next = browser.find_element(By.ID, 'btn_1_2_next')
    btn1_2_next.click()

# ВОПРОС 1_3
    time.sleep(0.5)
    ans_1_3 = browser.find_element(By.ID, '1_3_top_0')
    ans_1_3.click()
    btn1_3_next = browser.find_element(By.ID, 'btn_1_3_next')
    btn1_3_next.click()

# ВОПРОС 1_4
    time.sleep(0.5)
    ans_1_4 = browser.find_element(By.ID, '1_4_top_0')
    ans_1_4.click()
    btn1_4_next = browser.find_element(By.ID, 'btn_1_4_next')
    btn1_4_next.click()

# ВОПРОС 1_5
    time.sleep(0.5)
    ans_1_5 = browser.find_element(By.ID, '1_5_top_0')
    ans_1_5.click()
    btn1_5_next = browser.find_element(By.ID, 'btn_1_5_next')
    btn1_5_next.click()

# ВОПРОС 1_6
    time.sleep(0.5)
    ans_1_6 = browser.find_element(By.ID, '1_6_top_0')
    ans_1_6.click()
    btn1_6_next = browser.find_element(By.ID, 'btn_1_6_next')
    btn1_6_next.click()

# ВОПРОС 1_7
    time.sleep(0.5)
    ans_1_7 = browser.find_element(By.ID, '1_7_top_0')
    ans_1_7.click()
    btn1_7_next = browser.find_element(By.ID, 'btn_1_7_next')
    btn1_7_next.click()

# ВОПРОС 1_8
    time.sleep(0.5)
    ans_1_8 = browser.find_element(By.ID, '1_8_top_0')
    ans_1_8.click()
    btn1_8_next = browser.find_element(By.ID, 'btn_1_8_next')
    btn1_8_next.click()

# ВОПРОС 1_9
    time.sleep(0.5)
    ans_1_9 = browser.find_element(By.ID, '1_9_top_0')
    ans_1_9.click()
    btn1_9_next = browser.find_element(By.ID, 'btn_1_9_next')
    btn1_9_next.click()

# ВОПРОС 1_10
    time.sleep(0.5)
    ans_1_10 = browser.find_element(By.ID, '1_10_top_0')
    ans_1_10.click()
    btn1_10_next = browser.find_element(By.ID, 'btn_1_10_next')
    btn1_10_next.click()

# ВОПРОС 1_11
    time.sleep(0.5)
    ans_1_11 = browser.find_element(By.ID, '1_11_top_0')
    ans_1_11.click()
    btn1_11_next = browser.find_element(By.ID, 'btn_1_11_next')
    btn1_11_next.click()

# ВОПРОС 1_12
    time.sleep(0.5)
    ans_1_12 = browser.find_element(By.ID, '1_12_top_0')
    ans_1_12.click()
    btn1_12_next = browser.find_element(By.ID, 'btn_1_12_next')
    btn1_12_next.click()

# ВОПРОС 1_13
    time.sleep(0.5)
    ans_1_13 = browser.find_element(By.ID, '1_13_top_0')
    ans_1_13.click()
    btn1_13_next = browser.find_element(By.ID, 'btn_1_13_next')
    btn1_13_next.click()

# ВОПРОС 1_14
    time.sleep(0.5)
    ans_1_14 = browser.find_element(By.ID, '1_14_top_0')
    ans_1_14.click()
    btn1_14_next = browser.find_element(By.ID, 'btn_1_14_next')
    btn1_14_next.click()

# ВОПРОС 1_15
    time.sleep(0.5)
    ans_1_15 = browser.find_element(By.ID, '1_15_top_0')
    ans_1_15.click()
    btn1_15_next = browser.find_element(By.ID, 'btn_1_15_next')
    btn1_15_next.click()

# КОНЕЦ БЛОКА 1
    time.sleep(0.5)
    ans_1_end = browser.find_element(By.ID, 'confirm_1_end')
    ans_1_end.click()
    btn1_end_next = browser.find_element(By.ID, 'end_test_next_1')
    btn1_end_next.click()

# СТАРТ БЛОКА 2
    time.sleep(0.5)
    btn2_start = browser.find_element(By.ID, 'test_2_start')
    btn2_start.click()

# ВОПРОС 2_1
    time.sleep(0.5)
    ans_2_1 = browser.find_element(By.ID, '2_1_bottom_3')
    ans_2_1.click()
    btn2_1_next = browser.find_element(By.ID, 'btn_2_1_next')
    btn2_1_next.click()

# ВОПРОС 2_2
    time.sleep(0.5)
    ans_2_2 = browser.find_element(By.ID, '2_2_bottom_3')
    ans_2_2.click()
    btn2_2_next = browser.find_element(By.ID, 'btn_2_2_next')
    btn2_2_next.click()

# ВОПРОС 2_3
    time.sleep(0.5)
    ans_2_3 = browser.find_element(By.ID, '2_3_bottom_3')
    ans_2_3.click()
    btn2_3_next = browser.find_element(By.ID, 'btn_2_3_next')
    btn2_3_next.click()

# ВОПРОС 2_4
    time.sleep(0.5)
    ans_2_4 = browser.find_element(By.ID, '2_4_bottom_3')
    ans_2_4.click()
    btn2_4_next = browser.find_element(By.ID, 'btn_2_4_next')
    btn2_4_next.click()

# ВОПРОС 2_5
    time.sleep(0.5)
    ans_2_5 = browser.find_element(By.ID, '2_5_bottom_3')
    ans_2_5.click()
    btn2_5_next = browser.find_element(By.ID, 'btn_2_5_next')
    btn2_5_next.click()

# ВОПРОС 2_6
    time.sleep(0.5)
    ans_2_6 = browser.find_element(By.ID, '2_6_bottom_3')
    ans_2_6.click()
    btn2_6_next = browser.find_element(By.ID, 'btn_2_6_next')
    btn2_6_next.click()

# ВОПРОС 2_7
    time.sleep(0.5)
    ans_2_7 = browser.find_element(By.ID, '2_7_bottom_3')
    ans_2_7.click()
    btn2_7_next = browser.find_element(By.ID, 'btn_2_7_next')
    btn2_7_next.click()

# ВОПРОС 2_8
    time.sleep(0.5)
    ans_2_8 = browser.find_element(By.ID, '2_8_bottom_3')
    ans_2_8.click()
    btn2_8_next = browser.find_element(By.ID, 'btn_2_8_next')
    btn2_8_next.click()

# ВОПРОС 2_9
    time.sleep(0.5)
    ans_2_9 = browser.find_element(By.ID, '2_9_bottom_3')
    ans_2_9.click()
    btn2_9_next = browser.find_element(By.ID, 'btn_2_9_next')
    btn2_9_next.click()

# ВОПРОС 2_10
    time.sleep(0.5)
    ans_2_10 = browser.find_element(By.ID, '2_10_bottom_3')
    ans_2_10.click()
    btn2_10_next = browser.find_element(By.ID, 'btn_2_10_next')
    btn2_10_next.click()

# ВОПРОС 2_11
    time.sleep(0.5)
    ans_2_11 = browser.find_element(By.ID, '2_11_bottom_3')
    ans_2_11.click()
    btn2_11_next = browser.find_element(By.ID, 'btn_2_11_next')
    btn2_11_next.click()

# ВОПРОС 2_12
    time.sleep(0.5)
    ans_2_12 = browser.find_element(By.ID, '2_12_bottom_3')
    ans_2_12.click()
    btn2_12_next = browser.find_element(By.ID, 'btn_2_12_next')
    btn2_12_next.click()

# ВОПРОС 2_13
    time.sleep(0.5)
    ans_2_13 = browser.find_element(By.ID, '2_13_bottom_3')
    ans_2_13.click()
    btn2_13_next = browser.find_element(By.ID, 'btn_2_13_next')
    btn2_13_next.click()

# ВОПРОС 2_14
    time.sleep(0.5)
    ans_2_14 = browser.find_element(By.ID, '2_14_bottom_3')
    ans_2_14.click()
    btn2_14_next = browser.find_element(By.ID, 'btn_2_14_next')
    btn2_14_next.click()

# ВОПРОС 2_15
    time.sleep(0.5)
    ans_2_15 = browser.find_element(By.ID, '2_15_bottom_3')
    ans_2_15.click()
    btn2_15_next = browser.find_element(By.ID, 'btn_2_15_next')
    btn2_15_next.click()

# ВОПРОС 2_16
    time.sleep(0.5)
    ans_2_16 = browser.find_element(By.ID, '2_16_bottom_3')
    ans_2_16.click()
    btn2_16_next = browser.find_element(By.ID, 'btn_2_16_next')
    btn2_16_next.click()

# ВОПРОС 2_17
    time.sleep(0.5)
    ans_2_17 = browser.find_element(By.ID, '2_17_bottom_3')
    ans_2_17.click()
    btn2_17_next = browser.find_element(By.ID, 'btn_2_17_next')
    btn2_17_next.click()

# ВОПРОС 2_18
    time.sleep(0.5)
    ans_2_18 = browser.find_element(By.ID, '2_18_bottom_3')
    ans_2_18.click()
    btn2_18_next = browser.find_element(By.ID, 'btn_2_18_next')
    btn2_18_next.click()

# ВОПРОС 2_19
    time.sleep(0.5)
    ans_2_19 = browser.find_element(By.ID, '2_19_bottom_3')
    ans_2_19.click()
    btn2_19_next = browser.find_element(By.ID, 'btn_2_19_next')
    btn2_19_next.click()

# ВОПРОС 2_20
    time.sleep(0.5)
    ans_2_20 = browser.find_element(By.ID, '2_20_bottom_3')
    ans_2_20.click()
    btn2_20_next = browser.find_element(By.ID, 'btn_2_20_next')
    btn2_20_next.click()

# ВОПРОС 2_21
    time.sleep(0.5)
    ans_2_21 = browser.find_element(By.ID, '2_21_bottom_3')
    ans_2_21.click()
    btn2_21_next = browser.find_element(By.ID, 'btn_2_21_next')
    btn2_21_next.click()

# ВОПРОС 2_22
    time.sleep(0.5)
    ans_2_22 = browser.find_element(By.ID, '2_22_bottom_3')
    ans_2_22.click()
    btn2_22_next = browser.find_element(By.ID, 'btn_2_22_next')
    btn2_22_next.click()

# ВОПРОС 2_23
    time.sleep(0.5)
    ans_2_23 = browser.find_element(By.ID, '2_23_bottom_3')
    ans_2_23.click()
    btn2_23_next = browser.find_element(By.ID, 'btn_2_23_next')
    btn2_23_next.click()

# ВОПРОС 2_24
    time.sleep(0.5)
    ans_2_24 = browser.find_element(By.ID, '2_24_bottom_3')
    ans_2_24.click()
    btn2_24_next = browser.find_element(By.ID, 'btn_2_24_next')
    btn2_24_next.click()

# ВОПРОС 2_25
    time.sleep(0.5)
    ans_2_25 = browser.find_element(By.ID, '2_25_bottom_3')
    ans_2_25.click()
    btn2_25_next = browser.find_element(By.ID, 'btn_2_25_next')
    btn2_25_next.click()

# ВОПРОС 2_26
    time.sleep(0.5)
    ans_2_26 = browser.find_element(By.ID, '2_26_bottom_3')
    ans_2_26.click()
    btn2_26_next = browser.find_element(By.ID, 'btn_2_26_next')
    btn2_26_next.click()

# ВОПРОС 2_27
    time.sleep(0.5)
    ans_2_27 = browser.find_element(By.ID, '2_27_bottom_3')
    ans_2_27.click()
    btn2_27_next = browser.find_element(By.ID, 'btn_2_27_next')
    btn2_27_next.click()

# ВОПРОС 2_28
    time.sleep(0.5)
    ans_2_28 = browser.find_element(By.ID, '2_28_bottom_3')
    ans_2_28.click()
    btn2_28_next = browser.find_element(By.ID, 'btn_2_28_next')
    btn2_28_next.click()

# ВОПРОС 2_29
    time.sleep(0.5)
    ans_2_29 = browser.find_element(By.ID, '2_29_bottom_3')
    ans_2_29.click()
    btn2_29_next = browser.find_element(By.ID, 'btn_2_29_next')
    btn2_29_next.click()

# ВОПРОС 2_30
    time.sleep(0.5)
    ans_2_30 = browser.find_element(By.ID, '2_30_bottom_3')
    ans_2_30.click()
    btn2_30_next = browser.find_element(By.ID, 'btn_2_30_next')
    btn2_30_next.click()

# КОНЕЦ БЛОКА 2
    time.sleep(0.5)
    ans_2_end = browser.find_element(By.ID, 'confirm_2_end')
    ans_2_end.click()
    btn2_end_next = browser.find_element(By.ID, 'end_test_next_2')
    btn2_end_next.click()

# СТАРТ БЛОКА 3
    time.sleep(0.5)
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



    