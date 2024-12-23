import numpy as np
import cv2 as cv
import time

from find_button import FindButton as FB
from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import initialMousePosition
from monitor_capture import MonitorCapture
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from write_text import writeText, writeOMC
from windows_control import WindowsControl as WC

infoclinika_screen = MonitorCapture('monitor')
class FindErrors:
    errorOMC = cv.imread('images/errors/errorOMC.png', 0)
    errorUIP = cv.imread('images/errors/errorDataUIP.png', 0)

    def findOMCError(template=errorOMC, timeWait=1, debug_mode=False):
        stop = time.time() + timeWait
        while time.time() < stop:
            screenshot = infoclinika_screen.get_screenshot()
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
                    print('Найдена ошибка: отсутствует начало действия ОМС')
                    keyboardTap(KP.ENTER)
                    # Подтвердить?
                    keyboardTap(KP.ENTER)
                    # Карточка регистрации
                    FB.find(FB.cardRegistrButton)
                    time.sleep(1)
                    mouseTap(MP.LKM_MOUSE)
                    # поиск полиса ОМС
                    FB.find(FB.OMCButton)
                    mouseDoubleLKMTap()
                    # Дата прикрепления
                    FB.find(FB.dataPrikrep)
                    mouseTap(MP.LKM_MOUSE)
                    writeText('14.11.14')
                    # сохранить
                    keyboardTap(KP.F2)
                    time.sleep(1)
                    keyboardTap(KP.F2)
                    # Диагноз МКБ
                    initialMousePosition()
                    mousePosition(300, 160)
                    mouseTap(MP.LKM_MOUSE)
                    keyboardTap(KP.Z)
                    keyboardTap(KP.NUM0)
                    keyboardTap(KP.NUM1)
                    keyboardTap(KP.Ю)
                    keyboardTap(KP.NUM8)
                    # подписать
                    FB.find(FB.signatureButton)
                    mouseTap(MP.LKM_MOUSE)
                    time.sleep(1)
                    # печать
                    keyboardTap(KP.F5)
                    # OK
                    keyboardTap(KP.ENTER)
                    # подписать ENTER
                    keyboardTap(KP.ENTER)
                    time.sleep(1)
                    # выход
                    WC.find(WC.elPodProtocWindow)
                    WC.wait(WC.elPodProtocWindow)
                    FB.find(FB.exitButton)
                    mouseTap(MP.LKM_MOUSE)
                    time.sleep(1)
                    # cчитать прием диспансерным?
                    keyboardTap(KP.RightArrow)
                    keyboardTap(KP.ENTER)
                    # сохранить F2
                    keyboardTap(KP.F2)
                    # сохранить изменения?
                    keyboardTap(KP.ENTER)
                    # выбрать
                    keyboardTap(KP.F2)
                    # выбрать
                    keyboardTap(KP.F2)
                    # нет диагноза в приеме
                    keyboardTap(KP.ENTER)

                break
            else:
                pass
            if debug_mode is True:
                cv.imshow('Read screen', screenshot)

            if cv.waitKey(1) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                break

        return points

    def findDataUIPError(template=errorUIP, timeWait=1, debug_mode=False):
        stop = time.time() + timeWait
        while time.time() < stop:
            infoclinika_screen.get_screenshot()
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
                    print('Найдена ошибка: Не найдена дата выдачи документа УИП')
                    keyboardTap(KP.ENTER)
                    # Подтвердить?
                    keyboardTap(KP.ENTER)
                    # Карточка регистрации
                    FB.find(FB.cardRegistrButton)
                    time.sleep(1)
                    mouseTap(MP.LKM_MOUSE)
                    # поиск полиса ОМС
                    FB.find(FB.OMCButton)
                    mouseDoubleLKMTap()
                    # Дата прикрепления
                    FB.find(FB.dataPrikrep)
                    mouseTap(MP.LKM_MOUSE)
                    writeText('14.11.14')
                    # сохранить
                    keyboardTap(KP.F2)
                    time.sleep(1)
                    keyboardTap(KP.F2)
                    # Диагноз МКБ
                    initialMousePosition()
                    mousePosition(300, 160)
                    mouseTap(MP.LKM_MOUSE)
                    keyboardTap(KP.Z)
                    keyboardTap(KP.NUM0)
                    keyboardTap(KP.NUM1)
                    keyboardTap(KP.Ю)
                    keyboardTap(KP.NUM8)
                    # подписать
                    FB.find(FB.signatureButton)
                    mouseTap(MP.LKM_MOUSE)
                    time.sleep(1)
                    # печать
                    keyboardTap(KP.F5)
                    # OK
                    keyboardTap(KP.ENTER)
                    # подписать ENTER
                    keyboardTap(KP.ENTER)
                    time.sleep(1)
                    # выход
                    WC.find(WC.elPodProtocWindow)
                    WC.wait(WC.elPodProtocWindow)
                    FB.find(FB.exitButton)
                    mouseTap(MP.LKM_MOUSE)
                    time.sleep(1)
                    # cчитать прием диспансерным?
                    keyboardTap(KP.RightArrow)
                    keyboardTap(KP.ENTER)
                    # сохранить F2
                    keyboardTap(KP.F2)
                    # сохранить изменения?
                    keyboardTap(KP.ENTER)
                    # выбрать
                    keyboardTap(KP.F2)
                    # выбрать
                    keyboardTap(KP.F2)
                    # нет диагноза в приеме
                    keyboardTap(KP.ENTER)
                break
            else:
                pass
            if debug_mode is True:
                cv.imshow('Read screen', screenshot)

            if cv.waitKey(1) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                break

        return points
