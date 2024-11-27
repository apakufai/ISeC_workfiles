from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time  # Импортируем модуль time

# Инициализация веб-драйвера
browser = webdriver.Chrome()

try:
    browser.get('file:///C:/Users/Admin/Desktop/ISeC/userDataInput.html')

# ВВОД ДАННЫХ ПОЛЬЗОВАТЕЛЯ
    time.sleep(1)
    btn_UDI_next = browser.find_element(By.ID, 'btn_UDI_next') # КНОПКА "ПРОДОЛЖИТЬ"
    closeBtn_UDI = browser.find_element(By.ID, 'closeBtn_UDI') # ЗАКРЫТИЕ ВСПЛЫВАЮЩЕГО ОКНА
    inputName = browser.find_element(By.ID, 'user_name') # ИМЯ
    inputSurname = browser.find_element(By.ID, 'user_surname') # ФАМИЛИЯ
    inputSexFemale = browser.find_element(By.ID, 'user_sex_female') # ПОЛ
    inputBirthdate = browser.find_element(By.ID, 'user_birthdate') # ДАТА РОЖДЕНИЯ
    inputCompany = browser.find_element(By.ID, 'user_company') # ПОЛ
    inputCategory = Select(browser.find_element(By.ID, 'user_category')) # КАТЕГОРИЯ
    inputEmail = browser.find_element(By.ID, 'user_email') # ЭЛ.ПОЧТА
    inputAgreement = browser.find_element(By.ID, 'user_confirmation') # СОГЛАСИЕ НА ОБРАБОТКУ ДАННЫХ


    # ДАННЫЕ НЕ ВВЕДЕНЫ
    btn_UDI_next.click()
    time.sleep(0.5)
    closeBtn_UDI.click()
    time.sleep(0.5)


    # ДАННЫЕ ВВЕДЕНЫ НЕВЕРНО
    inputName.send_keys("!!!")
    time.sleep(0.1)
    inputSurname.send_keys("!!!")
    time.sleep(0.1)
    inputBirthdate.send_keys("31.02.2000")
    time.sleep(0.1)
    inputCompany.send_keys("!!!")
    time.sleep(0.1)
    inputEmail.send_keys("!!!")
    time.sleep(0.5)
    
    btn_UDI_next.click()
    time.sleep(0.5)
    closeBtn_UDI.click()
    time.sleep(0.5)

    inputName.clear()
    time.sleep(0.1)
    inputSurname.clear()
    time.sleep(0.1)
    inputBirthdate.clear()
    time.sleep(0.1)
    inputCompany.clear()
    time.sleep(0.1)
    inputEmail.clear()
    time.sleep(0.5)


    # ВВЕДЕНЫ ВЕРНЫЕ ДАННЫЕ
    inputName.send_keys("Анна-Мария")
    time.sleep(0.1)
    inputSurname.send_keys("Мамина-Алексеева")
    time.sleep(0.1)
    inputSexFemale.click()
    time.sleep(0.1)
    inputBirthdate.send_keys("01022000")
    time.sleep(0.1)
    inputCompany.send_keys("ООО «Компания '\"Агрохим-cuprum\" и сыновья'»")
    time.sleep(0.1)
    inputCategory.select_by_value("-")
    time.sleep(0.1)
    inputEmail.send_keys("Mamina-Alek_jr.@tr-ili.ax.com")
    time.sleep(0.1)
    inputAgreement.click()
    time.sleep(0.5)
    btn_UDI_next.click()


except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Ожидание ввода от пользователя, чтобы браузер не закрылся
    input("Нажмите Enter, чтобы закрыть браузер...")
    browser.quit()