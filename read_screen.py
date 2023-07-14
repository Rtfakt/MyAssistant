import cv2 as cv
from imutils import contours
import numpy as np
import time
from udp_client import sock, UDP_IP, UDP_PORT


cap = cv.VideoCapture(0)
cap.set(4, 1080)  # Id высоты 4
cap.set(3, 1900)  # Id ширины 3


def readScreen():
    while True:

        ret, frame = cap.read() #получение кадров с камеры

        # img = cv2.cvtColor(np.array(frame), cv2.COLOR_BGR2GRAY)
        # Save img data as matrix
        # img_matrix.append(img)

        cv.imshow("screenshot", cap.read()[1])  # показ скриншота экрана
        cv.imwrite('screenshot.png', cap.read()[1])  # сохранаем скриншот в файл
        # print(img_matrix)
        # print(len(img_matrix))

        if cv.waitKey(1) & 0xFF == ord('q'):   #выйти из камеры
            cv.destroyAllWindows()
            break






'''
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

        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        # print(rectangles)

        points = []
        if len(rectangles):
                # print('Found needle.')

                line_color = (0, 255, 0)
                line_type = cv.LINE_4
                marker_color = (255, 0, 255)
                marker_type = cv.MARKER_CROSS

                # Loop over all the rectangles
                for (x, y, w, h) in rectangles:
                        # Determine the center position
                        center_x = x + int(w / 2)
                        center_y = y + int(h / 2)
                        # Save the points
                        points.append((center_x, center_y))
                        cv.drawMarker(grey_screen, (center_x, center_y), marker_type)
                        print('точка х %s' % str(center_x))
                        print('точка y %s' % str(center_y))

                        points.append((center_x, center_y))
                        sock.sendto(
                        '34564000{:05d}{:05d}'.format(center_x if center_x >= 0 else 65536 + center_x, center_y if center_y >= 0 else 65536 + center_y).encode(),
                        (UDP_IP, UDP_PORT))
                        time.sleep(0.1)
                        pass

                cv.imshow('result', grey_screen)

        if cv.waitKey(1) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                break
'''



