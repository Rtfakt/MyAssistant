import time

import numpy as np
import pytesseract
import cv2 as cv
import os
from collections import deque
from filter_text import filter_text, writeOMC
from keyboard import keyboardTap, keyboardLongTap, KeyboardPackagesUdp as KP
from open_programs import OpenPrograms as OP
import pyautogui as pag

path_directory = r"C:\Users\konor\Pictures\Camera Roll"
fileList = deque([])


def getText():
    global last_name_data
    OP.findButtonInMyComputer(OP.WindowsCamIcon)
    pag.click()
    #нопка сделать документ
    OP.findButtonInMyComputer(OP.document_photo)
    pag.click()
    time.sleep(3)

    for root, dirs, files in os.walk(path_directory):  # находим файлы с нужным разрешением и добавляем в список
        for file in files:
            if file.endswith(".jpg"):
                fileList.appendleft(os.path.join(root, file))
                print(fileList)
                filePath = fileList.pop()
                f = open(filePath, "rb") # Открываем нужный файл из списка
                # print(filePath)

                image = cv.imread(filePath) #обрабатываем изображение
                image = cv.resize(image, None, fx=0.5, fy=0.5)
                height, width, _ = image.shape

                blurry = cv.bilateralFilter(image, 20, 30, 30)
                #thresh = cv.adaptiveThreshold(blurry, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 37, 5)

                #распознаем текст
                pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"#Распознаем текст
                OCRresult = pytesseract.image_to_string(image, lang="rus")
                #print(OCRresult)# Получаем полный текст
                try:
                    s = filter_text(OCRresult)  # Фильтруем полный текст и получаем только необходимые данные
                    last_name_data = s[1]
                    first_name_data = s[2]
                    middle_name_data = s[3]
                    birthdate_data = s[4]
                    OMCdata = s[5]
                    print(last_name_data)
                    print(first_name_data)
                    print(middle_name_data)
                    print(birthdate_data)
                    print(OMCdata)
                    # cv.imshow("Test", image)
                    # cv.waitKey()
                    writeOMC(s[5])  # Пишем полученные данные на другом компе
                    keyboardTap(KP.ENTER)
                except:
                    print('Не удалось распознать текст')
                finally:
                    f.close()
                    os.remove(filePath)




