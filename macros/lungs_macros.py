import time
from keyboard_emulator import keyboardTap, Keyboard as KP
from mouse import mouseTap, Mouse as MP, mousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_errors import FindErrors as FE
from find_refferal import FindRefferal as FR
from find_objects import FindObjects

# (без печати)РЕНТГЕНОГРАФИЯ ОРГАНОВ ГРУДНОЙ КЛЕТКИ


def fluraNorma():
    # Поиск кнопки Рентгено
    FR.findRefferalButton(templateBlue=FR.fluraBlueButton, template=FR.fluraButton)
    # Дата
    FB.find(template=FB.F8Button, operator_w=FindObjects.subtraction, w_value=5)
    mouseTap(MP.LKM_MOUSE)
    # Подтвердить случай?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # ?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # Продолжить без создания случая
    FB.findWithTime(FB.prodBezSozSlu, timeWait=3)
    # mouseTap(MP.LKM_MOUSE)
    # диагноз
    FB.find(FB.diagnozButton)
    time.sleep(0.2)
    mouseTap(MP.LKM_MOUSE)
    # новый
    FB.find(FB.noviyButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # Поиск по коду
    keyboardTap(KP.Z)
    keyboardTap(KP.NUM0)
    keyboardTap(KP.NUM1)
    keyboardTap(KP.Ю)
    keyboardTap(KP.NUM8)
    # стрелка влево
    keyboardTap(KP.ENTER)
    #
    # Добавлять диагноз?
    keyboardTap(KP.ENTER)
    ##
    # диагноз уже добавлен
    keyboardTap(KP.ENTER)
    keyboardTap(KP.ENTER)
    keyboardTap(KP.ENTER)
    # сохранить
    keyboardTap(KP.F2)
    time.sleep(1)
    # считать прием диспансерным?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # История болезни
    FB.find(template=FB.F8Button, operator_w=FindObjects.subtraction, w_value=5)
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
    # время проведения исследования
    keyboardTap(KP.TAB)
    keyboardTap(KP.NUM1)
    # подписать
    FB.find(FB.signatureButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # Подписать ENTER
    keyboardTap(KP.ENTER)
    # Поиск ошибки ОМС ******************************************
    FE.findOMCError()
    # FE.findUIPError()
    # выход
    WC.find(WC.elPodProtocWindow)
    WC.wait(WC.elPodProtocWindow)
    FB.find(FB.exitButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(2)  # важно
    # кнопка z01.8
    FB.find(FB.z018Button)
    mouseTap(MP.LKM_MOUSE)
    # закрыть
    FB.find(FB.closeZ018Button)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # результат
    FB.findResult()
    # лечение завершено
    FB.find(FB.lechenieEnd)
    mouseTap(MP.LKM_MOUSE)
    # Исход заболевания
    mousePosition(135, -18)
    mouseTap(MP.LKM_MOUSE)
    # осмотр
    FB.find(FB.osmotr)
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
    FB.find(FB.saveF2Button)
    keyboardTap(KP.F2)
    # сохранить изменения?
    keyboardTap(KP.ENTER)
    # выбрать
    FB.find(FB.vybratF2Button)
    keyboardTap(KP.F2)
    # выбрать
    FB.find(FB.vybratF2Button)
    keyboardTap(KP.F2)
    # нет диагноза в приеме
    keyboardTap(KP.ENTER)
    # Продолжить сохранение приема
    time.sleep(2)
    FB.findWithTime(FB.prodSohrPriButton)


def fluraNormaCT():
    # Поиск кнопки Рентгено
    FR.findRefferalButton(templateBlue=FR.fluraBlueButton, template=FR.fluraButton)
    # Дата
    FB.find(FB.okButton)
    mouseTap(MP.LKM_MOUSE)
    # Подтвердить случай?
    mouseTap(MP.LKM_MOUSE)
    # ?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # Продолжить без создания случая
    FB.findWithTime(FB.prodBezSozSlu)
    # История болезни
    FB.find(template=FB.F8Button, operator_w=FindObjects.subtraction, w_value=5)
    mouseTap(MP.LKM_MOUSE)
    # Флюорографическое исследование органов грудной клетки
    FB.find(FB.mainShablonFlura)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(4)
    # шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    FB.find(FB.vybratButton)
    mouseTap(MP.LKM_MOUSE)
    # убрать диагноз
    FB.find(FB.threePointsAndCloseButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    FB.find(FB.vyborSDobavleniem)
    mouseTap(MP.LKM_MOUSE)
    # В протоколе уже есть основной диагноз
    time.sleep(1)
    keyboardTap(KP.ENTER)
    # Сегодняшняя дата проведения исследования
    FB.find(FB.todayButton)
    mouseTap(MP.LKM_MOUSE)
    # время проведения исследования
    keyboardTap(KP.TAB)
    keyboardTap(KP.NUM1)
    # подписать
    FB.find(FB.signatureButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # Подписать ENTER
    keyboardTap(KP.ENTER)
    # Поиск ошибки ОМС ******************************************
    FE.findOMCError()
    # FE.findDataUIPError()
    # выход
    WC.find(WC.elPodProtocWindow)
    WC.wait(WC.elPodProtocWindow)
    FB.find(FB.exitButton)
    mouseTap(MP.LKM_MOUSE)
    # считать прием диспансерным?
    keyboardTap(KP.LeftArrow)
    keyboardTap(KP.ENTER)
    # сохранить
    FB.find(FB.saveF2Button)
    mouseTap(MP.LKM_MOUSE)
    # сохранить изменения?
    # keyboardTap(KP.ENTER)
    # выбрать
    FB.find(FB.vybratF2Button)
    keyboardTap(KP.F2)
    # выбрать
    FB.find(FB.vybratF2Button)
    keyboardTap(KP.F2)
    # нет диагноза в приеме
    # keyboardTap(KP.ENTER)
    # Продолжить сохранение приема
    time.sleep(2)
    FB.findWithTime(FB.prodSohrPriButton)


def rOGKNorma(print=False, CT=False):
    # Поиск кнопки Рентгено
    FR.findRefferalButton(templateBlue=FR.OGKBlueButton, template=FR.OGKButton)
    # Дата
    FB.find(FB.okButton)
    mouseTap(MP.LKM_MOUSE)
    # Продолжить без создания случая
    FB.findWithTime(FB.prodBezSozSlu, timeWait=4)
    if CT == True:
        # Подтвердить случай?
        keyboardTap(KP.ENTER)
        # ?
        keyboardTap(KP.RightArrow)
        keyboardTap(KP.ENTER)
    else:
        # Подтвердить случай?
        FB.findWithTime(FB.noButton, timeWait=2)
        mouseTap(MP.LKM_MOUSE)
        # ?
        keyboardTap(KP.RightArrow)
        keyboardTap(KP.ENTER)

    # История болезни
    FB.find(template=FB.F8Button, operator_w=FindObjects.subtraction, w_value=5)
    mouseTap(MP.LKM_MOUSE)
    # Рентгенографическое исследование(униф.)
    FB.find(FB.rentgenUnifMainShablon)
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
    # подписать
    FB.find(FB.signatureButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    # печать
    if print == True:
        keyboardTap(KP.F5)
        # OK
        keyboardTap(KP.ENTER)
        # подписать ENTER
        keyboardTap(KP.ENTER)
        time.sleep(1)
    else:
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
