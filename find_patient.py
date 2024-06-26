import cv2
import numpy as np
import pytesseract
from imutils import contours


# firstPosition(78, 280)
# secondPosition(300, 930)
def findPatient():
    image = cv2.imread('example_images/screenFail.png')
    mask = np.zeros(image.shape, dtype=np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    (cnts, _) = contours.sort_contours(cnts, method="left-to-right")
    ROI_number = 0
    for c in cnts:
        area = cv2.contourArea(c)
        if area < 800 and area > 200:
            x, y, w, h = cv2.boundingRect(c)
            ROI = 255 - thresh[y:y + h, x:x + w]
            cv2.drawContours(mask, [c], -1, (255, 255, 255), -1)
            cv2.imwrite('ROI_{}.png'.format(ROI_number), ROI)
            ROI_number += 1

    cv2.imshow('mask', mask)
    cv2.imshow('thresh', thresh)
    cv2.waitKey()

'''
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
    str = '05.10.2010'
    #index = patient_list.index(str)
    #print(index)


    cv.imshow('result', image_without_lines)

    cv.waitKey()


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
