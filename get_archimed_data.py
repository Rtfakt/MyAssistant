import sqlite3
import numpy as np
import cv2 as cv
import time
from monitor_capture import MonitorCapture
from find_patient import find_patient
import pytesseract
import re
import textwrap
import threading
import keyboard
from monitor_capture import MonitorCapture
from find_archimed_button import FindArchimedButton as FAB
from write_text import ocr_text


def get_arhimed_data():
    while True:
        infoclinika_screen = MonitorCapture('monitor')
        screenshot = infoclinika_screen.get_screenshot()  # получение кадров с камеры
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        '''так как поле с фамилией каждый раз разное, то приходится искать неизменные части
        UI рядом и относительно его находим нужное нам поле
        '''
        # Находим поле с ФИО
        find_fio_text_field = FAB.find(FAB.number_patient, operator_h=FAB.subtraction, operator_w=FAB.addition,
                                       h_value=5, w_value=10)
        coordinates_y = find_fio_text_field[0][1]
        coordinates_x = find_fio_text_field[0][0]
        coordinates_h = coordinates_y - 20
        coordinates_w = coordinates_x + 400
        cropped = screenshot[coordinates_h:coordinates_y,
                  coordinates_x:coordinates_w]  # Верхняя сторона:нижняя сторона, левая:правая
        # Распознаем текст
        fio_data = ocr_text(cropped)
        # if fio_data != None:
        # cv.destroyAllWindows()
        # break
        # Находим поле даты рождения
        find_birthday_text_field = FAB.find(FAB.birthsday, operator_h=FAB.subtraction, operator_w=FAB.addition,
                                            h_value=5, w_value=10)
        coordinates_y = find_birthday_text_field[0][1]
        coordinates_x = find_birthday_text_field[0][0]
        coordinates_h = coordinates_y - 20
        coordinates_w = coordinates_x + 180
        cropped_birthday = screenshot[coordinates_h:coordinates_y, coordinates_x:coordinates_w]
        birthday_date = ocr_text(cropped_birthday)
        # так как tesseract в некоторых размеров окна выдает строку типа "08.02.1935 | №" то убираем лишнее
        birthday_date = birthday_date.split(' ')[0].strip()
        # print(birthday_date)
        # находим поле текущей даты и времени
        find_current_date_field = FAB.find(FAB.current_date_time, operator_h=FAB.subtraction, operator_w=FAB.addition,
                                           h_value=5, w_value=10)
        coordinates_y = find_current_date_field[0][1]
        coordinates_x = find_current_date_field[0][0]
        coordinates_h = coordinates_y - 20
        coordinates_w = coordinates_x + 470
        cropped_current_date = screenshot[coordinates_h:coordinates_y, coordinates_x:coordinates_w]
        current_date_time = ocr_text(cropped_current_date)
        # так как распознанный текст имеет вид '13 Май 2025 года 08:39 Вид' удаляем лишнее, и меняем месяц на число с помощью регулярного выражения
        result = re.sub(r'^(\d{1,2} \w+ \d{4}) года (\d{2}:\d{2}) Вид$', r'\1 \2', current_date_time)
        months = {
            "января": "01",
            "февраля": "02",
            "марта": "03",
            "апреля": "04",
            "мая": "05",
            "июня": "06",
            "июля": "07",
            "августа": "08",
            "сентября": "09",
            "октября": "10",
            "ноября": "11",
            "декабря": "12",
            "январь": "01",
            "февраль": "02",
            "март": "03",
            "апрель": "04",
            "май": "05",
            "июнь": "06",
            "июль": "07",
            "август": "08",
            "сентябрь": "09",
            "октябрь": "10",
            "ноябрь": "11",
            "декабрь": "12"
        }

        parts = result.split(' ')
        time = parts[3]
        day = parts[0]
        year = parts[2]
        month = parts[1].lower()
        month = months[month]
        current_date = day + month + year
        print(current_date)
        print(fio_data)
        print(birthday_date)
        print(day)
        print(month)
        print(year)
        print(time)

        if month != None:
          cv.destroyAllWindows()
          break
        cv.imshow('Read screen', cropped_current_date)

        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break


