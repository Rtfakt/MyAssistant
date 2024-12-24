from monitor_capture import MonitorCapture
import numpy as np
import cv2 as cv
import time
from udp_client import sock, UDP_IP, UDP_PORT
from mouse import mouseTap, Mouse as MP, initialMousePosition, mousePosition, mouseDoubleLKMTap
import operator



infoclinika_screen = MonitorCapture('monitor')
class FindObjects:
    F8Button = cv.imread('images/buttons/F8Button.png', 0)
    # для точного расположения курсора относительно прямоугольника найденного объекта
    addition = operator.add
    subtraction = operator.sub
    multiplication = operator.mul
    division = operator.truediv
    infoclinika_screen = MonitorCapture('monitor')


    def __init__(infoclinika_screen):
        self.infoclinika_screen = infoclinika_screen
    def find(template, operator_w=division, operator_h=division, w_value=2, h_value=2, debug_mode=False):

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

                for (x, y, w, h) in rectangles:
                    # Determine the center position
                    center_x = x + int(operator_w(w, w_value))
                    center_y = y + int(operator_h(h, h_value))
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
