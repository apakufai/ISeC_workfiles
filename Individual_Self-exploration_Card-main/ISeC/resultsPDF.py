from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import re

# Регистрация шрифта Bahnschrift
try:
    pdfmetrics.registerFont(TTFont('Bahnschrift', 'Bahnschrift.ttf'))
except Exception as e:
    print(f"Ошибка при регистрации шрифта: {e}")



# Функция для извлечения значения переменной из "results.html"
def extract_value_from_html(file_path, variable_name, expected_type=str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Регулярное выражение для поиска строкового или числового значения
            match = re.search(
                rf'let {variable_name}\s*=\s*["\']?([^"\';]+)["\']?', content)
            if match:
                value = match.group(1)  # Извлекаем значение
                if expected_type == str:
                    return value  # Возвращаем строковое значение
                elif expected_type == int:  # Только int
                    try:
                        return int(value)  # Преобразуем в целое число
                    except ValueError:
                        print(f"Не удалось преобразовать значение '{value}' в {expected_type.__name__}.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
    return None

# Извлечение значений переменных
html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.html")

resName = extract_value_from_html(html_file, 'resName', expected_type=str)
resSurname = extract_value_from_html(html_file, 'resSurname', expected_type=str)
resSex = extract_value_from_html(html_file, 'resSex', expected_type=str)
resBirthdate = extract_value_from_html(html_file, 'resBirthdate', expected_type=str)
resCompany = extract_value_from_html(html_file, 'resCompany', expected_type=str)
resCategory = extract_value_from_html(html_file, 'resCategory', expected_type=str)
resEmail = extract_value_from_html(html_file, 'resEmail', expected_type=str)
resId = extract_value_from_html(html_file, 'resId', expected_type=str)
resUnderstandingOfStyles = extract_value_from_html(html_file, 'resUnderstandingOfStyles', expected_type=int)
resAdaptation = extract_value_from_html(html_file, 'resAdaptation', expected_type=int)
resCompromise = extract_value_from_html(html_file, 'resCompromise', expected_type=int)
resBidding = extract_value_from_html(html_file, 'resBidding', expected_type=int)
resThreat = extract_value_from_html(html_file, 'resThreat', expected_type=int)
resLogicArgument = extract_value_from_html(html_file, 'resLogicArgument', expected_type=int)
resEmotionsArgument = extract_value_from_html(html_file, 'resEmotionsArgument', expected_type=int)
resStrengthInstallation = extract_value_from_html(html_file, 'resStrengthInstallation', expected_type=int)
resManipulationInstallation = extract_value_from_html(html_file, 'resManipulationInstallation', expected_type=int)
resNegotiationsInstallation = extract_value_from_html(html_file, 'resNegotiationsInstallation', expected_type=int)
resCooperation = extract_value_from_html(html_file, 'resCooperation', expected_type=int)
resAvoidance = extract_value_from_html(html_file, 'resAvoidance', expected_type=int)

resAdaptation_1 = extract_value_from_html(html_file, 'resAdaptation_1', expected_type=int)
resCompromise_1 = extract_value_from_html(html_file, 'resCompromise_1', expected_type=int)
resBidding_1 = extract_value_from_html(html_file, 'resBidding_1', expected_type=int)
resThreat_1 = extract_value_from_html(html_file, 'resThreat_1', expected_type=int)
resLogicArgument_1 = extract_value_from_html(html_file, 'resLogicArgument_1', expected_type=int)
resEmotionsArgument_1 = extract_value_from_html(html_file, 'resEmotionsArgument_1', expected_type=int)

resAdaptation_2 = extract_value_from_html(html_file, 'resAdaptation_2', expected_type=int)
resCompromise_2 = extract_value_from_html(html_file, 'resCompromise_2', expected_type=int)
resThreat_2 = extract_value_from_html(html_file, 'resThreat_2', expected_type=int)
resCooperation_2 = extract_value_from_html(html_file, 'resCooperation_2', expected_type=int)
resAvoidance_2 = extract_value_from_html(html_file, 'resAvoidance_2', expected_type=int)

resAdaptation_3 = extract_value_from_html(html_file, 'resAdaptation_3', expected_type=int)
resThreat_3 = extract_value_from_html(html_file, 'resThreat_3', expected_type=int)
resCooperation_3 = extract_value_from_html(html_file, 'resCooperation_3', expected_type=int)

resStrengthInstallation_4 = extract_value_from_html(html_file, 'resStrengthInstallation_4', expected_type=int)
resManipulationInstallation_4 = extract_value_from_html(html_file, 'resManipulationInstallation_4', expected_type=int)
resNegotiationsInstallation_4 = extract_value_from_html(html_file, 'resNegotiationsInstallation_4', expected_type=int)

resAdaptation_5 = extract_value_from_html(html_file, 'resAdaptation_5', expected_type=int)
resBidding_5 = extract_value_from_html(html_file, 'resBidding_5', expected_type=int)
resLogicArgument_5 = extract_value_from_html(html_file, 'resLogicArgument_5', expected_type=int)
resEmotionsArgument_5 = extract_value_from_html(html_file, 'resEmotionsArgument_5', expected_type=int)
resAvoidance_5 = extract_value_from_html(html_file, 'resAvoidance_5', expected_type=int)

resLogicArgument_6 = extract_value_from_html(html_file, 'resLogicArgument_6', expected_type=int)
resEmotionsArgument_6 = extract_value_from_html(html_file, 'resEmotionsArgument_6', expected_type=int)



if resAdaptation_2 is None:
    print("Не удалось найти значение resAdaptation_2.")
else:
    print(f"Значение resAdaptation_2: {resAdaptation_2}")

if resCompromise_2 is None:
    print("Не удалось найти значение resCompromise_2.")
else:
    print(f"Значение resCompromise_2: {resCompromise_2}")

if resThreat_2 is None:
    print("Не удалось найти значение resThreat_2.")
else:
    print(f"Значение resThreat_2: {resThreat_2}")

if resCooperation_2 is None:
    print("Не удалось найти значение resCooperation_2.")
else:
    print(f"Значение resCooperation_2: {resCooperation_2}")

if resAvoidance_2 is None:
    print("Не удалось найти значение resAvoidance_2.")
else:
    print(f"Значение resAvoidance_2: {resAvoidance_2}")


# ПРОВЕРКИ!!!

if resName is None:
    print("Не удалось найти значение resName.")
else:
    print(f"Значение resName: {resName}")

if resSurname is None:
    print("Не удалось найти значение resSurname.")
else:
    print(f"Значение resSurname: {resSurname}")

if resSex is None:
    print("Не удалось найти значение resSex.")
else:
    print(f"Значение resSex: {resSex}")

if resBirthdate is None:
    print("Не удалось найти значение resBirthdate.")
else:
    print(f"Значение resBirthdate: {resBirthdate}")

if resCompany is None:
    print("Не удалось найти значение resCompany.")
else:
    print(f"Значение resCompany: {resCompany}")

if resCategory is None:
    print("Не удалось найти значение resCategory.")
else:
    print(f"Значение resCategory: {resCategory}")

if resEmail is None:
    print("Не удалось найти значение resEmail.")
else:
    print(f"Значение resEmail: {resEmail}")

if resId is None:
    print("Не удалось найти значение resId.")
else:
    print(f"Значение resId: {resId}") 



if resUnderstandingOfStyles is None:
    print("Не удалось найти значение resUnderstandingOfStyles.")
else:
    print(f"Значение resUnderstandingOfStyles: {resUnderstandingOfStyles}")

if resAdaptation is None:
    print("Не удалось найти значение resAdaptation.")
else:
    print(f"Значение resAdaptation: {resAdaptation}")

if resCompromise is None:
    print("Не удалось найти значение resCompromise.")
else:
    print(f"Значение resCompromise: {resCompromise}")

if resBidding is None:
    print("Не удалось найти значение resBidding.")
else:
    print(f"Значение resBidding: {resBidding}")

if resThreat is None:
    print("Не удалось найти значение resThreat.")
else:
    print(f"Значение resThreat: {resThreat}")

if resLogicArgument is None:
    print("Не удалось найти значение resLogicArgument.")
else:
    print(f"Значение resLogicArgument: {resLogicArgument}")

if resEmotionsArgument is None:
    print("Не удалось найти значение resEmotionsArgument.")
else:
    print(f"Значение resEmotionsArgument: {resEmotionsArgument}")

if resStrengthInstallation is None:
    print("Не удалось найти значение resStrengthInstallation.")
else:
    print(f"Значение resStrengthInstallation: {resStrengthInstallation}")

if resManipulationInstallation is None:
    print("Не удалось найти значение resManipulationInstallation.")
else:
    print(f"Значение resManipulationInstallation: {resManipulationInstallation}")

if resNegotiationsInstallation is None:
    print("Не удалось найти значение resNegotiationsInstallation.")
else:
    print(f"Значение resNegotiationsInstallation: {resNegotiationsInstallation}")

if resCooperation is None:
    print("Не удалось найти значение resCooperation.")
else:
    print(f"Значение resCooperation: {resCooperation}")

if resAvoidance is None:
    print("Не удалось найти значение resAvoidance.")
else:
    print(f"Значение resAvoidance: {resAvoidance}")



if resAdaptation_1 is None:
    print("Не удалось найти значение resAdaptation_1.")
else:
    print(f"Значение resAdaptation_1: {resAdaptation_1}")

if resCompromise_1 is None:
    print("Не удалось найти значение resCompromise_1.")
else:
    print(f"Значение resCompromise_1: {resCompromise_1}")

if resBidding_1 is None:
    print("Не удалось найти значение resBidding_1.")
else:
    print(f"Значение resBidding_1: {resBidding_1}")

if resThreat_1 is None:
    print("Не удалось найти значение resThreat_1.")
else:
    print(f"Значение resThreat_1: {resThreat_1}")

if resLogicArgument_1 is None:
    print("Не удалось найти значение resLogicArgument_1.")
else:
    print(f"Значение resLogicArgument_1: {resLogicArgument_1}")

if resEmotionsArgument_1 is None:
    print("Не удалось найти значение resEmotionsArgument_1.")
else:
    print(f"Значение resEmotionsArgument_1: {resEmotionsArgument_1}")



if resAdaptation_2 is None:
    print("Не удалось найти значение resAdaptation_2.")
else:
    print(f"Значение resAdaptation_2: {resAdaptation_2}")

if resCompromise_2 is None:
    print("Не удалось найти значение resCompromise_2.")
else:
    print(f"Значение resCompromise_2: {resCompromise_2}")

if resThreat_2 is None:
    print("Не удалось найти значение resThreat_2.")
else:
    print(f"Значение resThreat_2: {resThreat_2}")

if resCooperation_2 is None:
    print("Не удалось найти значение resCooperation_2.")
else:
    print(f"Значение resCooperation_2: {resCooperation_2}")

if resAvoidance_2 is None:
    print("Не удалось найти значение resAvoidance_2.")
else:
    print(f"Значение resAvoidance_2: {resAvoidance_2}")



if resAdaptation_3 is None:
    print("Не удалось найти значение resAdaptation_3.")
else:
    print(f"Значение resAdaptation_3: {resAdaptation_3}")

if resThreat_3 is None:
    print("Не удалось найти значение resThreat_3.")
else:
    print(f"Значение resThreat_3: {resThreat_3}")

if resCooperation_3 is None:
    print("Не удалось найти значение resCooperation_3.")
else:
    print(f"Значение resCooperation_3: {resCooperation_3}")



if resStrengthInstallation_4 is None:
    print("Не удалось найти значение resStrengthInstallation_4.")
else:
    print(f"Значение resStrengthInstallation_4: {resStrengthInstallation_4}")

if resManipulationInstallation_4 is None:
    print("Не удалось найти значение resManipulationInstallation_4.")
else:
    print(f"Значение resManipulationInstallation_4: {resManipulationInstallation_4}")

if resNegotiationsInstallation_4 is None:
    print("Не удалось найти значение resNegotiationsInstallation_4.")
else:
    print(f"Значение resNegotiationsInstallation_4: {resNegotiationsInstallation_4}")



if resAdaptation_5 is None:
    print("Не удалось найти значение resAdaptation_5.")
else:
    print(f"Значение resAdaptation_5: {resAdaptation_5}")

if resBidding_5 is None:
    print("Не удалось найти значение resBidding_5.")
else:
    print(f"Значение resBidding_5: {resBidding_5}")

if resLogicArgument_5 is None:
    print("Не удалось найти значение resLogicArgument_5.")
else:
    print(f"Значение resLogicArgument_5: {resLogicArgument_5}")

if resEmotionsArgument_5 is None:
    print("Не удалось найти значение resEmotionsArgument_5.")
else:
    print(f"Значение resEmotionsArgument_5: {resEmotionsArgument_5}")

if resAvoidance_5 is None:
    print("Не удалось найти значение resAvoidance_5.")
else:
    print(f"Значение resAvoidance_5: {resAvoidance_5}")



if resLogicArgument_6 is None:
    print("Не удалось найти значение resLogicArgument_6.")
else:
    print(f"Значение resLogicArgument_6: {resLogicArgument_6}")

if resEmotionsArgument_6 is None:
    print("Не удалось найти значение resEmotionsArgument_6.")
else:
    print(f"Значение resEmotionsArgument_6: {resEmotionsArgument_6}")




# Функция для создания PDF-файла
def create_pdf(filename):
    can = canvas.Canvas(filename, pagesize=A4)
    width, height = A4  # Получаем размеры страницы



    # СТРАНИЦА 1
    image_path_1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_1.png")
    if not os.path.exists(image_path_1):
        print(f"Изображение {image_path_1} не найдено.")
        return

    can.drawImage(image_path_1, 0, 0, width=width, height=height)

    # Печать текста на PDF
    can.setFont("Bahnschrift", 14)  # Устанавливаем шрифт и размер

    if resId:  # Проверяем, что resId не None и не пустая строка
        can.drawString(75, (height - 679.55), str(resId))  # Печатаем текст
    else:
        print("resId пустое или None, текст не будет напечатан.")

    if resName:  # Проверяем, что resName не None и не пустая строка
        can.drawString(89.7, (height - 696.345), str(resName))  # Печатаем текст
    else:
        print("resName пустое или None, текст не будет напечатан.")

    if resSurname:  # Проверяем, что resSurname не None и не пустая строка
        can.drawString(122.5, (height - 713.149), str(resSurname))  # Печатаем текст
    else:
        print("resSurname пустое или None, текст не будет напечатан.")

    if resBirthdate:  # Проверяем, что resBirthdate не None и не пустая строка
        can.drawString(163.838, (height - 730.049), str(resBirthdate))  # Печатаем текст
    else:
        print("resBirthdate пустое или None, текст не будет напечатан.")

    if resCompany:  # Проверяем, что resCompany не None и не пустая строка
        can.drawString(128.02, (height - 746.764), str(resCompany))  # Печатаем текст
    else:
        print("resCompany пустое или None, текст не будет напечатан.")

    if resCategory:  # Проверяем, что resCategory не None и не пустая строка
        can.drawString(129.7, (height - 763.5), str(resCategory))  # Печатаем текст
    else:
        print("resCategory пустое или None, текст не будет напечатан.")

    if resEmail:  # Проверяем, что resEmail не None и не пустая строка
        can.drawString(124.2, (height - 780.3), str(resEmail))  # Печатаем текст
    else:
        print("resEmail пустое или None, текст не будет напечатан.")

    can.showPage()  # Завершение первой страницы



    # СТРАНИЦА 2
    image_path_2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_2.png")
    if not os.path.exists(image_path_2):
        print(f"Изображение {image_path_2} не найдено.")
        return

    can.drawImage(image_path_2, 0, 0, width=width, height=height)

    if resAdaptation_1 is not None:
        # Вычисляем координаты X для "палочки"
        x_start = 69.033 + (((526.35 - 69.033) / 15) * resAdaptation_1)
        y_start = height - 517.673
        xLeft = -4
        xRight = 4
        yTop = 20
        yCenter = 16
        yBottom = 12
        # Рисуем круг диаметром 1 пункт
        can.setFillColorRGB(0, 0, 0) # Устанавливаем цвет заливки (черный)
        circle_radius = 0.5  # Радиус круга в пунктах
        can.circle(x_start, y_start, circle_radius,
                   stroke=0, fill=1)  # Рисуем круг
        # Рисуем "палочку"
        can.setStrokeColorRGB(0, 0, 0)  # Устанавливаем цвет линии (черный)
        can.setLineWidth(1)  # Устанавливаем ширину линии
        # Рисуем линию (палочку)
        can.line(x_start, y_start, x_start, y_start + yBottom)
        # Рисуем остальные элементы
        can.line(x_start, y_start + yBottom, x_start + xLeft, y_start + yCenter)
        can.circle(x_start + xLeft, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xLeft, y_start + yCenter, x_start, y_start + yTop)
        can.circle(x_start, y_start + yTop, circle_radius, stroke=0, fill=1)
        can.line(x_start, y_start + yTop, x_start + xRight, y_start + yCenter)
        can.circle(x_start + xRight, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xRight, y_start + yCenter, x_start, y_start + yBottom)

    if resCompromise_1 is not None:
        # Вычисляем координаты X для "палочки"
        x_start = 69.033 + (((526.35 - 69.033) / 15) * resCompromise_1)
        y_start = height - 754.016
        xLeft = -4
        xRight = 4
        yTop = 20
        yCenter = 16
        yBottom = 12
        # Рисуем круг диаметром 1 пункт
        can.setFillColorRGB(0, 0, 0) # Устанавливаем цвет заливки (черный)
        circle_radius = 0.5  # Радиус круга в пунктах
        can.circle(x_start, y_start, circle_radius,
                   stroke=0, fill=1)  # Рисуем круг
        # Рисуем "палочку"
        can.setStrokeColorRGB(0, 0, 0)  # Устанавливаем цвет линии (черный)
        can.setLineWidth(1)  # Устанавливаем ширину линии
        # Рисуем линию (палочку)
        can.line(x_start, y_start, x_start, y_start + yBottom)
        # Рисуем остальные элементы
        can.line(x_start, y_start + yBottom, x_start + xLeft, y_start + yCenter)
        can.circle(x_start + xLeft, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xLeft, y_start + yCenter, x_start, y_start + yTop)
        can.circle(x_start, y_start + yTop, circle_radius, stroke=0, fill=1)
        can.line(x_start, y_start + yTop, x_start + xRight, y_start + yCenter)
        can.circle(x_start + xRight, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xRight, y_start + yCenter, x_start, y_start + yBottom)

    can.showPage()  # Завершение второй страницы



    # СТРАНИЦА 3
    image_path_3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_3.png")
    if not os.path.exists(image_path_3):
        print(f"Изображение {image_path_3} не найдено.")
        return

    can.drawImage(image_path_3, 0, 0, width=width, height=height)

    if resBidding_1 is not None:
        # Вычисляем координаты X для "палочки"
        x_start = 69.033 + (((526.35 - 69.033) / 15) * resBidding_1)
        y_start = height - 187.427
        xLeft = -4
        xRight = 4
        yTop = 20
        yCenter = 16
        yBottom = 12
        # Рисуем круг диаметром 1 пункт
        can.setFillColorRGB(0, 0, 0) # Устанавливаем цвет заливки (черный)
        circle_radius = 0.5  # Радиус круга в пунктах
        can.circle(x_start, y_start, circle_radius,
                   stroke=0, fill=1)  # Рисуем круг
        # Рисуем "палочку"
        can.setStrokeColorRGB(0, 0, 0)  # Устанавливаем цвет линии (черный)
        can.setLineWidth(1)  # Устанавливаем ширину линии
        # Рисуем линию (палочку)
        can.line(x_start, y_start, x_start, y_start + yBottom)
        # Рисуем остальные элементы
        can.line(x_start, y_start + yBottom, x_start + xLeft, y_start + yCenter)
        can.circle(x_start + xLeft, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xLeft, y_start + yCenter, x_start, y_start + yTop)
        can.circle(x_start, y_start + yTop, circle_radius, stroke=0, fill=1)
        can.line(x_start, y_start + yTop, x_start + xRight, y_start + yCenter)
        can.circle(x_start + xRight, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xRight, y_start + yCenter, x_start, y_start + yBottom)

    if resThreat_1 is not None:
        # Вычисляем координаты X для "палочки"
        x_start = 69.033 + (((526.35 - 69.033) / 15) * resThreat_1)
        y_start = height - 406.91
        xLeft = -4
        xRight = 4
        yTop = 20
        yCenter = 16
        yBottom = 12
        # Рисуем круг диаметром 1 пункт
        can.setFillColorRGB(0, 0, 0) # Устанавливаем цвет заливки (черный)
        circle_radius = 0.5  # Радиус круга в пунктах
        can.circle(x_start, y_start, circle_radius,
                   stroke=0, fill=1)  # Рисуем круг
        # Рисуем "палочку"
        can.setStrokeColorRGB(0, 0, 0)  # Устанавливаем цвет линии (черный)
        can.setLineWidth(1)  # Устанавливаем ширину линии
        # Рисуем линию (палочку)
        can.line(x_start, y_start, x_start, y_start + yBottom)
        # Рисуем остальные элементы
        can.line(x_start, y_start + yBottom, x_start + xLeft, y_start + yCenter)
        can.circle(x_start + xLeft, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xLeft, y_start + yCenter, x_start, y_start + yTop)
        can.circle(x_start, y_start + yTop, circle_radius, stroke=0, fill=1)
        can.line(x_start, y_start + yTop, x_start + xRight, y_start + yCenter)
        can.circle(x_start + xRight, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xRight, y_start + yCenter, x_start, y_start + yBottom)

    if resLogicArgument_1 is not None:
        # Вычисляем координаты X для "палочки"
        x_start = 69.033 + (((526.35 - 69.033) / 15) * resLogicArgument_1)
        y_start = height - 626.394
        xLeft = -4
        xRight = 4
        yTop = 20
        yCenter = 16
        yBottom = 12
        # Рисуем круг диаметром 1 пункт
        can.setFillColorRGB(0, 0, 0) # Устанавливаем цвет заливки (черный)
        circle_radius = 0.5  # Радиус круга в пунктах
        can.circle(x_start, y_start, circle_radius,
                   stroke=0, fill=1)  # Рисуем круг
        # Рисуем "палочку"
        can.setStrokeColorRGB(0, 0, 0)  # Устанавливаем цвет линии (черный)
        can.setLineWidth(1)  # Устанавливаем ширину линии
        # Рисуем линию (палочку)
        can.line(x_start, y_start, x_start, y_start + yBottom)
        # Рисуем остальные элементы
        can.line(x_start, y_start + yBottom, x_start + xLeft, y_start + yCenter)
        can.circle(x_start + xLeft, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xLeft, y_start + yCenter, x_start, y_start + yTop)
        can.circle(x_start, y_start + yTop, circle_radius, stroke=0, fill=1)
        can.line(x_start, y_start + yTop, x_start + xRight, y_start + yCenter)
        can.circle(x_start + xRight, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xRight, y_start + yCenter, x_start, y_start + yBottom)

    can.showPage()  # Завершение третьей страницы



    # СТРАНИЦА 4
    image_path_4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_4.png")
    if not os.path.exists(image_path_4):
        print(f"Изображение {image_path_4} не найдено.")
        return

    can.drawImage(image_path_4, 0, 0, width=width, height=height)

    if resEmotionsArgument_1 is not None:
        # Вычисляем координаты X для "палочки"
        x_start = 69.033 + (((526.35 - 69.033) / 15) * resEmotionsArgument_1)
        y_start = height - 237.834
        xLeft = -4
        xRight = 4
        yTop = 20
        yCenter = 16
        yBottom = 12
        # Рисуем круг диаметром 1 пункт
        can.setFillColorRGB(0, 0, 0) # Устанавливаем цвет заливки (черный)
        circle_radius = 0.5  # Радиус круга в пунктах
        can.circle(x_start, y_start, circle_radius,
                   stroke=0, fill=1)  # Рисуем круг
        # Рисуем "палочку"
        can.setStrokeColorRGB(0, 0, 0)  # Устанавливаем цвет линии (черный)
        can.setLineWidth(1)  # Устанавливаем ширину линии
        # Рисуем линию (палочку)
        can.line(x_start, y_start, x_start, y_start + yBottom)
        # Рисуем остальные элементы
        can.line(x_start, y_start + yBottom, x_start + xLeft, y_start + yCenter)
        can.circle(x_start + xLeft, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xLeft, y_start + yCenter, x_start, y_start + yTop)
        can.circle(x_start, y_start + yTop, circle_radius, stroke=0, fill=1)
        can.line(x_start, y_start + yTop, x_start + xRight, y_start + yCenter)
        can.circle(x_start + xRight, y_start + yCenter, circle_radius, stroke=0, fill=1)
        can.line(x_start + xRight, y_start + yCenter, x_start, y_start + yBottom)


    can.showPage()  # Завершение четвёртой страницы





    # Сохраняем документ
    can.save()
    print(f"PDF-файл успешно создан: {filename}")


# Указываем путь к рабочему столу и создаем PDF-файл
desktop_path = os.path.expanduser("~/Desktop")
ISeCRes = os.path.join(desktop_path, "ИКС-файл ФИО.pdf")
create_pdf(ISeCRes)
