import cv2

capture = cv2.VideoCapture(2)

while True:
    ret, img = capture.read()
    cv2.imshow("Text camera", img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break


capture.release()
cv2.destroyWindow()