import pytesseract
import cv2
from imutils import contours


#capture = cv2.VideoCapture(0)

#while True:
#    ret, img = capture.read()
#    cv2.imshow("Text camera", img)
#    k = cv2.waitKey(30) & 0xFF
#    if k == 27:
#        break


#capture.release()
#cv2.destroyWindow()
def readText():
 image = cv2.imread("images/4.jpg")
 image = cv2.resize(image, None, fx=0.5, fy=0.5)
 height, width, _ = image.shape
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 thresh = cv2.threshold(gray, 0, 225, cv2.THRESH_OTSU)[1]


 pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
 result = pytesseract.image_to_string(image, lang="rus")
 print(result)
 cv2.imshow("Test", thresh)
 cv2.waitKey()


