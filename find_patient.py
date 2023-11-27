import cv2 as cv
import numpy as np
import pytesseract
from imutils import contours


# firstPosition(78, 280)
# secondPosition(300, 930)
def findPatient():
    screenshot = cv.imread('example_images/screenFail.png')
    crop_img = screenshot[280:930, 78:350]

    blurry = cv.bilateralFilter(crop_img, 20, 30, 30)
    thresh = cv.adaptiveThreshold(blurry, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 37, 5)

    # убираем вертикальные линии
    hor = np.array([[1, 1, 1, 1, 1, 1]])
    vertical_lines_eroded_image = cv.erode(thresh, hor, iterations=3)
    vertical_lines_eroded_image = cv.dilate(vertical_lines_eroded_image, hor, iterations=10)

    # убираем горизонтальные линии
    ver = np.array([[1], [1], [1], [1], [1], [1], [1]])
    horizontal_lines_eroded_image = cv.erode(thresh, ver, iterations=3)
    horizontal_lines_eroded_image = cv.dilate(horizontal_lines_eroded_image, ver, iterations=10)
    # соединяем горизонтальные и вертикальные линии
    combined_image = cv.add(vertical_lines_eroded_image, horizontal_lines_eroded_image)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
    combined_image_dilated = cv.dilate(combined_image, kernel, iterations=1)
    # получаем изображение без линий
    image_without_lines = cv.subtract(thresh, combined_image_dilated)


    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Распознаем текст
    OCRResult = pytesseract.image_to_string(image_without_lines, lang="rus", config='--psm 1')
    splitOCRResult = OCRResult.splitlines()
    print(splitOCRResult)
    str = 'Иванов Иван Иванович 05.10.2010'
    #index = patient_list.index(str)
    #print(index)


    cv.imshow('result', image_without_lines)

    cv.waitKey()


'''
def findPatient():
    screenshot = cv.imread('example_images/screenFail.png', 0)
    crop_img = screenshot[278:930, 278:350]

    blurry = cv.bilateralFilter(crop_img, 20, 30, 30)
    thresh = cv.adaptiveThreshold(blurry, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 37, 5)

    # убираем вертикальные линии
    hor = np.array([[1, 1, 1, 1, 1, 1]])
    vertical_lines_eroded_image = cv.erode(thresh, hor, iterations=3)
    vertical_lines_eroded_image = cv.dilate(vertical_lines_eroded_image, hor, iterations=10)

    # убираем горизонтальные линии
    ver = np.array([[1], [1], [1], [1], [1], [1], [1]])
    horizontal_lines_eroded_image = cv.erode(thresh, ver, iterations=3)
    horizontal_lines_eroded_image = cv.dilate(horizontal_lines_eroded_image, ver, iterations=10)
    # соединяем горизонтальные и вертикальные линии
    combined_image = cv.add(vertical_lines_eroded_image, horizontal_lines_eroded_image)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
    combined_image_dilated = cv.dilate(combined_image, kernel, iterations=1)
    # получаем изображение без линий
    image_without_lines = cv.subtract(thresh, combined_image_dilated)


    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Распознаем текст
    OCRResult = pytesseract.image_to_string(image_without_lines, lang="rus", config='--psm 6')
    splitOCRResult = OCRResult.splitlines()
    patient_list = splitOCRResult
    print(OCRResult)
    #str = 'Иванов Иван Романович 05.10.2010'
    #index = patient_list.index(str)
    #print(index)
    #filtered = filter(lambda element: element == str, patient_list)
    #print(patient_list)

    cv.imshow('result', image_without_lines)

    cv.waitKey()



    
'''
