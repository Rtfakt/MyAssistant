import time

from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_refferal import FindRefferal as FR




def craniumNorma():
    # Поиск кнопки Рентгено
    FR.findRefferalButton(templateBlue=FR.CraniumBlueButton, template=FR.CraniumButton)
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
    # История болезни
    FB.findF8()
    mouseTap(MP.LKM_MOUSE)
    # Рентгенографическое исследование(униф.)
    FB.find(FB.rentgenUnifMainShablon)
    mouseTap(MP.LKM_MOUSE)
    # шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    mousePosition(5, 30)
    mouseTap(MP.LKM_MOUSE)
    # череп норма
    FB.find(FB.craniumNorma)
    mouseTap(MP.LKM_MOUSE)
    # Выбор с добавлением
    FB.find(FB.vyborSDobavleniem)
    mouseTap(MP.LKM_MOUSE)
    # подписать
    FB.find(FB.signatureButton)
    mouseTap(MP.LKM_MOUSE)
    # Доп. блок
    # кнопка добавить
    FB.find(FB.plusAddButton)
    mouseTap(MP.LKM_MOUSE)
    # область
    FB.find(FB.oblast)
    mouseDoubleLKMTap()
    # Кнопка развернуть
    FB.find(FB.downButton)
    mouseTap(MP.LKM_MOUSE)
    # Голова шея
    keyboardTap(KP.DownArrow)
    keyboardTap(KP.DownArrow)
    keyboardTap(KP.ENTER)
    # Метод
    FB.find(FB.metodLong)
    mouseDoubleLKMTap()
    # Кнопка развернуть
    FB.find(FB.downLongButton)
    mouseTap(MP.LKM_MOUSE)
    # Рентген
    FB.find(FB.rentgen)
    mouseTap(MP.LKM_MOUSE)
    # исследования
    FB.find(FB.issledovanieLong)
    mouseDoubleLKMTap()
    # Кнопка развернуть
    FB.find(FB.downLongButton)
    mouseTap(MP.LKM_MOUSE)
    keyboardTap(KP.DownArrow)
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