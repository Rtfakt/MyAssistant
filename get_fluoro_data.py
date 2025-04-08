import numpy as np
import cv2 as cv
import time
from monitor_capture import MonitorCapture
from find_patient import find_patient
import pytesseract
import re
import sqlite3
import textwrap
import threading
import keyboard

#fluoro_screen = MonitorCapture("fluoro_screen")
fluoro_patients_dict = {}


def get_fluoro_data():
    while True:
        screenshot = fluoro_screen.get_screenshot()  # получение кадров с камеры
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # делаем изображение серым
        cropped = screenshot[10:40, 28:900]  # Верхняя сторона:нижняя сторона,  координаты полных данных 40:100, 190:900

        # Распознаем текст
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Распознаем текст
        OCRresult = pytesseract.image_to_string(cropped, lang="rus")  # Получаем полный текст
        # Разделяем текст на ФИО и дату
        name = re.findall(r'[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+', OCRresult)[0]
        date = re.findall(r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}', OCRresult)[0]
        # print(name)
        # print(date)
        # добавляем данные в бд fluoro_n.db
        try:
            connection = sqlite3.connect('fluoro_n.db')
            cursor = connection.cursor()
            # print("Подключен к SQLite")

            sqlite_insert_with_param = """INSERT INTO Fluoro_pat
                                  (name, date)
                                  VALUES (?, ?);"""

            data_tuple = (name, date)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            print(f"{name}, {date}  успешно вставлены в таблицу fluoro_n.db")
            connection.commit()
            cursor.execute('SELECT COUNT(*) FROM Fluoro_pat')
            total_users = cursor.fetchone()[0]
            print(f"{total_users} пациентов в базе данных")


            cursor.close()


        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if connection:
                connection.close()
                # print("Соединение с SQLite закрыто")

        if OCRresult != None:
            cv.destroyAllWindows()
            break


def write_fluoro_patient():
    try:
        connection = sqlite3.connect('fluoro_n.db')
        cursor = connection.cursor()
        while True:
            # Подсчет общего числа пользователей
            cursor.execute('SELECT COUNT(*) FROM Fluoro_pat')
            total_users = cursor.fetchone()[0]
            # print(f"{total_users} пациентов в базе данных")
            if total_users > 0:
                # берем первую строку данных из бд fluoro_n.db
                row = connection.cursor().execute("SELECT * FROM Fluoro_pat").fetchone()
                # Преобразуем в словарь
                my_list = list(row)
                name_full = row[0]
                date = row[1]
                # делаем name не больше 32 символа так как поле поиска ФИО больше не принимает
                name = name_full[:30]
                print(name)
                d = {}
                d[name] = date
                print(d)
                find_patient(dict=d)
                # удаляем пользователя из бд
                cursor.execute('DELETE FROM Fluoro_pat WHERE name = ?', (name_full,))
                print(f"{name_full}  удален из базы данных")
                connection.commit()
            else:
                cursor.close()
                connection.commit()
                print('база данных пуста')
                break
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            # print("Соединение с SQLite закрыто")


def debug_fluoro_n():
    try:
        connection = sqlite3.connect('fluoro_n.db')
        cursor = connection.cursor()
        sqlite_select_query = """SELECT * from Fluoro_pat"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("name:", row[0])
            print("date:", row[1])


    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            # print("Соединение с SQLite закрыто")
