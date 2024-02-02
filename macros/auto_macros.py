import time
import pytesseract
import cv2 as cv
import os
from collections import deque
from filter_text import filter_text, writeOMC
from keyboard import keyboardTap, keyboardLongTap, KeyboardPackagesUdp as KP
from macros.lungs_macros import fluraNorma, rOGK
from omc_control import getScreenTemplate, waitChanges
from open_programs import OpenPrograms as OP
import pyautogui as pag
import asyncio

path_directory = r"C:\Users\konor\Pictures\Camera Roll"
filesList = deque([])
OMCList = deque([])


def autoFluraNorma():
    for root, dirs, files in os.walk(path_directory):  # находим файлы с нужным разрешением и добавляем в список
        for file in files:
            if file.endswith(".jpg"):
                filesList.appendleft(os.path.join(root, file))
                # print(filesList)
                filePath = filesList.pop()
                f = open(filePath, "rb")  # Открываем нужный файл из списка
                # print(filePath)

                image = cv.imread(filePath)  # обрабатываем изображение
                image = cv.resize(image, None, fx=0.5, fy=0.5)
                height, width, _ = image.shape
                gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                blur = cv.bilateralFilter(gray, 20, 30, 30)
                thresh = cv.threshold(blur, 0, 225, cv.THRESH_OTSU)[1]

                pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Распознаем текст
                OCRresult = pytesseract.image_to_string(image, lang="rus")
                # print(OCRresult)  # Получаем полный текст
                s = filter_text(OCRresult)  # Фильтруем полный текст и получаем только необходимые данные
                # print(s[1])
                # print(s[2])
                # print(s[3])
                # print(s[4])
                # print(s[5])
                # cv.imshow("Test", image)
                OMCList.appendleft(s[5])
                # cv.waitKey()
                # keyboardTap(KP.ENTER)
                f.close()
                print("%s %s %s" % (s[1], s[2], s[3]))

                for element in list(OMCList):
                    OMC = OMCList.pop()
                    getScreenTemplate()
                    writeOMC(OMC) # Пишем полученные данные на другом компе
                    keyboardTap(KP.ENTER)
                    #waitChanges()
                    time.sleep(3)
                    fluraNorma()
                    os.remove(filePath)


def autoOGKNorma():
    for root, dirs, files in os.walk(path_directory):  # находим файлы с нужным разрешением и добавляем в список
        for file in files:
            if file.endswith(".jpg"):
                filesList.appendleft(os.path.join(root, file))
                # print(filesList)
                filePath = filesList.pop()
                f = open(filePath, "rb")  # Открываем нужный файл из списка
                # print(filePath)

                image = cv.imread(filePath)  # обрабатываем изображение
                image = cv.resize(image, None, fx=0.5, fy=0.5)
                height, width, _ = image.shape
                gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                blur = cv.bilateralFilter(gray, 20, 30, 30)
                thresh = cv.threshold(blur, 0, 225, cv.THRESH_OTSU)[1]

                pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Распознаем текст
                OCRresult = pytesseract.image_to_string(image, lang="rus")
                # print(OCRresult)  # Получаем полный текст
                s = filter_text(OCRresult)  # Фильтруем полный текст и получаем только необходимые данные
                # print(s[1])
                # print(s[2])
                # print(s[3])
                # print(s[4])
                # print(s[5])
                # cv.imshow("Test", image)
                OMCList.appendleft(s[5])
                # cv.waitKey()
                # keyboardTap(KP.ENTER)
                f.close()
                print("%s %s %s" % (s[1], s[2], s[3]))

                for element in list(OMCList):
                    OMC = OMCList.pop()
                    getScreenTemplate()
                    writeOMC(OMC) # Пишем полученные данные на другом компе
                    keyboardTap(KP.ENTER)
                    waitChanges()
                    rOGK()
                    os.remove(filePath)
