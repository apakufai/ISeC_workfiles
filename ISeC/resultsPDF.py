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
html_file = os.path.join("ISeC", "results.html")
resName = extract_value_from_html(html_file, 'resName', expected_type=str)  # Строка
resAdaptation = extract_value_from_html(html_file, 'resAdaptation', expected_type=int)  # Число


if resName is None:
    print("Не удалось найти значение resName.")
else:
    print(f"Значение resName: {resName}")

if resAdaptation is None:
    print("Не удалось найти значение resAdaptation.")
else:
    print(f"Значение resAdaptation: {resAdaptation}")

# Функция для создания PDF-файла


def create_pdf(filename):
    can = canvas.Canvas(filename, pagesize=A4)
    width, height = A4  # Получаем размеры страницы

    # Загрузка и отрисовка первой страницы
    image_path_1 = os.path.join("ISeC", "pagesPDF", "page_1.png")
    if not os.path.exists(image_path_1):
        print(f"Изображение {image_path_1} не найдено.")
        return

    can.drawImage(image_path_1, 0, 0, width=width, height=height)

    # Печать текста на PDF
    can.setFont("Bahnschrift", 14)  # Устанавливаем шрифт и размер
    if resName:  # Проверяем, что resName не None и не пустая строка
        can.drawString(89.738, (height - 556.072), str(resName))  # Печатаем текст
    else:
        print("resName пустое или None, текст не будет напечатан.")
    can.showPage()  # Завершение первой страницы

    # Загрузка и отрисовка второй страницы
    image_path_2 = os.path.join("ISeC", "pagesPDF", "page_2.png")
    if not os.path.exists(image_path_2):
        print(f"Изображение {image_path_2} не найдено.")
        return

    can.drawImage(image_path_2, 0, 0, width=width, height=height)

    if resAdaptation is not None:
        # Вычисляем координаты X для "палочки"
        x_start = 61.978 + (((527.481 - 61.978) / 17) * resAdaptation)
        y_start = height - 768.614  # Фиксированная Y

        # Рисуем круг диаметром 1 пункт
        can.setFillColorRGB(0, 0, 0)  # Устанавливаем цвет заливки (черный)
        circle_radius = 0.5  # Радиус круга в пунктах
        can.circle(x_start, y_start, circle_radius,
                   stroke=0, fill=1)  # Рисуем круг

        # Рисуем "палочку"
        can.setStrokeColorRGB(0, 0, 0)  # Устанавливаем цвет линии (черный)
        can.setLineWidth(1)  # Устанавливаем ширину линии
        # Рисуем линию (палочку)
        can.line(x_start, y_start, x_start, y_start + 30)

        # Рисуем остальные элементы
        can.line(x_start, y_start + 30, x_start - 5, y_start + 35)
        can.circle(x_start - 5, y_start + 35, circle_radius, stroke=0, fill=1)
        can.line(x_start - 5, y_start + 35, x_start, y_start + 40)
        can.circle(x_start, y_start + 40, circle_radius, stroke=0, fill=1)
        can.line(x_start, y_start + 40, x_start + 5, y_start + 35)
        can.circle(x_start + 5, y_start + 35, circle_radius, stroke=0, fill=1)
        can.line(x_start + 5, y_start + 35, x_start, y_start + 30)

    # Сохраняем документ
    can.save()
    print(f"PDF-файл успешно создан: {filename}")


# Указываем путь к рабочему столу и создаем PDF-файл
desktop_path = os.path.expanduser("~/Desktop")
ISeCRes = os.path.join(desktop_path, "ИКС-файл ФИО.pdf")
create_pdf(ISeCRes)
