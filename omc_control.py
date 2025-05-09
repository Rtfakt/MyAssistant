from mouse import initialMousePosition
from monitor_capture import MonitorCapture

import numpy as np
import cv2 as cv
import time

from udp_client import sock, UDP_IP, UDP_PORT

infoclinika_screen = MonitorCapture('monitor')

def getScreenTemplate():
    screenshot = infoclinika_screen.get_screenshot()
    crop_image = screenshot[260:350, 78:930]
    cv.imwrite('example_images/ScreenTemplate.png', crop_image)

templateScreen = cv.imread('example_images/ScreenTemplate.png', 0)


def findChanges(template, debug_mode=False):
    while True:
        screenshot = infoclinika_screen.get_screenshot()  # получение кадров с камеры
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # делаем изображение серым
        result = cv.matchTemplate(screenshot, template, cv.TM_CCOEFF_NORMED)  # сравниваем шаблоны
        cv.minMaxLoc(screenshot)

        button_h = template.shape[0]
        button_w = template.shape[1]

        # print('левая верхняя точка %s' % str(max_loc))
        # print('пороговое значение %s' % str(max_val))

        threshold = 0.90
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print(locations)

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), button_w, button_h]
            rectangles.append(rect)
            # print(rect)

        # print(rectangles)

        points = []
        if len(rectangles):

            marker_type = cv.MARKER_CROSS

            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:
                # Determine the center position
                center_x = x + int(w / 2)
                center_y = y + int(h / 2)
                # Save the points
                points.append((center_x, center_y))
                cv.drawMarker(screenshot, (center_x, center_y), marker_type)
                # print('точка х %s' % str(center_x))
                # print('точка y %s' % str(center_y))
                initialMousePosition()
                sock.sendto(
                    '34564000{:05d}{:05d}'.format(center_x if center_x >= 0 else 65536 + center_x,
                                                  center_y if center_y >= 0 else 65536 + center_y).encode(),
                    (UDP_IP, UDP_PORT))
                time.sleep(0.1)

                print(points)

            break
        else:
            pass
        if debug_mode is True:
            cv.imshow('Read screen', screenshot)

        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break

    return points


def waitChanges(template, debug_mode=False):
    while True:
        screenshot = infoclinika_screen.get_screenshot()  # получение кадров с камеры
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # делаем изображение серым
        result = cv.matchTemplate(screenshot, template, cv.TM_CCOEFF_NORMED)  # сравниваем шаблоны
        cv.minMaxLoc(screenshot)

        button_h = template.shape[0]
        button_w = template.shape[1]

        # print('левая верхняя точка %s' % str(max_loc))
        # print('пороговое значение %s' % str(max_val))

        threshold = 0.90
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print(locations)

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), button_w, button_h]
            rectangles.append(rect)
            # print(rect)

        # print(rectangles)

        points = []
        if len(rectangles):

            marker_type = cv.MARKER_CROSS

            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:
                # Determine the center position
                center_x = x + int(w / 2)
                center_y = y + int(h / 2)
                # Save the points
                points.append((center_x, center_y))
                cv.drawMarker(screenshot, (center_x, center_y), marker_type)
                print('Поиск изменений данных')

            pass
        else:
            break
        if debug_mode is True:
            cv.imshow('Read screen', template)

        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break

    return points

    cv.waitKey()
