import time

from keyboard_emulator import keyboardTap, Keyboard as KP
from mouse import mouseTap, Mouse as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_title import FindTitles as FT
from find_refferal import FindRefferal as FR



def shop():
    # Поиск кнопки Рентгено
    FR.findRefferalButton(templateBlue=FR.shopBlueButton, template=FR.shopButton)
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
    FB.find(template=FB.F8Button, operator_w=FindObjects.subtraction, w_value=5)
    mouseTap(MP.LKM_MOUSE)
    # Рентгенография позвоночника
    FB.find(FB.rentgenUnifMainShablon)
    mouseTap(MP.LKM_MOUSE)
    # шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    mousePosition(5, 30)
    mouseTap(MP.LKM_MOUSE)
    # ШОП остеохондроз
    FB.find(FB.shopShablon)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    FB.find(FB.vyborSDobavleniem)
    mouseTap(MP.LKM_MOUSE)
    # подписать
    FB.find(FB.signatureButton)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    #Доп. блок
    # кнопка добавить
    FB.find(FB.plusAddButton)
    mouseTap(MP.LKM_MOUSE)
    # область
    FB.find(FB.oblast)
    mouseDoubleLKMTap()
    # Кнопка развернуть
    FB.find(FB.downButton)
    mouseTap(MP.LKM_MOUSE)
    # Грудь
    FB.find(FB.grudButton)
    mouseTap(MP.LKM_MOUSE)
    # Метод
    FB.find(FB.metod)
    mouseDoubleLKMTap()
    # Кнопка развернуть
    FB.find(FB.downButton)
    mouseTap(MP.LKM_MOUSE)
    # Рентген
    FB.find(FB.rentgen)
    mouseTap(MP.LKM_MOUSE)
    # исследования
    FB.find(FB.issledovanie)
    mouseDoubleLKMTap()
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


def pop(scolioz=False):
    # Поиск кнопки Рентгено
    FR.findRefferalButton()
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
    FB.find(template=FB.F8Button, operator_w=FindObjects.subtraction, w_value=5)
    mouseTap(MP.LKM_MOUSE)
    # Рентгенография позвоночника
    FB.find(FB.backboneShablon)
    mouseTap(MP.LKM_MOUSE)
    # шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    FB.find(FB.vybratButton)
    mouseTap(MP.LKM_MOUSE)
    # ПОП остеохондроз
    FB.find(FB.popShablon)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    FB.find(FB.vyborSDobavleniem)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # добавление сколиоза
    if scolioz is True:
        time.sleep(1)
        # добавляем в протокол описание сколиоза
        FT.findTitles(FT.protocolTitle, debug_mode=True)
        mousePosition(200, 20)
        mouseTap(MP.LKM_MOUSE)
        time.sleep(1)  # важно!
        mouseTap(MP.LKM_MOUSE)
        keyboardTap(KP.SPACEBAR)
        FB.find(FB.scoliozPOPButton)
        mouseDoubleLKMTap()
        # добавляем в заключение Сколиоз
        FT.findTitles(FT.resultTitle)
        mousePosition(1200, 0)
        mouseTap(MP.LKM_MOUSE)
        time.sleep(1)  # важно!
        mouseTap(MP.LKM_MOUSE)
        keyboardTap(KP.SPACEBAR)
        FB.find(FB.scoliozButton)
        mouseDoubleLKMTap()
    else:
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


def shopGop():
    # Поиск кнопки Рентгено
    FR.findRefferalButton()
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
    FB.find(template=FB.F8Button, operator_w=FindObjects.subtraction, w_value=5)
    mouseTap(MP.LKM_MOUSE)
    # Рентгенография позвоночника
    FB.find(FB.backboneShablon)
    mouseTap(MP.LKM_MOUSE)
    # шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    FB.find(FB.vybratButton)
    mouseTap(MP.LKM_MOUSE)
    # ШОП и ГОП остеохондроз
    FB.find(FB.shopGopShablon)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    FB.find(FB.vyborSDobavleniem)
    mouseTap(MP.LKM_MOUSE)
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



