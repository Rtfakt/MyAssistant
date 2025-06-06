import time

from write_text import writePass, writeText
from find_title import FindTitles as FT
from keyboard_emulator import keyboardTap, Keyboard as KP, keyboardLongTap

from mouse import mouseTap, Mouse as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_objects import FindObjects as FO
from find_archimed_button import FindArchimedButton as FAB





def startIK():
    #ярлык архимеда

    # ярлык инфоклиники
    FB.find(FB.firstInfoclinicaButton)
    # переключаем язык на английский
    initialMousePosition()
    mousePosition(1780, 1050)
    mouseTap(MP.LKM_MOUSE)
    mousePosition(0, -100)
    mouseTap(MP.LKM_MOUSE)
    FB.find(FB.firstInfoclinicaButton)
    mouseDoubleLKMTap()
    time.sleep(1)
    # подключить
    keyboardTap(KP.ENTER)
    # находим иконку авторизации
    time.sleep(5)
    FT.findUserNameWithTime()
    # место работы
    writePass()
    # Подтвердить
    #keyboardTap(KP.ENTER)
    # значок инфоклиники
    FB.find(FB.secondInfoclinicaButton)
    mouseDoubleLKMTap()
    time.sleep(2)
    # поликлиника
    keyboardTap(KP.ENTER)
    WC.find(WC.authWindows)
    mouseTap(MP.LKM_MOUSE)
    # смена поля ввода
    keyboardTap(KP.TAB)
    # ввод
    keyboardTap(KP.NUM1)
    keyboardTap(KP.NUM2)
    keyboardTap(KP.NUM3)
    keyboardTap(KP.NUM4)
    keyboardTap(KP.NUM5)
    keyboardTap(KP.NUM6)
    keyboardTap(KP.ENTER)
    # продолжить F2
    FB.find(FB.prodolgitF2Button)
    mouseTap(MP.LKM_MOUSE)
    # картотека
    FB.find(FB.cartotekaButton)
    mouseTap(MP.LKM_MOUSE)
    #для сортировки по карте нужно найти любого человека и отсортировать список
    FB.find(FB.searchMain, operator_w=FO.subtraction,w_value=150)  # находим поле поиска в инфоклинике  # находим поле поиска
    mouseTap(MP.LKM_MOUSE)
    keyboardLongTap(KP.LeftControl)
    keyboardTap(KP.A)
    time.sleep(0.5)
    writeText('Илларионова Елена')
    time.sleep(2)
    # № амбулаторной карты
    FB.find(FB.NAmbulatKart)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(1)
    FB.find(FB.NAmbulatKart)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(2)
    # сворачиваем инфоклинику
    #FB.find(FAB.svernut_infokliniku)
    #mouseTap(MP.LKM_MOUSE)


def endIK():
    # выход из инфоклиники1
    FB.find(FB.exitFromInfoclinikaButton)
    mouseTap(MP.LKM_MOUSE)
    # ожидание появления окна
    FB.find(FB.cartotekaButton)
    # выход из инфоклиники2
    FB.find(FB.exitFromInfoclinikaButton)
    mouseTap(MP.LKM_MOUSE)
    # завершение работы
    FB.find(FB.endWork)
    mouseTap(MP.LKM_MOUSE)
    # ожидание закрытия программы
    FB.find(FB.secondInfoclinicaButton)
    mouseTap(MP.LKM_MOUSE)
    # Пуск
    FB.find(FB.startButton)
    mouseTap(MP.LKM_MOUSE)
    # Значек пользователя
    FB.find(FB.userButton)
    mouseTap(MP.LKM_MOUSE)
    # выход
    FB.find(FB.windowsExit)
    mouseTap(MP.LKM_MOUSE)
    # ожидание появления рабочего стола
    FB.find(FB.firstInfoclinicaButton)
    # Пуск
    FB.find(FB.startButton)
    mouseTap(MP.LKM_MOUSE)
    # кнопка выключения
    FB.find(FB.offButton)
    mouseTap(MP.LKM_MOUSE)


def restartIK():
    # Пуск
    FB.find(FB.startButton)
    mouseTap(MP.LKM_MOUSE)
    # Значек пользователя
    FB.find(FB.userButton)
    mouseTap(MP.LKM_MOUSE)
    # выход
    FB.find(FB.windowsExit)
    mouseTap(MP.LKM_MOUSE)
    # все равно выйти
    FB.find(FB.vseRavnoVyitiButton)
    mouseTap(MP.LKM_MOUSE)
    # ярлык инфоклиники
    FB.find(FB.firstInfoclinicaButton)
    # переключаем язык на английский
    initialMousePosition()
    mousePosition(1780, 1050)
    mouseTap(MP.LKM_MOUSE)
    mousePosition(0, -100)
    mouseTap(MP.LKM_MOUSE)
    FB.find(FB.firstInfoclinicaButton)
    mouseDoubleLKMTap()
    time.sleep(1)
    # подключить
    keyboardTap(KP.ENTER)
    # находим иконку авторизации
    FT.findUserNameWithTime()
    # место работы
    writePass()
    # keyboardLongTap(KP.LeftShift)
    # keyboardTap(KP.C)
    # keyboardTap(KP.R)
    # keyboardTap(KP.B)
    # keyboardTap(KP.S)
    # keyboardTap(KP.K)
    # keyboardTap(KP.A)
    # keyboardTap(KP.V)
    # keyboardTap(KP.NUM1)
    # keyboardTap(KP.NUM2)
    # Подтвердить
    # keyboardTap(KP.ENTER)
    # ярлык инфоклиники
    FB.find(FB.firstInfoclinicaButton)
    mouseDoubleLKMTap()
    time.sleep(1)
    # подключить
    keyboardTap(KP.ENTER)
    # находим иконку авторизации
    FT.findUserNameWithTime()
    # место работы
    writePass()
    # Подтвердить
    # keyboardTap(KP.ENTER)
    # значок инфоклиники
    FB.find(FB.secondInfoclinicaButton)
    mouseDoubleLKMTap()
    time.sleep(2)
    # поликлиника
    keyboardTap(KP.ENTER)
    WC.find(WC.authWindows)
    # смена поля ввода
    keyboardTap(KP.TAB)
    # ввод
    keyboardTap(KP.NUM1)
    keyboardTap(KP.NUM2)
    keyboardTap(KP.NUM3)
    keyboardTap(KP.NUM4)
    keyboardTap(KP.NUM5)
    keyboardTap(KP.NUM6)
    keyboardTap(KP.ENTER)
    time.sleep(1)
    # продолжить F2
    keyboardTap(KP.F2)
    # картотека
    FB.find(FB.cartotekaButton)
    mouseTap(MP.LKM_MOUSE)
    # № амбулаторной карты
    FB.find(FB.NAmbulatKart)
    time.sleep(1)
    FB.find(FB.NAmbulatKart)


def keyMacros():
    initialMousePosition()
    mousePosition(1820, 1040)
    mouseTap(MP.LKM_MOUSE)
    mousePosition(0, -60)
    mouseTap(MP.LKM_MOUSE)
    initialMousePosition()
    mousePosition(1000, 620)
    mouseTap(MP.LKM_MOUSE)
    writePass()


def dop_block():    # Доп. блок
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
    # Кнопка развернуть
    FB.find(FB.downButton)
    mouseTap(MP.LKM_MOUSE)
    keyboardTap(KP.DownArrow)
    keyboardTap(KP.ENTER)