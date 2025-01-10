import numpy as np
import cv2 as cv
import time
from monitor_capture import MonitorCapture
import pytesseract



fluoro_screen = MonitorCapture("fluoro_screen")

def get_fluoro_data():
    while True:
        screenshot = fluoro_screen.get_screenshot()  # получение кадров с камеры
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # делаем изображение серым
        cropped = screenshot[40:100, 190:900]
        thresh = cv.threshold(cropped, 0, 255, cv.THRESH_OTSU)[1]






        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Распознаем текст
        OCRresult = pytesseract.image_to_string(thresh, lang="rus")
        print(OCRresult)# Получаем полный текст
        cv.imshow('Read screen', cropped)


        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break