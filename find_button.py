import numpy as np
import cv2 as cv
import time
from get_screenshot import get_screenshot
from udp_client import sock, UDP_IP, UDP_PORT
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap


class FindButton:
    # шаблоны кнопок
    playButton = cv.imread('images/buttons/playButton.png', 0)
    diagnozButton = cv.imread('images/buttons/diagnozButton.png', 0)
    noviyButton = cv.imread('images/buttons/noviyButton.png', 0)
    z018Button = cv.imread('images/buttons/z01.8Button.png', 0)
    F8Button = cv.imread('images/buttons/F8Button.png', 0)
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
    plusButton = cv.imread('images/create_refferal/PlusButton.png', 0)
    plusIns = cv.imread('images/create_refferal/plusIns.png', 0)
    rentgenButton = cv.imread('images/create_refferal/rentgenButton.png', 0)
    threePointsButton = cv.imread('images/create_refferal/ThreePointsButton.png', 0)
    usluga = cv.imread('images/create_refferal/Usluga.png', 0)
    vnutrennee = cv.imread('images/create_refferal/vnutreneeButton.png', 0)
    kodUslugi = cv.imread('images/create_refferal/kodUslugi.png', 0)
    backboneShablon = cv.imread('images/buttons/backboneShablon.png', 0)
    shopShablon = cv.imread('images/buttons/shopShablon.png', 0)
    gopShablon = cv.imread('images/buttons/gopShablon.png', 0)
    popShablon = cv.imread('images/buttons/popShablon.png', 0)
    ppnShablon = cv.imread('images/buttons/ppnShablon.png', 0)
    sinusitLeftShablon = cv.imread('images/buttons/sinusitLeftShablon.png', 0)
    sinusitRightShablon = cv.imread('images/buttons/sinusitRightShablon.png', 0)
    ppnNormaShablon = cv.imread('images/buttons/ppnNormaShablon.png', 0)
    mainShablonOGK = cv.imread('images/buttons/mainShablonOGK.png', 0)
    shopGopShablon = cv.imread('images/buttons/shopGopShablon.png', 0)
    okButton = cv.imread('images/buttons/OKButton.png', 0)
    endWork = cv.imread('images/buttons/zavershenieRaboty.png', 0)
    startButton = cv.imread('images/buttons/startButton.png', 0)
    userButton = cv.imread('images/buttons/userButton.png', 0)
    windowsExit = cv.imread('images/buttons/windowsExit.png', 0)
    engLanguage = cv.imread('images/buttons/ENGLanguage.png', 0)
    offButton = cv.imread('images/buttons/offButton.png', 0)
    NAmbulatKart = cv.imread('images/buttons/NAmbulatKart.png', 0)
    lechenieEnd = cv.imread('images/buttons/lechenieEnd.png', 0)
    osmotr = cv.imread('images/buttons/osmotr.png', 0)
    threePointsAndCloseButton = cv.imread('images/buttons/threePointsAndCloseButton.png', 0)
    noButton = cv.imread('images/buttons/NOButton.png', 0)
    doubleShablon = cv.imread('images/buttons/rentgenologycheskoeIssledovanieMainShablon.png', 0)




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
                    mouseTap(MP.LKM_MOUSE)


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
                    mouseTap(MP.LKM_MOUSE)

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

    def findPlusButton(template=plusButton, debug_mode = False):

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
                    center_x = x + int(w - 60)
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
                    mouseTap(MP.LKM_MOUSE)

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

