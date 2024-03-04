import numpy as np
import cv2 as cv
import time
from find_button import FindButton as FB
from get_screenshot import get_screenshot
from udp_client import sock, UDP_IP, UDP_PORT
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap

class FindRefferal():
    rentgenoButton = cv.imread('images/refferal_buttons/rentgenoRefferalButton.png', 0)
    rentgenoBlueButton = cv.imread('images/refferal_buttons/rentgenoRefferalBlueButton.png', 0)
    fluraButton = cv.imread('images/refferal_buttons/fluraRefferalButton.png', 0)
    fluraBlueButton = cv.imread('images/refferal_buttons/fluraRefferalBlueButton.png', 0)
    OGKButton = cv.imread('images/refferal_buttons/OGKRefferalButton.png', 0)
    OGKBlueButton = cv.imread('images/refferal_buttons/OGKBlueRefferalButton.png', 0)
    PPNButton = cv.imread('images/refferal_buttons/PPNRefferalButton.png', 0)
    PPNBlueButton = cv.imread('images/refferal_buttons/PPNRefferalBlueButton.png', 0)
    OBPButton = cv.imread('images/refferal_buttons/OBPRefferalButton.png', 0)
    OBPBlueButton = cv.imread('images/refferal_buttons/OBPRefferalBlueButton.png', 0)
    UrografiaButton = cv.imread('images/refferal_buttons/UrografiaRefferalButton.png', 0)
    UrografiaBlueButton = cv.imread('images/refferal_buttons/UrografiaRefferalBlueButton.png', 0)

    def findRefferalButton(templateBlue, template, debug_mode=False):
        stop = time.time() + 2
        while time.time() < stop:
            screenshot = get_screenshot()  # получение кадров с камеры
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # делаем изображение серым
            result = cv.matchTemplate(screenshot, templateBlue, cv.TM_CCOEFF_NORMED)  # сравниваем шаблоны
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(screenshot)

            button_h = templateBlue.shape[0]
            button_w = templateBlue.shape[1]

            # print('левая верхняя точка %s' % str(max_loc))
            # print('пороговое значение %s' % str(max_val))

            threshold = 0.95
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
                    # print(points)
                    # выбираем нужную кнопку

                    center_x = points[0][0]
                    center_y = points[0][1]

                    print('точка х %s' % str(center_x))
                    print('точка y %s' % str(center_y))
                    initialMousePosition()
                    sock.sendto(
                        '34564000{:05d}{:05d}'.format(center_x if center_x >= 0 else 65536 + center_x,
                                                      center_y if center_y >= 0 else 65536 + center_y).encode(),
                        (UDP_IP, UDP_PORT))
                    time.sleep(0.1)
                    mouseTap(MP.LKM_MOUSE)
                    time.sleep(0.1)
                    FB.find(FB.playButton) #нажимаем зеленую кнопку play
                    mouseTap(MP.LKM_MOUSE)
                break
            else:
                screenshot = get_screenshot()  # получение кадров с камеры
                screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # делаем изображение серым
                result = cv.matchTemplate(screenshot, template, cv.TM_CCOEFF_NORMED)  # сравниваем шаблоны
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(screenshot)

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
                if len(rectangles) > 0:

                    marker_type = cv.MARKER_CROSS

                    # Loop over all the rectangles
                    for (x, y, w, h) in rectangles:
                        # Determine the center position
                        center_x = x + int(w / 2)
                        center_y = y + int(h / 2)
                        # Save the points
                        points.append((center_x, center_y))
                        cv.drawMarker(screenshot, (center_x, center_y), marker_type)
                        # print(points)
                        # выбираем нужную кнопку

                        center_x = points[0][0]
                        center_y = points[0][1]

                        print('точка х %s' % str(center_x))
                        print('точка y %s' % str(center_y))
                        initialMousePosition()
                        time.sleep(0.1)
                        sock.sendto(
                            '34564000{:05d}{:05d}'.format(center_x if center_x >= 0 else 65536 + center_x,
                                                          center_y if center_y >= 0 else 65536 + center_y).encode(),
                            (UDP_IP, UDP_PORT))
                        time.sleep(0.1)
                        mouseTap(MP.LKM_MOUSE)
                        time.sleep(0.1)
                        FB.find(FB.playButton)#нажимаем зеленую кнопку play
                        time.sleep(0.1)
                        mouseTap(MP.LKM_MOUSE)
                    break
            if debug_mode is True:
                cv.imshow('Read screen', screenshot)

            if cv.waitKey(1) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                break

            return points




