import time
from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, mouseDoubleLKMTap, initialMousePosition
from main import Ui_Form

ui = Ui_Form


def tet():
    print('1')
    print(ui.argument)


# тазобедренный сустав
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
    # подписать
    mousePosition(-60, -35)

    time.sleep(1)


# коленные суставы
def kneesJoints():
    # Начало
    initialMousePosition()
    # История болезни
    mousePosition(315, 40)
    mouseTap(MP.LKM_MOUSE)
    # Флюрография(униф.)
    mousePosition(0, 330)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(5)
    # шаблоны
    mousePosition(640, -324)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    mousePosition(5, 34)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # ДОА коленных суставов
    mousePosition(-605, 210)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    mousePosition(130, -220)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # Область исследования
    mousePosition(0, 120)
    mouseTap(MP.LKM_MOUSE)
    # правого и левого********************************************
    initialMousePosition()
    mousePosition(1500, 200)
    mouseDoubleLKMTap()
    time.sleep(1)
    # Заключение
    mousePosition(-500, 500)
    mouseTap(MP.LKM_MOUSE)
    # выбор стороны в заключении***********************************
    mousePosition(500, -420)
    mouseDoubleLKMTap()
    # Заключение2
    mousePosition(-500, 420)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # выставление степени****************************************
    keyboardTap(KP.NUM3)
    keyboardTap(KP.KEYBOARD_MINUS)
    keyboardTap(KP.NUM4)
    # подписать
    mousePosition(-560, -660)
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
    time.sleep(10)
    mousePosition(1470, 5)
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
