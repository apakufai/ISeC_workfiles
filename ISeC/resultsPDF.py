from reportlab.lib import colors
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

    if resId is not None:  # Проверяем, что resId не None и не пустая строка
        can.drawString(75, (height - 679.55), str(resId))  # Печатаем текст
    else:
        print("resId пустое или None, текст не будет напечатан.")

    if resName is not None:  # Проверяем, что resName не None и не пустая строка
        can.drawString(89.7, (height - 696.345), str(resName))  # Печатаем текст
    else:
        print("resName пустое или None, текст не будет напечатан.")

    if resSurname is not None:  # Проверяем, что resSurname не None и не пустая строка
        can.drawString(122.5, (height - 713.149), str(resSurname))  # Печатаем текст
    else:
        print("resSurname пустое или None, текст не будет напечатан.")

    if resBirthdate is not None:  # Проверяем, что resBirthdate не None и не пустая строка
        can.drawString(163.838, (height - 730.049), str(resBirthdate))  # Печатаем текст
    else:
        print("resBirthdate пустое или None, текст не будет напечатан.")

    if resCompany is not None:  # Проверяем, что resCompany не None и не пустая строка
        can.drawString(128.02, (height - 746.764), str(resCompany))  # Печатаем текст
    else:
        print("resCompany пустое или None, текст не будет напечатан.")

    if resCategory is not None:  # Проверяем, что resCategory не None и не пустая строка
        can.drawString(129.7, (height - 763.5), str(resCategory))  # Печатаем текст
    else:
        print("resCategory пустое или None, текст не будет напечатан.")

    if resEmail is not None:  # Проверяем, что resEmail не None и не пустая строка
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

        # Функция рисования личного результата на горизонтальной шкале
    def rangeResultHorizontal(range_name, range_x_start, range_x_end, range_y_start, range_divisionsCount):
        # Вычисляем координаты X для "палочки"
        x_start = range_x_start + (((range_x_end - range_x_start) / range_divisionsCount) * range_name)
        y_start = height - range_y_start
        xLeft = -4
        xRight = 4
        yTop = 20
        yCenter = 16
        yBottom = 12
        # Рисуем круг диаметром 1 пункт
        can.setFillColorRGB(0, 0, 0) # Устанавливаем цвет заливки (черный)
        circle_radius = 0.5  # Радиус круга в пунктах
        can.circle(x_start, y_start, circle_radius, stroke=0, fill=1)  # Рисуем круг
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

    if resAdaptation_1 is not None:
        rangeResultHorizontal(resAdaptation_1, 69.033, 526.35, 517.673, 15)

    if resCompromise_1 is not None:
        rangeResultHorizontal(resCompromise_1, 69.033, 526.35, 754.016, 15)

    can.showPage()  # Завершение второй страницы



    # СТРАНИЦА 3
    image_path_3 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_3.png")
    if not os.path.exists(image_path_3):
        print(f"Изображение {image_path_3} не найдено.")
        return
    can.drawImage(image_path_3, 0, 0, width=width, height=height)

    if resBidding_1 is not None:
        rangeResultHorizontal(resBidding_1, 69.033, 526.35, 187.427, 15)

    if resThreat_1 is not None:
        rangeResultHorizontal(resThreat_1, 69.033, 526.35, 406.91, 15)

    if resLogicArgument_1 is not None:
        rangeResultHorizontal(resLogicArgument_1, 69.033, 526.35, 626.394, 15)


    can.showPage()  # Завершение третьей страницы



    # СТРАНИЦА 4
    image_path_4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_4.png")
    if not os.path.exists(image_path_4):
        print(f"Изображение {image_path_4} не найдено.")
        return
    can.drawImage(image_path_4, 0, 0, width=width, height=height)

    if resEmotionsArgument_1 is not None:
        rangeResultHorizontal(resEmotionsArgument_1, 69.033, 526.35, 237.834, 15)


    # Идеальный профиль
        # Устанавливаем начальные и конечные координаты
        start_x_left = 141.732
        start_y_left = height - 785.197
        end_y_left = height - 484.996
        width_left = 141.732

        # Определяем высоту графика, которую мы будем использовать
        fullHeight_left = start_y_left - end_y_left

        # Определяем значения для каждой части графика
        values_left = [
            {"name": "Эмоции", "color": (133/255, 85/255, 85/255), "value": 14},
            {"name": "Логика", "color": (118/255, 102/255, 171/255), "value": 84},
            {"name": "Угроза", "color": (138/255, 171/255, 78/255), "value": 54},
            {"name": "Торги", "color": (200/255, 65/255, 85/255), "value": 63},
            {"name": "Компромисс", "color": (90/255, 127/255, 174/255), "value": 33},
            {"name": "Приспособление", "color": (235/255, 188/255, 109/255), "value": 33},
        ]

        # Начальная позиция по Y для рисования в цикле for каждой части графика
        current_y_left = start_y_left

        # Рисуем график
        for part_left in values_left:
            if part_left["value"] > 0:  # Проверяем, что значение больше 0
                # Рассчитываем высоту на основе значения
                height_left = (fullHeight_left * part_left["value"]) / sum(part["value"] for part in values_left)
                can.setStrokeColorRGB(*part_left["color"])
                can.setLineWidth(width_left)
                can.line(start_x_left, current_y_left, start_x_left, current_y_left - height_left)
                current_y_left -= height_left

    # Ваш профиль
        # Устанавливаем начальные и конечные координаты
        start_x_right = 453.543
        start_y_right = height - 785.197
        end_y_right = height - 484.996
        width_right = 141.732

        # Определяем высоту графика, которую мы будем использовать
        fullHeight_right = start_y_right - end_y_right

        # Определяем значения для каждой части графика
        values_right = [
            {"name": "Эмоции", "color": (133/255, 85/255, 85/255), "value": resEmotionsArgument_1},
            {"name": "Логика", "color": (118/255, 102/255, 171/255), "value": resLogicArgument_1},
            {"name": "Угроза", "color": (138/255, 171/255, 78/255), "value": resThreat_1},
            {"name": "Торги", "color": (200/255, 65/255, 85/255), "value": resBidding_1},
            {"name": "Компромисс", "color": (90/255, 127/255, 174/255), "value": resCompromise_1},
            {"name": "Приспособление", "color": (235/255, 188/255, 109/255), "value": resAdaptation_1},
        ]

        # Начальная позиция по Y для рисования в цикле for каждой части графика
        current_y_right = start_y_right

        # Рисуем график
        for part_right in values_right:
            if part_right["value"] > 0:  # Проверяем, что значение больше 0
                # Рассчитываем высоту на основе значения
                height_right = (fullHeight_right * part_right["value"]) / sum(part["value"] for part in values_right)
                can.setStrokeColorRGB(*part_right["color"])
                can.setLineWidth(width_right)
                can.line(start_x_right, current_y_right, start_x_right, current_y_right - height_right)
                current_y_right -= height_right

    can.showPage()  # Завершение четвёртой страницы



    # СТРАНИЦА 5
    image_path_5 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_5.png")
    if not os.path.exists(image_path_5):
        print(f"Изображение {image_path_5} не найдено.")
        return
    can.drawImage(image_path_5, 0, 0, width=width, height=height)

    # Печать текста на PDF
    can.setFont("Bahnschrift", 14)  # Устанавливаем шрифт и размер

    if resAdaptation_2 is not None:  # Проверяем, что resAdaptation_2 не None
        can.drawString(230, (height - 254.286), str(resAdaptation_2))  # Печатаем текст (ДЧ)
    else:
        print("resAdaptation_2 пустое или None, текст не будет напечатан.")

    if resCompromise_2 is not None:  # Проверяем, что resCompromise_2 не None
        can.drawString(190.113, (height - 287.886), str(resCompromise_2))  # Печатаем текст (П)
    else:
        print("resCompromise_2 пустое или None, текст не будет напечатан.")

    if resThreat_2 is not None:  # Проверяем, что resThreat_2 не None
        can.drawString(189, (height - 321.5), str(resThreat_2))  # Печатаем текст (Б)
    else:
        print("resThreat_2 пустое или None, текст не будет напечатан.")

    if resCooperation_2 is not None:  # Проверяем, что resCooperation_2 не None
        can.drawString(187.463, (height - 271.111), str(resCooperation_2))  # Печатаем текст (В)
    else:
        print("resCooperation_2 пустое или None, текст не будет напечатан.")

    if resAvoidance_2 is not None:  # Проверяем, что resAvoidance_2 не None
        can.drawString(196.658, (height - 304.686), str(resAvoidance_2))  # Печатаем текст (Р)
    else:
        print("resAvoidance_2 пустое или None, текст не будет напечатан.")

    # Устанавливаем цвет и толщину линии
    can.setStrokeColorRGB(199 / 255, 65 / 255, 84 / 255)
    can.setLineWidth(5)

    # Устанавливаем цвет заливки для круга
    can.setFillColorRGB(199 / 255, 65 / 255, 84 / 255)

    # Координаты точек
    soulman_x, soulman_y = 179.528, height - 424.016
    virtuoso_x, virtuoso_y = 429.921, height - 424.016
    politician_x, politician_y = 304.724, height - 549.212
    resident_x, resident_y = 179.528, height - 674.409
    berserker_x, berserker_y = 429.921, height - 674.409

    # Отступы
    axial_hei = 15 # Высота холма вертикальных линий
    axial_wid = 40 # Ширина пика холма вертикальных линий
    diagSmall_hei = 10 # Высота холма малых диагональных линий
    diagSmall_wid = 30 # Ширина пика холма малых диагональных линий
    diagBig_hei = 30 # Высота холма больших диагональных линий
    diagBig_wid = 100 # Ширина пика холма больших диагональных линий
    
    # Душа-человек -> Виртуоз
    def soulman_to_virtuoso():
        can.line(soulman_x, soulman_y, ((soulman_x + virtuoso_x) / 2) - axial_wid, ((soulman_y + virtuoso_y) / 2) + axial_hei)
        can.circle(((soulman_x + virtuoso_x) / 2) - axial_wid, ((soulman_y + virtuoso_y) / 2) + axial_hei, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + virtuoso_x) / 2) - axial_wid, ((soulman_y + virtuoso_y) / 2) + axial_hei, ((soulman_x + virtuoso_x) / 2) + axial_wid, ((soulman_y + virtuoso_y) / 2) + axial_hei)
        can.circle(((soulman_x + virtuoso_x) / 2) + axial_wid, ((soulman_y + virtuoso_y) / 2) + axial_hei, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + virtuoso_x) / 2) + axial_wid, ((soulman_y + virtuoso_y) / 2) + axial_hei, virtuoso_x, virtuoso_y)

    # Виртуоз -> Душа-человек
    def virtuoso_to_soulman():
        can.line(virtuoso_x, virtuoso_y, ((soulman_x + virtuoso_x) / 2) + axial_wid, ((soulman_y + virtuoso_y) / 2) - axial_hei)
        can.circle(((soulman_x + virtuoso_x) / 2) + axial_wid, ((soulman_y + virtuoso_y) / 2) - axial_hei, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + virtuoso_x) / 2) + axial_wid, ((soulman_y + virtuoso_y) / 2) - axial_hei, ((soulman_x + virtuoso_x) / 2) - axial_wid, ((soulman_y + virtuoso_y) / 2) - axial_hei)
        can.circle(((soulman_x + virtuoso_x) / 2) - axial_wid, ((soulman_y + virtuoso_y) / 2) - axial_hei, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + virtuoso_x) / 2) - axial_wid, ((soulman_y + virtuoso_y) / 2) - axial_hei, soulman_x, soulman_y)
    
    # Резидент -> Берсерк
    def resident_to_berserker():
        can.line(resident_x, resident_y, ((resident_x + berserker_x) / 2) - axial_wid, ((resident_y + berserker_y) / 2) + axial_hei)
        can.circle(((resident_x + berserker_x) / 2) - axial_wid, ((resident_y + berserker_y) / 2) + axial_hei, 2.5, stroke=0, fill=1)
        can.line(((resident_x + berserker_x) / 2) - axial_wid, ((resident_y + berserker_y) / 2) + axial_hei, ((resident_x + berserker_x) / 2) + axial_wid, ((resident_y + berserker_y) / 2) + axial_hei)
        can.circle(((resident_x + berserker_x) / 2) + axial_wid, ((resident_y + berserker_y) / 2) + axial_hei, 2.5, stroke=0, fill=1)
        can.line(((resident_x + berserker_x) / 2) + axial_wid, ((resident_y + berserker_y) / 2) + axial_hei, berserker_x, berserker_y)

    # Берсерк -> Резидент
    def berserker_to_resident():
        can.line(berserker_x, berserker_y, ((resident_x + berserker_x) / 2) + axial_wid, ((resident_y + berserker_y) / 2) - axial_hei)
        can.circle(((resident_x + berserker_x) / 2) + axial_wid, ((resident_y + berserker_y) / 2) - axial_hei, 2.5, stroke=0, fill=1)
        can.line(((resident_x + berserker_x) / 2) + axial_wid, ((resident_y + berserker_y) / 2) - axial_hei, ((resident_x + berserker_x) / 2) - axial_wid, ((resident_y + berserker_y) / 2) - axial_hei)
        can.circle(((resident_x + berserker_x) / 2) - axial_wid, ((resident_y + berserker_y) / 2) - axial_hei, 2.5, stroke=0, fill=1)
        can.line(((resident_x + berserker_x) / 2) - axial_wid, ((resident_y + berserker_y) / 2) - axial_hei, resident_x, resident_y)

    # Душа-человек -> Резидент
    def soulman_to_resident():
        can.line(soulman_x, soulman_y, ((soulman_x + resident_x) / 2) - axial_hei, ((soulman_y + resident_y) / 2) + axial_wid)
        can.circle(((soulman_x + resident_x) / 2) - axial_hei, ((soulman_y + resident_y) / 2) + axial_wid, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + resident_x) / 2) - axial_hei, ((soulman_y + resident_y) / 2) + axial_wid, ((soulman_x + resident_x) / 2) - axial_hei, ((soulman_y + resident_y) / 2) - axial_wid)
        can.circle(((soulman_x + resident_x) / 2) - axial_hei, ((soulman_y + resident_y) / 2) - axial_wid, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + resident_x) / 2) - axial_hei, ((soulman_y + resident_y) / 2) - axial_wid, resident_x, resident_y)

    # Резидент -> Душа-человек
    def resident_to_soulman():
        can.line(resident_x, resident_y, ((soulman_x + resident_x) / 2) + axial_hei, ((soulman_y + resident_y) / 2) - axial_wid)
        can.circle(((soulman_x + resident_x) / 2) + axial_hei, ((soulman_y + resident_y) / 2) - axial_wid, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + resident_x) / 2) + axial_hei, ((soulman_y + resident_y) / 2) - axial_wid, ((soulman_x + resident_x) / 2) + axial_hei, ((soulman_y + resident_y) / 2) + axial_wid)
        can.circle(((soulman_x + resident_x) / 2) + axial_hei, ((soulman_y + resident_y) / 2) + axial_wid, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + resident_x) / 2) + axial_hei, ((soulman_y + resident_y) / 2) + axial_wid, soulman_x, soulman_y)

    # Виртуоз -> Берсерк
    def virtuoso_to_berserker():
        can.line(virtuoso_x, virtuoso_y, ((virtuoso_x + berserker_x) / 2) - axial_hei, ((virtuoso_y + berserker_y) / 2) + axial_wid)
        can.circle(((virtuoso_x + berserker_x) / 2) - axial_hei, ((virtuoso_y + berserker_y) / 2) + axial_wid, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + berserker_x) / 2) - axial_hei, ((virtuoso_y + berserker_y) / 2) + axial_wid, ((virtuoso_x + berserker_x) / 2) - axial_hei, ((virtuoso_y + berserker_y) / 2) - axial_wid)
        can.circle(((virtuoso_x + berserker_x) / 2) - axial_hei, ((virtuoso_y + berserker_y) / 2) - axial_wid, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + berserker_x) / 2) - axial_hei, ((virtuoso_y + berserker_y) / 2) - axial_wid, berserker_x, berserker_y)

    # Берсерк -> Виртуоз
    def berserker_to_virtuoso():
        can.line(berserker_x, berserker_y, ((virtuoso_x + berserker_x) / 2) + axial_hei, ((virtuoso_y + berserker_y) / 2) - axial_wid)
        can.circle(((virtuoso_x + berserker_x) / 2) + axial_hei, ((virtuoso_y + berserker_y) / 2) - axial_wid, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + berserker_x) / 2) + axial_hei, ((virtuoso_y + berserker_y) / 2) - axial_wid, ((virtuoso_x + berserker_x) / 2) + axial_hei, ((virtuoso_y + berserker_y) / 2) + axial_wid)
        can.circle(((virtuoso_x + berserker_x) / 2) + axial_hei, ((virtuoso_y + berserker_y) / 2) + axial_wid, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + berserker_x) / 2) + axial_hei, ((virtuoso_y + berserker_y) / 2) + axial_wid, virtuoso_x, virtuoso_y)

    # Душа-человек -> Политик
    def soulman_to_politician():
        can.line(soulman_x, soulman_y, ((soulman_x + politician_x) / 2) - diagSmall_wid + diagSmall_hei, ((soulman_y + politician_y) / 2)  + diagSmall_wid)
        can.circle(((soulman_x + politician_x) / 2) - diagSmall_wid + diagSmall_hei, ((soulman_y + politician_y) / 2)  + diagSmall_wid, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + politician_x) / 2) - diagSmall_wid + diagSmall_hei, ((soulman_y + politician_y) / 2)  + diagSmall_wid, ((soulman_x + politician_x) / 2) + diagSmall_wid, ((soulman_y + politician_y) / 2)  - diagSmall_wid + diagSmall_hei)
        can.circle(((soulman_x + politician_x) / 2) + diagSmall_wid, ((soulman_y + politician_y) / 2)  - diagSmall_wid + diagSmall_hei, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + politician_x) / 2) + diagSmall_wid, ((soulman_y + politician_y) / 2)  - diagSmall_wid + diagSmall_hei, politician_x, politician_y)
    
    # Политик -> Душа-человек
    def politician_to_soulman():
        can.line(politician_x, politician_y, ((soulman_x + politician_x) / 2) + diagSmall_wid - diagSmall_hei, ((soulman_y + politician_y) / 2)  - diagSmall_wid)
        can.circle( ((soulman_x + politician_x) / 2) + diagSmall_wid - diagSmall_hei, ((soulman_y + politician_y) / 2)  - diagSmall_wid, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + politician_x) / 2) + diagSmall_wid - diagSmall_hei, ((soulman_y + politician_y) / 2)  - diagSmall_wid, ((soulman_x + politician_x) / 2) - diagSmall_wid, ((soulman_y + politician_y) / 2)  + diagSmall_wid - diagSmall_hei)
        can.circle(((soulman_x + politician_x) / 2) - diagSmall_wid, ((soulman_y + politician_y) / 2)  + diagSmall_wid - diagSmall_hei, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + politician_x) / 2) - diagSmall_wid, ((soulman_y + politician_y) / 2)  + diagSmall_wid - diagSmall_hei, soulman_x, soulman_y)

    # Политик -> Берсерк
    def politician_to_berserker():
        can.line(politician_x, politician_y, ((politician_x + berserker_x) / 2) - diagSmall_wid + diagSmall_hei, ((politician_y + berserker_y) / 2)  + diagSmall_wid)
        can.circle(((politician_x + berserker_x) / 2) - diagSmall_wid + diagSmall_hei, ((politician_y + berserker_y) / 2)  + diagSmall_wid, 2.5, stroke=0, fill=1)
        can.line(((politician_x + berserker_x) / 2) - diagSmall_wid + diagSmall_hei, ((politician_y + berserker_y) / 2)  + diagSmall_wid, ((politician_x + berserker_x) / 2) + diagSmall_wid, ((politician_y + berserker_y) / 2)  - diagSmall_wid + diagSmall_hei)
        can.circle(((politician_x + berserker_x) / 2) + diagSmall_wid, ((politician_y + berserker_y) / 2)  - diagSmall_wid + diagSmall_hei, 2.5, stroke=0, fill=1)
        can.line(((politician_x + berserker_x) / 2) + diagSmall_wid, ((politician_y + berserker_y) / 2)  - diagSmall_wid + diagSmall_hei, berserker_x, berserker_y)
    
    # Берсерк -> Политик
    def berserker_to_politician():
        can.line(berserker_x, berserker_y, ((politician_x + berserker_x) / 2) + diagSmall_wid - diagSmall_hei, ((politician_y + berserker_y) / 2)  - diagSmall_wid)
        can.circle( ((politician_x + berserker_x) / 2) + diagSmall_wid - diagSmall_hei, ((politician_y + berserker_y) / 2)  - diagSmall_wid, 2.5, stroke=0, fill=1)
        can.line(((politician_x + berserker_x) / 2) + diagSmall_wid - diagSmall_hei, ((politician_y + berserker_y) / 2)  - diagSmall_wid, ((politician_x + berserker_x) / 2) - diagSmall_wid, ((politician_y + berserker_y) / 2)  + diagSmall_wid - diagSmall_hei)
        can.circle(((politician_x + berserker_x) / 2) - diagSmall_wid, ((politician_y + berserker_y) / 2)  + diagSmall_wid - diagSmall_hei, 2.5, stroke=0, fill=1)
        can.line(((politician_x + berserker_x) / 2) - diagSmall_wid, ((politician_y + berserker_y) / 2)  + diagSmall_wid - diagSmall_hei, politician_x, politician_y)

    # Резидент -> Политик
    def resident_to_politician():
        can.line(resident_x, resident_y, ((resident_x + politician_x) / 2) - diagSmall_wid, ((resident_y + politician_y) / 2) - diagSmall_wid + diagSmall_hei)
        can.circle(((resident_x + politician_x) / 2) - diagSmall_wid, ((resident_y + politician_y) / 2) - diagSmall_wid + diagSmall_hei, 2.5, stroke=0, fill=1)
        can.line(((resident_x + politician_x) / 2) - diagSmall_wid, ((resident_y + politician_y) / 2) - diagSmall_wid + diagSmall_hei, ((resident_x + politician_x) / 2) + diagSmall_wid - diagSmall_hei, ((resident_y + politician_y) / 2)  + diagSmall_wid)
        can.circle(((resident_x + politician_x) / 2) + diagSmall_wid - diagSmall_hei, ((resident_y + politician_y) / 2)  + diagSmall_wid, 2.5, stroke=0, fill=1)
        can.line(((resident_x + politician_x) / 2) + diagSmall_wid - diagSmall_hei, ((resident_y + politician_y) / 2)  + diagSmall_wid, politician_x, politician_y)
     
    # Политик -> Резидент
    def politician_to_resident():
        can.line(politician_x, politician_y, ((resident_x + politician_x) / 2) + diagSmall_wid, ((resident_y + politician_y) / 2) + diagSmall_wid - diagSmall_hei)
        can.circle(((resident_x + politician_x) / 2) + diagSmall_wid, ((resident_y + politician_y) / 2) + diagSmall_wid - diagSmall_hei, 2.5, stroke=0, fill=1)
        can.line(((resident_x + politician_x) / 2) + diagSmall_wid, ((resident_y + politician_y) / 2) + diagSmall_wid - diagSmall_hei, ((resident_x + politician_x) / 2) - diagSmall_wid + diagSmall_hei, ((resident_y + politician_y) / 2) - diagSmall_wid)
        can.circle(((resident_x + politician_x) / 2) - diagSmall_wid + diagSmall_hei, ((resident_y + politician_y) / 2) - diagSmall_wid, 2.5, stroke=0, fill=1)
        can.line(((resident_x + politician_x) / 2) - diagSmall_wid + diagSmall_hei, ((resident_y + politician_y) / 2) - diagSmall_wid, resident_x, resident_y)
     
    # Политик -> Виртуоз
    def politician_to_virtuoso():
        can.line(politician_x, politician_y, ((virtuoso_x + politician_x) / 2) - diagSmall_wid, ((virtuoso_y + politician_y) / 2) - diagSmall_wid + diagSmall_hei)
        can.circle(((virtuoso_x + politician_x) / 2) - diagSmall_wid, ((virtuoso_y + politician_y) / 2) - diagSmall_wid + diagSmall_hei, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + politician_x) / 2) - diagSmall_wid, ((virtuoso_y + politician_y) / 2) - diagSmall_wid + diagSmall_hei, ((virtuoso_x + politician_x) / 2) + diagSmall_wid - diagSmall_hei, ((virtuoso_y + politician_y) / 2)  + diagSmall_wid)
        can.circle(((virtuoso_x + politician_x) / 2) + diagSmall_wid - diagSmall_hei, ((virtuoso_y + politician_y) / 2)  + diagSmall_wid, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + politician_x) / 2) + diagSmall_wid - diagSmall_hei, ((virtuoso_y + politician_y) / 2)  + diagSmall_wid, virtuoso_x, virtuoso_y)
     
    # Виртуоз -> Политик
    def virtuoso_to_politician():
        can.line(virtuoso_x, virtuoso_y, ((virtuoso_x + politician_x) / 2) + diagSmall_wid, ((virtuoso_y + politician_y) / 2) + diagSmall_wid - diagSmall_hei)
        can.circle(((virtuoso_x + politician_x) / 2) + diagSmall_wid, ((virtuoso_y + politician_y) / 2) + diagSmall_wid - diagSmall_hei, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + politician_x) / 2) - diagSmall_wid + diagSmall_hei, ((virtuoso_y + politician_y) / 2) - diagSmall_wid, ((virtuoso_x + politician_x) / 2) + diagSmall_wid, ((virtuoso_y + politician_y) / 2) + diagSmall_wid - diagSmall_hei)
        can.circle(((virtuoso_x + politician_x) / 2) - diagSmall_wid + diagSmall_hei, ((virtuoso_y + politician_y) / 2) - diagSmall_wid, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + politician_x) / 2) - diagSmall_wid + diagSmall_hei, ((virtuoso_y + politician_y) / 2) - diagSmall_wid, politician_x, politician_y)

    # Душа-человек -> Берсерк
    def soulman_to_berserker():
        can.line(soulman_x, soulman_y, ((soulman_x + berserker_x) / 2) - diagBig_wid + diagBig_hei, ((soulman_y + berserker_y) / 2)  + diagBig_wid)
        can.circle(((soulman_x + berserker_x) / 2) - diagBig_wid + diagBig_hei, ((soulman_y + berserker_y) / 2)  + diagBig_wid, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + berserker_x) / 2) - diagBig_wid + diagBig_hei, ((soulman_y + berserker_y) / 2)  + diagBig_wid, ((soulman_x + berserker_x) / 2) + diagBig_wid, ((soulman_y + berserker_y) / 2)  - diagBig_wid + diagBig_hei)
        can.circle(((soulman_x + berserker_x) / 2) + diagBig_wid, ((soulman_y + berserker_y) / 2)  - diagBig_wid + diagBig_hei, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + berserker_x) / 2) + diagBig_wid, ((soulman_y + berserker_y) / 2)  - diagBig_wid + diagBig_hei, berserker_x, berserker_y)
     
    # Берсерк -> Душа-человек
    def berserker_to_soulman():
        can.line(berserker_x, berserker_y, ((soulman_x + berserker_x) / 2) + diagBig_wid - diagBig_hei, ((soulman_y + berserker_y) / 2)  - diagBig_wid)
        can.circle( ((soulman_x + berserker_x) / 2) + diagBig_wid - diagBig_hei, ((soulman_y + berserker_y) / 2)  - diagBig_wid, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + berserker_x) / 2) + diagBig_wid - diagBig_hei, ((soulman_y + berserker_y) / 2)  - diagBig_wid, ((soulman_x + berserker_x) / 2) - diagBig_wid, ((soulman_y + berserker_y) / 2)  + diagBig_wid - diagBig_hei)
        can.circle(((soulman_x + berserker_x) / 2) - diagBig_wid, ((soulman_y + berserker_y) / 2)  + diagBig_wid - diagBig_hei, 2.5, stroke=0, fill=1)
        can.line(((soulman_x + berserker_x) / 2) - diagBig_wid, ((soulman_y + berserker_y) / 2)  + diagBig_wid - diagBig_hei, soulman_x, soulman_y)

    # Резидент -> Виртуоз
    def resident_to_virtuoso():
        can.line(resident_x, resident_y, ((virtuoso_x + resident_x) / 2) - diagBig_wid, ((virtuoso_y + resident_y) / 2) - diagBig_wid + diagBig_hei)
        can.circle(((virtuoso_x + resident_x) / 2) - diagBig_wid, ((virtuoso_y + resident_y) / 2) - diagBig_wid + diagBig_hei, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + resident_x) / 2) - diagBig_wid, ((virtuoso_y + resident_y) / 2) - diagBig_wid + diagBig_hei, ((virtuoso_x + resident_x) / 2) + diagBig_wid - diagBig_hei, ((virtuoso_y + resident_y) / 2)  + diagBig_wid)
        can.circle(((virtuoso_x + resident_x) / 2) + diagBig_wid - diagBig_hei, ((virtuoso_y + resident_y) / 2)  + diagBig_wid, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + resident_x) / 2) + diagBig_wid - diagBig_hei, ((virtuoso_y + resident_y) / 2)  + diagBig_wid, virtuoso_x, virtuoso_y)
     
    # Виртуоз -> Резидент
    def virtuoso_to_resident():
        can.line(virtuoso_x, virtuoso_y, ((virtuoso_x + resident_x) / 2) + diagBig_wid, ((virtuoso_y + resident_y) / 2) + diagBig_wid - diagBig_hei)
        can.circle(((virtuoso_x + resident_x) / 2) + diagBig_wid, ((virtuoso_y + resident_y) / 2) + diagBig_wid - diagBig_hei, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + resident_x) / 2) - diagBig_wid + diagBig_hei, ((virtuoso_y + resident_y) / 2) - diagBig_wid, ((virtuoso_x + resident_x) / 2) + diagBig_wid, ((virtuoso_y + resident_y) / 2) + diagBig_wid - diagBig_hei)
        can.circle(((virtuoso_x + resident_x) / 2) - diagBig_wid + diagBig_hei, ((virtuoso_y + resident_y) / 2) - diagBig_wid, 2.5, stroke=0, fill=1)
        can.line(((virtuoso_x + resident_x) / 2) - diagBig_wid + diagBig_hei, ((virtuoso_y + resident_y) / 2) - diagBig_wid, resident_x, resident_y)

    # Сортировка переменных из второго блока
    def sort_variables_2(resAdaptation_2, resCompromise_2, resThreat_2, resCooperation_2, resAvoidance_2):
        # Собираем переменные в словарь
        variables = {
            'soulman': resAdaptation_2,
            'politician': resCompromise_2,
            'berserker': resThreat_2,
            'virtuoso': resCooperation_2,
            'resident': resAvoidance_2
        }
        
        # Сортируем ключи по значениям в порядке убывания
        sorted_keys_2 = sorted(variables, key=variables.get, reverse=True)
        
        return sorted_keys_2, variables

    # Пример вызова функции
    sorted_result, variables = sort_variables_2(resAdaptation_2, resCompromise_2, resThreat_2, resCooperation_2, resAvoidance_2)

    # Проверяем переходы между значениями
    transitions = [
        (sorted_result[0], sorted_result[1]),
        (sorted_result[1], sorted_result[2]),
        (sorted_result[2], sorted_result[3]),
        (sorted_result[3], sorted_result[4]),
    ]

    # Цикл для перебора пар значений
    for pair in transitions:
        first, second = pair  # Разделяем пару на переменные
        # В зависимости от значений переменных вызываем разные функции
        if first == 'soulman' and second == 'virtuoso':
            soulman_to_virtuoso()
        if first == 'virtuoso' and second == 'soulman':
            virtuoso_to_soulman()
        if first == 'resident' and second == 'berserker':
            resident_to_berserker()
        if first == 'berserker' and second == 'resident':
            berserker_to_resident()
        if first == 'soulman' and second == 'resident':
            soulman_to_resident()
        if first == 'resident' and second == 'soulman':
            resident_to_soulman()
        if first == 'virtuoso' and second == 'berserker':
            virtuoso_to_berserker()
        if first == 'berserker' and second == 'virtuoso':
            berserker_to_virtuoso()
        if first == 'soulman' and second == 'politician':
            soulman_to_politician()
        if first == 'politician' and second == 'soulman':
            politician_to_soulman()
        if first == 'politician' and second == 'berserker':
            politician_to_berserker()
        if first == 'berserker' and second == 'politician':
            berserker_to_politician()
        if first == 'resident' and second == 'politician':
            resident_to_politician()
        if first == 'politician' and second == 'resident':
            politician_to_resident()
        if first == 'politician' and second == 'virtuoso':
            politician_to_virtuoso()
        if first == 'virtuoso' and second == 'politician':
            virtuoso_to_politician()
        if first == 'soulman' and second == 'berserker':
            soulman_to_berserker()
        if first == 'berserker' and second == 'soulman':
            berserker_to_soulman()
        if first == 'resident' and second == 'virtuoso':
            resident_to_virtuoso()
        if first == 'virtuoso' and second == 'resident':
            virtuoso_to_resident()
            
    can.showPage()  # Завершение пятой страницы



    # СТРАНИЦА 6
    image_path_6 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_6.png")
    if not os.path.exists(image_path_6):
        print(f"Изображение {image_path_6} не найдено.")
        return
    can.drawImage(image_path_6, 0, 0, width=width, height=height)

    # Печать текста на PDF
    can.setFont("Bahnschrift", 14)  # Устанавливаем шрифт и размер

    if resAdaptation_2 is not None:
        rangeResultHorizontal(resAdaptation_2, 62.242, 532.995, 406.29, 36)

    if resCompromise_2 is not None:
        rangeResultHorizontal(resCompromise_2, 62.242, 532.995, 763.228, 36)
            
    can.showPage()  # Завершение шестой страницы



    # СТРАНИЦА 7
    image_path_7 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_7.png")
    if not os.path.exists(image_path_7):
        print(f"Изображение {image_path_7} не найдено.")
        return
    can.drawImage(image_path_7, 0, 0, width=width, height=height)

    if resThreat_2 is not None:
        rangeResultHorizontal(resThreat_2, 62.242, 532.995, 372.274, 36)

    if resCooperation_2 is not None:
        rangeResultHorizontal(resCooperation_2, 62.242, 532.995, 759.969, 36)
            
    can.showPage()  # Завершение седьмой страницы



    # СТРАНИЦА 8
    image_path_8 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_8.png")
    if not os.path.exists(image_path_8):
        print(f"Изображение {image_path_8} не найдено.")
        return
    can.drawImage(image_path_8, 0, 0, width=width, height=height)

    if resAvoidance_2 is not None:
        rangeResultHorizontal(resAvoidance_2, 62.242, 532.995, 405.865, 36)
            
    can.showPage()  # Завершение восьмой страницы



    # СТРАНИЦА 9
    image_path_9 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_9.png")
    if not os.path.exists(image_path_9):
        print(f"Изображение {image_path_9} не найдено.")
        return
    can.drawImage(image_path_9, 0, 0, width=width, height=height)

    # Печать текста на PDF
    can.setFont("Bahnschrift", 14)  # Устанавливаем шрифт и размер

    # Вычленяем значения из sorted_result[0] и sorted_result[4] для подсчёта разницы между минимумом и максимумом
    value_2_highest = variables[sorted_result[0]]
    value_2_lowest = variables[sorted_result[4]]
    value_2_subtraction = value_2_highest - value_2_lowest

    if value_2_subtraction < 10:
        can.drawString(257, height - 407.777, str(" " + str(value_2_subtraction)))  # Печатаем текст
    else:
        can.drawString(257, height - 407.777, str(value_2_subtraction))  # Печатаем текст
      
    can.showPage()  # Завершение девятой страницы



    # СТРАНИЦА 10
    image_path_10 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_10.png")
    if not os.path.exists(image_path_10):
        print(f"Изображение {image_path_10} не найдено.")
        return
    can.drawImage(image_path_10, 0, 0, width=width, height=height)

        # Функция рисования личного результата на вертикальной шкале
    def rangeResultVertical(range_name, range_y_start, range_y_end, range_x_start, range_divisionsCount):
        # Вычисляем координаты Y для "палочки"
        y_start = height - (range_y_start + (((range_y_end - range_y_start) / range_divisionsCount) * range_name))
        x_start = range_x_start
        yTop = 4
        yBottom = -4
        xLeft = -20
        xCenter = -16
        xRight = -12
        # Рисуем круг диаметром 1 пункт
        can.setFillColorRGB(0, 0, 0) # Устанавливаем цвет заливки (черный)
        circle_radius = 0.5  # Радиус круга в пунктах
        can.circle(x_start, y_start, circle_radius, stroke=0, fill=1)  # Рисуем круг
        # Рисуем "палочку"
        can.setStrokeColorRGB(0, 0, 0)  # Устанавливаем цвет линии (черный)
        can.setLineWidth(1)  # Устанавливаем ширину линии
        # Рисуем линию (палочку)
        can.line(x_start, y_start, x_start + xRight, y_start)
        # Рисуем остальные элементы
        can.line(x_start + xRight, y_start, x_start + xCenter, y_start + yBottom)
        can.circle(x_start + xCenter, y_start + yBottom, circle_radius, stroke=0, fill=1)
        can.line(x_start + xCenter, y_start + yBottom, x_start + xLeft, y_start)
        can.circle(x_start + xLeft, y_start, circle_radius, stroke=0, fill=1)
        can.line(x_start + xLeft, y_start, x_start + xCenter, y_start + yTop)
        can.circle(x_start + xCenter, y_start + yTop, circle_radius, stroke=0, fill=1)
        can.line(x_start + xCenter, y_start + yTop, x_start + xRight, y_start)

    if resAdaptation_3 is not None:
        rangeResultVertical(resAdaptation_3, 779.91, 312.05, 377.157, 27)

    if resThreat_3 is not None:
        rangeResultVertical(resThreat_3, 779.91, 312.05, 440.937, 27)

    if resCooperation_3 is not None:
        rangeResultVertical(resCooperation_3, 779.91, 312.05, 504.716, 27)

    can.showPage()  # Завершение десятой страницы



    # СТРАНИЦА 11
    image_path_11 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_11.png")
    if not os.path.exists(image_path_11):
        print(f"Изображение {image_path_11} не найдено.")
        return
    can.drawImage(image_path_11, 0, 0, width=width, height=height)

    can.showPage()  # Завершение одиннадцатой страницы



    # СТРАНИЦА 12
    image_path_12 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_12.png")
    if not os.path.exists(image_path_12):
        print(f"Изображение {image_path_12} не найдено.")
        return
    can.drawImage(image_path_12, 0, 0, width=width, height=height)

    can.showPage()  # Завершение двенадцатой страницы



    # СТРАНИЦА 13
    image_path_13 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pagesPDF", "page_13.png")
    if not os.path.exists(image_path_13):
        print(f"Изображение {image_path_13} не найдено.")
        return
    can.drawImage(image_path_13, 0, 0, width=width, height=height)

    if resLogicArgument_6 is not None:
        rangeResultHorizontal(resLogicArgument_6, 63.27, 532, 458.646, 30)

    if resEmotionsArgument_6 is not None:
        rangeResultHorizontal(resEmotionsArgument_6, 63.27, 532, 762.315, 30)

    can.showPage()  # Завершение тринадцатой страницы



    # Сохраняем документ
    can.save()
    print(f"PDF-файл успешно создан: {filename}")


# Указываем путь к рабочему столу и создаем PDF-файл
desktop_path = os.path.expanduser("~/Desktop")
ISeCRes = os.path.join(desktop_path, "ИКС-файл " + resId + ".pdf")
create_pdf(ISeCRes)