import time

from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_errors import FindErrors as FE

# (без печати)РЕНТГЕНОГРАФИЯ ОРГАНОВ ГРУДНОЙ КЛЕТКИ
def rOGK():
    # Поиск кнопки Рентгено
    FB.findRentgenoButton()
    keyboardTap(MP.LKM_MOUSE)
    # зеленая кнопка play
    FB.find(FB.playButton)
    mouseTap(MP.LKM_MOUSE)
    # Дата
    keyboardTap(KP.ENTER)
    time.sleep(3)
    # Подтвердить случай?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # ?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # Продолжить без создания случая
    FB.findWithTime(FB.prodBezSozSlu)
    mouseTap(MP.LKM_MOUSE)
    # История болезни
    FB.findF8()
    mouseTap(MP.LKM_MOUSE)
    # Рентгенография органов грудной клетки
    mousePosition(0, 190)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    FB.find(FB.vybratButton)
    mouseTap(MP.LKM_MOUSE)
    # ОГК норма
    FB.find(FB.OGKNormaButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    FB.find(FB.vyborSDobavleniem)
    mouseTap(MP.LKM_MOUSE)
    # подписать
    FB.find(FB.signatureButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    #подписать ENTER
    keyboardTap(KP.ENTER)
    time.sleep(1)
    # выход
    WC.find(WC.elPodProtocWindow)
    WC.wait(WC.elPodProtocWindow)
    FB.find(FB.exitButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
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
    # Поиск кнопки Рентгено
    FB.findRentgenoButton()
    keyboardTap(MP.LKM_MOUSE)
    # зеленая кнопка play
    FB.find(FB.playButton)
    mouseTap(MP.LKM_MOUSE)
    # Дата
    keyboardTap(KP.ENTER)
    time.sleep(3)
    # Подтвердить случай?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # ?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # Продолжить без создания случая
    FB.findWithTime(FB.prodBezSozSlu)
    mouseTap(MP.LKM_MOUSE)
    #История болезни
    FB.findF8()
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    #Рентгенография органов грудной клетки
    mousePosition(0, 190)
    mouseTap(MP.LKM_MOUSE)
    # шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    FB.find(FB.vybratButton)
    mouseTap(MP.LKM_MOUSE)
    # ОГК норма
    FB.find(FB.OGKNormaButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    FB.find(FB.vyborSDobavleniem)
    mouseTap(MP.LKM_MOUSE)
    # подписать
    FB.find(FB.signatureButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    #печать
    keyboardTap(KP.F5)
    #OK
    keyboardTap(KP.ENTER)
    #подписать ENTER
    keyboardTap(KP.ENTER)
    time.sleep(1)
    # выход
    WC.find(WC.elPodProtocWindow)
    WC.wait(WC.elPodProtocWindow)
    FB.find(FB.exitButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
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




def fluraNorma():
    #Поиск кнопки Рентгено
    FB.findRentgenoButton()
    time.sleep(0.5)  # важно
    keyboardTap(MP.LKM_MOUSE)
    #зеленая кнопка play
    FB.find(FB.playButton)
    mouseTap(MP.LKM_MOUSE)
    #Дата
    keyboardTap(KP.ENTER)
    time.sleep(3)
    #Подтвердить случай?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # ?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    #Продолжить без создания случая
    FB.findWithTime(FB.prodBezSozSlu)
    mouseTap(MP.LKM_MOUSE)
    #диагноз
    FB.find(FB.diagnozButton)
    time.sleep(0.2)
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
    FB.findF8()
    mouseTap(MP.LKM_MOUSE)
    # Флюорографическое исследование органов грудной клетки
    FB.find(FB.mainShablonFlura)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(4)
    # шаблоны
    FB.find(FB.shablonButton)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    FB.find(FB.vybratButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    FB.find(FB.vyborSDobavleniem)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # В протоколе уже есть основной диагноз
    keyboardTap(KP.ENTER)
    # Сегодняшняя дата проведения исследования
    FB.find(FB.todayButton)
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
    # подписать
    FB.find(FB.signatureButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # Подписать ENTER
    keyboardTap(KP.ENTER)
    #Поиск ошибки ОМС ******************************************
    FE.findOMCError()
    #FE.findUIPError()
    #выход
    WC.find(WC.elPodProtocWindow)
    WC.wait(WC.elPodProtocWindow)
    FB.find(FB.exitButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(2)#важно
    # кнопка z01.8
    FB.find(FB.z018Button)
    mouseTap(MP.LKM_MOUSE)
    # закрыть
    FB.find(FB.closeZ018Button)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # результат
    FB.findResult()
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
    WC.find(WC.elPodProtocWindow)
    WC.wait(WC.elPodProtocWindow)
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
    #Продолжить сохранение приема
    time.sleep(1)
    FB.findWithTime(FB.prodSohrPriButton)
    mouseTap(MP.LKM_MOUSE)




def fluraNormaShort():
    # Поиск кнопки Рентгено
    FB.findRentgenoButton()
    time.sleep(1)  # важно
    keyboardTap(MP.LKM_MOUSE)
    # зеленая кнопка play
    FB.find(FB.playButton)
    mouseTap(MP.LKM_MOUSE)
    # Дата
    keyboardTap(KP.ENTER)
    time.sleep(3)
    # Подтвердить случай?
    keyboardTap(KP.ENTER)
    # ?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # Продолжить без создания случая
    FB.findWithTime(FB.prodBezSozSlu)
    mouseTap(MP.LKM_MOUSE)
    # История болезни
    FB.findF8()
    mouseTap(MP.LKM_MOUSE)
    # Флюорографическое исследование органов грудной клетки
    FB.find(FB.mainShablonFlura)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(4)
    #шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    FB.find(FB.vybratButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    FB.find(FB.vyborSDobavleniem)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # В протоколе уже есть основной диагноз
    keyboardTap(KP.ENTER)
    # Сегодняшняя дата проведения исследования
    FB.find(FB.todayButton)
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
    # подписать
    FB.find(FB.signatureButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    #Подписать ENTER
    keyboardTap(KP.ENTER)
    # Поиск ошибки ОМС ******************************************
    FE.findOMCError()
    #FE.findDataUIPError()
    #выход
    WC.find(WC.elPodProtocWindow)
    WC.wait(WC.elPodProtocWindow)
    FB.find(FB.exitButton)
    mouseTap(MP.LKM_MOUSE)
    #диагноз
    FB.find(FB.diagnozButton)
    mouseTap(MP.LKM_MOUSE)
    # кнопка z01.8
    FB.find(FB.z018Button)
    mouseTap(MP.LKM_MOUSE)
    # закрыть
    FB.find(FB.closeZ018Button)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # результат
    FB.findResult()
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
    time.sleep(3)
    WC.find(WC.elPodProtocWindow)
    WC.wait(WC.elPodProtocWindow)
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
    #Продолжить сохранение приема
    time.sleep(1)
    FB.findWithTime(FB.prodSohrPriButton)
    mouseTap(MP.LKM_MOUSE)















