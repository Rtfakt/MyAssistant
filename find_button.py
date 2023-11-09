import numpy as np
import cv2 as cv
import time
from mouse import initialMousePosition
from get_screenshot import get_screenshot
from udp_client import sock, UDP_IP, UDP_PORT


class FindButton:
    # шаблоны кнопок
    playButton = cv.imread('images/buttons/playButton.png', 0)
    diagnozButton = cv.imread('images/buttons/diagnozButton.png', 0)
    noviyButton = cv.imread('images/buttons/noviyButton.png', 0)
    z018Button = cv.imread('images/buttons/z01.8Button.png', 0)
    F8Button = cv.imread('images/buttons/F8Button.png', 0)
    rentgenoButton = cv.imread('images/buttons/rentgenoButton.png', 0)
    rentgenoButtonBlue = cv.imread('images/buttons/rentgenoButtonBlue.png', 0)
    prodBezSozSlu = cv.imread('images/buttons/prodBezSozSluButton.png', 0)
    resultButton = cv.imread('images/buttons/resultButton.png', 0)
    prodSohrPriButton = cv.imread('images/buttons/prodSohrPriButton.png', 0)
    exitButton = cv.imread('images/buttons/exitButton.png', 0)
    shablonButton = cv.imread('images/buttons/shablonButton.png', 0)
    signatureButton = cv.imread('images/buttons/signatureButton.png', 0)
    scoliozPOPButton = cv.imread('images/buttons/scoliozPOPButton.png', 0)
    scoliozButton = cv.imread('images/buttons/scoliozButton.png', 0)
    cardRegistrButton = cv.imread('images/buttons/cardRegistrButton.png', 0)
    OMCButton = cv.imread('images/windows/OMC.png', 0)
    dataPrikrep = cv.imread('images/buttons/dataPrikrepButton.png', 0)
    vyborSDobavleniem = cv.imread('images/buttons/vyborSdobavleniem.png', 0)
    mainShablonFlura = cv.imread('images/buttons/mainShablonFlura.png', 0)
    vybratButton = cv.imread('images/buttons/vybratButton.png', 0)
    firstInfoclinicaButton = cv.imread('images/buttons/firstInfoclinikaButton.png', 0)
    secondInfoclinicaButton = cv.imread('images/buttons/infoclinicaButton.png', 0)
    cartotekaButton = cv.imread('images/buttons/cartotekaButton.png', 0)
    closeZ018Button = cv.imread('images/buttons/closeZ01.8Button.png', 0)
    exitFromInfoclinikaButton = cv.imread('images/buttons/exitFromInfoclinikaButton.png', 0)
    OGKNormaButton = cv.imread('images/buttons/OGKNorma.png', 0)
    todayButton = cv.imread('images/buttons/todayButton.png', 0)
    pycButton = cv.imread('images/buttons/pycButton.png', 0)

    def find(template, debug_mode=False):
        while True:
            screenshot = get_screenshot()  # получение кадров с камеры
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

    def findF8(template=F8Button, debug_mode=False):
        while True:
            screenshot = get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
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
            if len(rectangles):

                marker_type = cv.MARKER_CROSS

                # Loop over all the rectangles
                for (x, y, w, h) in rectangles:
                    # Determine the center position
                    center_x = x + int(w - 7)
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

    def findRentgenoButton(template=rentgenoButtonBlue, debug_mode=False, template2=rentgenoButton):

        stop = time.time() + 2
        while time.time() < stop:
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
                break
            else:
                screenshot = get_screenshot()  # получение кадров с камеры
                screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # делаем изображение серым
                result = cv.matchTemplate(screenshot, template2, cv.TM_CCOEFF_NORMED)  # сравниваем шаблоны
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
                        sock.sendto(
                            '34564000{:05d}{:05d}'.format(center_x if center_x >= 0 else 65536 + center_x,
                                                          center_y if center_y >= 0 else 65536 + center_y).encode(),
                            (UDP_IP, UDP_PORT))
                        time.sleep(0.1)
                    break
            if debug_mode is True:
                cv.imshow('Read screen', screenshot)

            if cv.waitKey(1) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                break

        return points

    def findWithTime(template, timeWait=1, debug_mode=False):
        stop = time.time() + timeWait
        while time.time() < stop:
            screenshot = get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
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

    def findResult(template=resultButton, debug_mode=False):
        while True:
            screenshot = get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
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
            if len(rectangles):

                marker_type = cv.MARKER_CROSS

                # Loop over all the rectangles
                for (x, y, w, h) in rectangles:
                    # Determine the center position
                    center_x = x + int(w - 12)
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
