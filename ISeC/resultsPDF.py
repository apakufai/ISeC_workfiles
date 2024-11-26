from reportlab.lib.pagesizes import A4  # Импортируем A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors  # Импортируем цвета
import os

# Регистрация шрифта Bahnschrift
pdfmetrics.registerFont(TTFont('Bahnschrift', 'Bahnschrift.ttf'))

def create_pdf(filename):
    # Создаем объект Canvas с размером A4
    can = canvas.Canvas(filename, pagesize=A4)
    width, height = A4  # Получаем размеры страницы

    # Добавляем текст с обычным шрифтом Bahnschrift
    can.setFont("Bahnschrift", 24)
    text1 = "ИКС-ФАЙЛ"
    text1_width = can.stringWidth(text1, "Bahnschrift", 24)
    can.drawString((width - text1_width) / 2, height - 50, text1)  # Центрируем по X

    # Добавляем текст с обычным шрифтом Bahnschrift
    can.setFont("Bahnschrift", 16)
    text2 = "Фамилия Имя Отчество"
    text2_width = can.stringWidth(text2, "Bahnschrift", 16)
    can.drawString((width - text2_width) / 2, height - 75, text2)  # Центрируем по X

    can.showPage()  # Завершение первой страницы и переход на вторую

    # Параметры для линии и "палочек"
    line_start_x = 50
    line_start_y = 600
    line_length = 450  # Длина линии
    num_parts = 30
    part_length = line_length / num_parts
    stick_length = 10  # Длина "палочек"
    stick_width = 2  # Толщина линии и "палочек"
    distance_between_sticks = 15  # Расстояние между "палочками"

    # Рисуем линию
    can.setStrokeColor(colors.HexColor('#FFC618'))
    can.setLineWidth(stick_width)
    can.line(line_start_x, line_start_y, line_start_x + line_length, line_start_y)

    # Рисуем "палочки" и цифры
    for i in range(num_parts + 1):
        stick_x = line_start_x + i * part_length
        # Рисуем "палочку"
        can.line(stick_x, line_start_y, stick_x, line_start_y + stick_length)
        # Рисуем цифры под "палочками"
        can.drawString(stick_x - 4, line_start_y - 20, str(i))

    # Добавляем красную линию от основания палочки над числом 12
    red_line_start_x = line_start_x + 12 * part_length  # x-координата палочки над 12
    red_line_start_y = line_start_y + stick_length  # y-координата основания палочки
    red_line_end_y = red_line_start_y + 30  # Конечная y-координата красной линии

    can.setStrokeColor(colors.red)  # Устанавливаем красный цвет
    can.line(red_line_start_x, red_line_start_y, red_line_start_x, red_line_end_y)

    # Рисуем круг в конечной точке красной линии
    circle_diameter = stick_width
    circle_radius = circle_diameter / 2
    can.circle(red_line_start_x, red_line_end_y, circle_radius)

    # Добавляем линию вправо до оси линии над цифрой 20
    second_line_start_x = red_line_start_x
    second_line_start_y = red_line_end_y
    second_line_end_x = line_start_x + 20 * part_length  # x-координата над 20

    can.line(second_line_start_x, second_line_start_y, second_line_end_x, second_line_start_y)

    # Рисуем круг в конечной точке второй линии
    can.circle(second_line_end_x, second_line_start_y, circle_radius)

    # Добавляем красную линию вниз от правой точки второй линии
    final_line_start_x = second_line_end_x
    final_line_start_y = second_line_start_y
    final_line_end_y = final_line_start_y - 30  # Конечная y-координата

    can.line(final_line_start_x, final_line_start_y, final_line_start_x, final_line_end_y)

    # Заканчиваем страницу
    can.showPage()

    # Сохраняем документ
    can.save()

# Указываем путь к рабочему столу и создаем PDF-файл
desktop_path = os.path.expanduser("~/Desktop")
ISeCRes = os.path.join(desktop_path, "ИКС-файл ФИО.pdf")
create_pdf(ISeCRes)