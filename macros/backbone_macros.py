import time

from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_title import FindTitles as FT



def shop():
    # История болезни
    FB.findF8()
    mouseTap(MP.LKM_MOUSE)
    # Рентгенография позвоночника
    mousePosition(0, 210)
    mouseTap(MP.LKM_MOUSE)
    # шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    mousePosition(5, 30)
    mouseTap(MP.LKM_MOUSE)
    # ПОП остеохондроз
    mousePosition(-605, 260)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    mousePosition(130, -260)
    time.sleep(1)
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


def pop(scolioz=False):
    # История болезни
    FB.findF8()
    mouseTap(MP.LKM_MOUSE)
    # Рентгенография позвоночника
    mousePosition(0, 210)
    mouseTap(MP.LKM_MOUSE)
    # шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    mousePosition(5, 30)
    mouseTap(MP.LKM_MOUSE)
    # ПОП остеохондроз
    mousePosition(-605, 220)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    mousePosition(130, -220)
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



