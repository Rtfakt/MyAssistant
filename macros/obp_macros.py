import time

from keyboard import keyboardTap, Keyboard as KP
from mouse import mouseTap, Mouse as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_refferal import FindRefferal as FR



def OBPNorma():
    # Поиск кнопки Рентгено
    FR.findRefferalButton(templateBlue=FR.OBPBlueButton, template=FR.OBPButton)
    # Дата
    FB.find(FB.okButton)
    mouseTap(MP.LKM_MOUSE)
    # Подтвердить случай?
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
    FB.find(FB.vybratButton)
    mouseTap(MP.LKM_MOUSE)
    # ОБП норма
    FB.find(FB.ObpShablon)
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
    # живот
    FB.find(FB.zhivot)
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
    # Кнопка развернуть
    FB.find(FB.downButton)
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



def urografiaNorma():
    # Поиск кнопки Рентгено
    FR.findRefferalButton(templateBlue=FR.rentgenPochekBlueButton, template=FR.rentgenPochekButton)
    # Дата
    FB.find(FB.okButton)
    mouseTap(MP.LKM_MOUSE)
    # Подтвердить случай?
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
    FB.find(FB.vybratButton)
    mouseTap(MP.LKM_MOUSE)
    # урография норма
    FB.find(FB.urografiaShablon)
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
    # живот
    FB.find(FB.zhivot)
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
    # Кнопка развернуть
    FB.find(FB.downButton)
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