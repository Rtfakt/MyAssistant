import time

from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition


# (без печати)РЕНТГЕНОГРАФИЯ ОРГАНОВ ГРУДНОЙ КЛЕТКИ
def rOGK():
    # Начало
    initialMousePosition()
    #История болезни
    mousePosition(315, 40)
    mouseTap(MP.LKM_MOUSE)
    #Рентгенография органов грудной клетки
    mousePosition(0, 200)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(5)
    #шаблоны
    mousePosition(640, -194)
    mouseTap(MP.LKM_MOUSE)
    #Выбрать
    mousePosition(5, 34)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    #ОГК норма
    mousePosition(-605, 250)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    #Выбор с добавлением
    mousePosition(130, -260)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    #подписать
    mousePosition(-60, -35)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    #подписать ENTER
    keyboardTap(KP.ENTER)
    time.sleep(1)
    #выход
    mousePosition(1440, 5)
    time.sleep(8)
    mouseTap(MP.LKM_MOUSE)
    #cчитать прием диспансерным?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    #сохранить F2
    keyboardTap(KP.F2)
    # сохранить изменения?
    keyboardTap(KP.ENTER)
    # выбрать
    keyboardTap(KP.F2)
    # выбрать
    keyboardTap(KP.F2)
    # нет диагноза в приеме
    keyboardTap(KP.ENTER)


def rOGKPrint():
    # Начало
    initialMousePosition()
    #История болезни
    mousePosition(315, 40)
    mouseTap(MP.LKM_MOUSE)
    #Рентгенография органов грудной клетки
    mousePosition(0, 200)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(5)
    #шаблоны
    mousePosition(640, -194)
    mouseTap(MP.LKM_MOUSE)
    #Выбрать
    mousePosition(5, 34)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    #ОГК норма
    mousePosition(-605, 250)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    #Выбор с добавлением
    mousePosition(130, -260)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    #подписать
    mousePosition(-60, -35)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # печать
    keyboardTap(KP.F5)
    # ОК
    keyboardTap(KP.ENTER)
    time.sleep(1)
    #подписать ENTER
    keyboardTap(KP.ENTER)
    time.sleep(1)
    #выход
    mousePosition(1500, 5)
    time.sleep(8)
    mouseTap(MP.LKM_MOUSE)
    #cчитать прием диспансерным?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    #сохранить F2
    keyboardTap(KP.F2)
    # сохранить изменения?
    keyboardTap(KP.ENTER)
    # выбрать
    keyboardTap(KP.F2)
    # выбрать
    keyboardTap(KP.F2)
    # нет диагноза в приеме
    keyboardTap(KP.ENTER)
