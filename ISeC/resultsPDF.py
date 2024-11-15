

from reportlab.lib.pagesizes import A4  # Импортируем A4 вместо letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
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

    # Сохраняем документ
    can.save()

# Указываем путь к рабочему столу и создаем PDF-файл
desktop_path = os.path.expanduser("~/Desktop")
ISeCRes = os.path.join(desktop_path, "ИКС-файл ФИО.pdf")
create_pdf(ISeCRes)