'''
class FindRefferal():
    rentgenoButton = cv.imread('images/refferal_buttons/rentgenoRefferalButton.png', 0)
    rentgenoBlueButton = cv.imread('images/refferal_buttons/rentgenoRefferalBlueButton.png', 0)
    fluraButton = cv.imread('images/refferal_buttons/fluraRefferalButton.png', 0)
    fluraBlueButton = cv.imread('images/refferal_buttons/fluraRefferalBlueButton.png', 0)
    OGKButton = cv.imread('images/refferal_buttons/OGKRefferalButton.png', 0)
    OGKBlueButton = cv.imread('images/refferal_buttons/OGKBlueRefferalButton.png', 0)
    PPNButton = cv.imread('images/refferal_buttons/PPNRefferalButton.png', 0)
    PPNBlueButton = cv.imread('images/refferal_buttons/PPNRefferalBlueButton.png', 0)


    def findRefferalButton(templateBlue, template, debug_mode=False):
        stop = time.time() + 3
        while time.time() < stop:
            screenshot = get_screenshot()  # получение кадров с камеры
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # делаем изображение серым
            result = cv.matchTemplate(screenshot, templateBlue, cv.TM_CCOEFF_NORMED)  # сравниваем шаблоны
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(screenshot)

            button_h = templateBlue.shape[0]
            button_w = templateBlue.shape[1]

            # print('левая верхняя точка %s' % str(max_loc))
            # print('пороговое значение %s' % str(max_val))

            threshold = 0.98
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
                    # print(points)
                    # выбираем нужную кнопку

                    center_x = points[0][0]
                    center_y = points[0][1]

                    print('точка х %s' % str(center_x))
                    print('точка y %s' % str(center_y))
                    initialMousePosition()
                    sock.sendto(
                        '34564000{:05d}{:05d}'.format(center_x if center_x >= 0 else 65536 + center_x,
                                                      center_y if center_y >= 0 else 65536 + center_y).encode(),
                        (UDP_IP, UDP_PORT))
                    time.sleep(0.1)
                    mouseTap(MP.LKM_MOUSE)
                break
            else:
                screenshot = get_screenshot()  # получение кадров с камеры
                screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # делаем изображение серым
                result = cv.matchTemplate(screenshot, template, cv.TM_CCOEFF_NORMED)  # сравниваем шаблоны
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(screenshot)

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
                if len(rectangles) > 0:

                    marker_type = cv.MARKER_CROSS

                    # Loop over all the rectangles
                    for (x, y, w, h) in rectangles:
                        # Determine the center position
                        center_x = x + int(w / 2)
                        center_y = y + int(h / 2)
                        # Save the points
                        points.append((center_x, center_y))
                        cv.drawMarker(screenshot, (center_x, center_y), marker_type)
                        # print(points)
                        # выбираем нужную кнопку

                        center_x = points[0][0]
                        center_y = points[0][1]

                        print('точка х %s' % str(center_x))
                        print('точка y %s' % str(center_y))
                        initialMousePosition()
                        time.sleep(0.1)
                        sock.sendto(
                            '34564000{:05d}{:05d}'.format(center_x if center_x >= 0 else 65536 + center_x,
                                                          center_y if center_y >= 0 else 65536 + center_y).encode(),
                            (UDP_IP, UDP_PORT))
                        time.sleep(0.1)
                        mouseTap(MP.LKM_MOUSE)
                    break
            if debug_mode is True:
                cv.imshow('Read screen', screenshot)

            if cv.waitKey(1) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                break

        return points
'''