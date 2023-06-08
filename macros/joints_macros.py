import time

from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, mouseDoubleLKMTap

#тазобедренный сустав
def hipJoint():
    # Начало
    mouseTap(MP.INITIAL_MOUSE_POSITION)
    #История болезни
    mousePosition(250, 40)
    mouseTap(MP.LKM_MOUSE)
    #Рентгенография суставов
    mousePosition(0, 240)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(5)
    #шаблоны
    mousePosition(725, -240)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    mousePosition(5, 34)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    #ДОА тазобедренного сустава
    mousePosition(-605, 335)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    mousePosition(130, -340)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    #Область исследования
    mousePosition(0, 100)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)



    #правого и левого
    mousePosition(1030,300)
    mouseDoubleLKMTap()
    time.sleep(1)


    #Заключение
    mousePosition(-500, 250)
    mouseTap(MP.LKM_MOUSE)
    #выбор стороны в заключении
    mousePosition(500, -220)
    mouseDoubleLKMTap()
    #Заключение2
    mousePosition(-500, 220)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)


    #выставление степени
    keyboardTap(KP.NUM2)
    keyboardTap(KP.KEYBOARD_MINUS)
    keyboardTap(KP.NUM3)

    # подписать
    mousePosition(-600, -670)
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
    mousePosition(1460, 5)
    time.sleep(8)
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
def kneesJoint():
    # Начало
    mouseTap(MP.INITIAL_MOUSE_POSITION)
    # История болезни
    mousePosition(250, 40)


