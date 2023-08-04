import time

from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB


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
    mousePosition(1470, 5)
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
    #печать
    keyboardTap(KP.F5)
    #OK
    keyboardTap(KP.ENTER)
    #подписать ENTER
    keyboardTap(KP.ENTER)
    time.sleep(1)
    #выход
    mousePosition(1470, 5)
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




def fluraStart():
    #зеленая кнопка play
    FB.find(FB.playButton)
    mouseTap(MP.LKM_MOUSE)
    #Дата
    keyboardTap(KP.ENTER)
    #Подтвердить случай?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # ?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    #диагноз
    FB.find(FB.diagnozButton)
    mouseTap(MP.LKM_MOUSE)
    #новый
    FB.find(FB.noviyButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    #Поиск по коду
    keyboardTap(KP.Z)
    keyboardTap(KP.NUM0)
    keyboardTap(KP.NUM1)
    keyboardTap(KP.Ю)
    keyboardTap(KP.NUM8)
    #стрелка влево
    keyboardTap(KP.ENTER)
    #
    #Добавлять диагноз?
    keyboardTap(KP.ENTER)
    ##
    #диагноз уже добавлен
    keyboardTap(KP.ENTER)
    keyboardTap(KP.ENTER)
    keyboardTap(KP.ENTER)
    #сохранить
    keyboardTap(KP.F2)
    time.sleep(1)
    #считать прием диспансерным?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # История болезни
    initialMousePosition()
    mousePosition(315, 40)
    mouseTap(MP.LKM_MOUSE)
    # Флюорографическое исследование органов грудной клетки
    mousePosition(0, 310)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(4)
    #шаблоны
    mousePosition(520, -300)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    #Выбрать
    mousePosition(5, 30)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    mousePosition(-330, -20)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # В протоколе уже есть основной диагноз
    keyboardTap(KP.ENTER)
    # Дата проведения исследования
    initialMousePosition()
    mousePosition(1402, 105)
    mouseTap(MP.LKM_MOUSE)
    # Сегодня
    mousePosition(-1100, 210)
    mouseTap(MP.LKM_MOUSE)
    #время проведения исследования
    keyboardTap(KP.TAB)
    keyboardTap(KP.NUM1)
    # смена языка
    initialMousePosition()
    mousePosition(1780, 1060)
    mouseTap(MP.LKM_MOUSE)
    mousePosition(0, -120)
    mouseDoubleLKMTap()
    #Диагноз МКБ
    initialMousePosition()
    mousePosition(300, 160)
    mouseTap(MP.LKM_MOUSE)
    keyboardTap(KP.Z)
    keyboardTap(KP.NUM0)
    keyboardTap(KP.NUM1)
    keyboardTap(KP.Ю)
    keyboardTap(KP.NUM8)
    #Подписать
    mousePosition(0, -120)
    mouseTap(MP.LKM_MOUSE)
    #Подписать
    keyboardTap(KP.ENTER)
    #выход
    time.sleep(14)
    mousePosition(1570, 5)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(2)
    # кнопка z01.8
    FB.find(FB.z018)
    mouseTap(MP.LKM_MOUSE)
    # кнопка z01.8
    FB.find(FB.z018)
    mouseTap(MP.LKM_MOUSE)
    # закрыть
    mousePosition(0, 85)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # результат
    mousePosition(1053, -103)
    mouseTap(MP.LKM_MOUSE)
    # лечение завершено
    mousePosition(0, 35)
    mouseTap(MP.LKM_MOUSE)
    # Исход заболевания
    mousePosition(0, -10)
    mouseTap(MP.LKM_MOUSE)
    # осмотр
    mousePosition(-20, 130)
    mouseTap(MP.LKM_MOUSE)
    # Закрыть с текущим диагнозом
    mousePosition(0, -90)
    mouseTap(MP.LKM_MOUSE)
    # Сформировать эпикриз автоматически?
    keyboardTap(KP.ENTER)
    time.sleep(8)
    # Подписать
    keyboardTap(KP.ENTER)
    time.sleep(10)
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





def fluraEnd():
    # кнопка z01.8
    FB.find(FB.z018)
    mouseTap(MP.LKM_MOUSE)
    # закрыть
    mousePosition(0, 85)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # результат
    mousePosition(1053, -103)
    mouseTap(MP.LKM_MOUSE)
    # лечение завершено
    mousePosition(0, 35)
    mouseTap(MP.LKM_MOUSE)
    # Исход заболевания
    mousePosition(0, -10)
    mouseTap(MP.LKM_MOUSE)
    # осмотр
    mousePosition(-20, 130)
    mouseTap(MP.LKM_MOUSE)
    # Закрыть с текущим диагнозом
    mousePosition(0, -90)
    mouseTap(MP.LKM_MOUSE)
    # Сформировать эпикриз автоматически?
    keyboardTap(KP.ENTER)
    time.sleep(8)
    # Подписать
    keyboardTap(KP.ENTER)
    time.sleep(10)
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











