import time

import pytesseract
import cv2 as cv
import os
from collections import deque
from filter_text import scan_text, writeOMC
from keyboard import keyboardTap, keyboardLongTap, KeyboardPackagesUdp as KP
from open_programs import OpenPrograms as OP
import pyautogui as pag

path_directory = r"C:\Users\konor\Pictures\Camera Roll"
fileList = deque([])


def getText():
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
                f = open(filePath, "rb")
                # print(filePath)
                image = cv.imread(filePath)
                image = cv.resize(image, None, fx=0.5, fy=0.5)
                height, width, _ = image.shape
                gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                blur = cv.bilateralFilter(gray, 20, 30, 30)
                thresh = cv.threshold(blur, 0, 225, cv.THRESH_OTSU)[1]
                pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                OCRresult = pytesseract.image_to_string(image, lang="rus")
                print(OCRresult)
                s = scan_text(OCRresult)
                print(s[1])
                print(s[2])
                print(s[3])
                print(s[4])
                print(s[5])
                # cv.imshow("Test", image)
                # cv.waitKey()
                writeOMC(s[5])
                keyboardTap(KP.ENTER)
                f.close()
                os.remove(filePath)




'''
def getText():
    for root, dirs, files in os.walk(path_directory):  # находим файлы с нужным разрешением и добавляем в список
        for file in files:
            if file.endswith(".jpg"):
                fileList.append(os.path.join(root, file))

        while True:
            try:
                filePath = fileList.popleft()
                f = open(filePath, "rb")
                # print(filePath)
                image = cv.imread(filePath)
                image = cv.resize(image, None, fx=0.5, fy=0.5)
                height, width, _ = image.shape
                gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                blur = cv.bilateralFilter(gray, 20, 30, 30)
                thresh = cv.threshold(blur, 0, 225, cv.THRESH_OTSU)[1]
                pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                OCRresult = pytesseract.image_to_string(image, lang="rus")
                #print(OCRresult)
                s = scan_text(OCRresult)
                print(s[1])
                print(s[2])
                print(s[3])
                print(s[4])
                print(s[5])
                #cv.imshow("Test", image)
                # cv.waitKey()
                writeOMC(s[5])
                keyboardTap(KP.ENTER)
                os.remove(filePath)
            except StopIteration:
                break

'''