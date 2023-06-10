import time

from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, mouseDoubleLKMTap, initialMousePosition






#тазобедренный сустав
def hipsJoints():



    # правого и левого
    initialMousePosition()
    mousePosition(1500, 200)
    mouseDoubleLKMTap()
    time.sleep(1)
    # Заключение
    mousePosition(-500, 500)
    mouseTap(MP.LKM_MOUSE)
    # выбор стороны в заключении
    mousePosition(500, -420)
    mouseDoubleLKMTap()



    # Заключение2
    mousePosition(-500, 420)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # выставление степени
    keyboardTap(KP.NUM1)
    # подписать
    mousePosition(-570, -660)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # печать
    keyboardTap(KP.F5)
    # ОК
    keyboardTap(KP.ENTER)
    time.sleep(1)
    # подписать ENTER
    keyboardTap(KP.ENTER)
    time.sleep(1)
    # выход
    time.sleep(10)
    mousePosition(1460, 5)
    mouseTap(MP.LKM_MOUSE)
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





 # коленные суставы
def kneesJoints():
    # Начало
    initialMousePosition()
    # История болезни
    mousePosition(315, 40)






























