import cv2 as cv
from imutils import contours
import numpy as np
import time
from udp_client import sock, UDP_IP, UDP_PORT


#def readScreen():
 #   capture = cv2.VideoCapture(0)
  #  capture.set(4, 1080)  # Id высоты 4
   # capture.set(3, 1900)  # Id ширины 3

    #while True:
     #   ret, img = capture.read()
      #  cv2.imshow("Screen camera", img)
       # k = cv2.waitKey(1) & 0xFF
        #if k == 27:
         #   break

    #capture.release()
    #cv2.destroyWindow()




def startReadScreen():

        cap = cv.VideoCapture(0)
        cap.set(4, 1080)  # Id высоты 4
        cap.set(3, 1900)  # Id ширины 3

template = cv.imread('images/rentgenoButton.png', 0)


while (True):
        ret, frame = cap.read()     #получение кадров с камеры
        grey_screen = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)   # делаем изображение серым
        result = cv.matchTemplate(grey_screen, template, cv.TM_CCOEFF_NORMED) # сравниваем шаблоны
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        button_h = template.shape[0]
        button_w = template.shape[1]
        line_type = cv.LINE_4

        #print('левая верхняя точка %s' % str(max_loc))
        #print('пороговое значение %s' % str(max_val))

        threshold = 0.90
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print(locations)

        rectangles = []
        for loc in locations:
                rect = [int(loc[0]), int(loc[1]), button_w, button_h]
                rectangles.append(rect)
                #print(rect)

        if len(rectangles):
                #print('кнопка найдена')

                line_color = (0, 255, 0)
                line_type = cv.LINE_4
                marker_type = cv.MARKER_TILTED_CROSS

                for (x, y, w, h) in rectangles:
                        # top_left = (x, y)
                        # bottom_right = (x + w, y + h)
                        # cv.rectangle(initialScreen, top_left, bottom_right, line_color, line_type)

                        center_x = x + int(w / 2)
                        center_y = y + int(h / 2)
                        cv.drawMarker(grey_screen, (center_x, center_y), marker_type)
                        print('точка х %s' % str(center_x))
                        print('точка y %s' % str(center_y))
                        break
                sock.sendto(
                '34564000{:05d}{:05d}'.format(center_x if center_x >= 0 else 65536 + center_x, center_y if center_y >= 0 else 65536 + center_y).encode(),
                        (UDP_IP, UDP_PORT))
                time.sleep(0.1)

                cv.imshow('result', grey_screen)




        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break

