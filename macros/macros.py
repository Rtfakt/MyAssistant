import time

from find_title import FindTitles as FT
from keyboard import keyboardTap, KeyboardPackagesUdp as KP, keyboardLongTap


from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC






def test():
    #if result == 1:
        print('правого и левого')


def startIK():
    # смена языка
    mouseTap(MP.LKM_MOUSE)
    FB.find(FB.pycButton)
    mouseTap(MP.LKM_MOUSE)
    mousePosition(0, -80)
    mouseDoubleLKMTap()
    # user
    initialMousePosition()
    mousePosition(1000, 620)
    mouseTap(MP.LKM_MOUSE)
    keyboardLongTap(KP.LeftShift)
    keyboardTap(KP.NUM1)
    keyboardTap(KP.NUM3)
    keyboardTap(KP.NUM4)
    keyboardTap(KP.R)
    keyboardTap(KP.E)
    keyboardTap(KP.G)
    keyboardTap(KP.Ю)
    keyboardTap(KP.NUM3)
    keyboardTap(KP.NUM7)
    keyboardTap(KP.ENTER)
    # ярлык инфоклиники
    FB.find(FB.firstInfoclinicaButton)
    #initialMousePosition()
    #mousePosition(30, 150)
    mouseDoubleLKMTap()
    time.sleep(1)
    # подключить
    keyboardTap(KP.ENTER)
    #находим иконку авторизации
    FT.findUserNameWithTime()
    #time.sleep(10)
    # поле имени

    # место работы
    #keyboardTap(KP.TAB)
    keyboardLongTap(KP.LeftShift)
    keyboardTap(KP.C)
    keyboardTap(KP.R)
    keyboardTap(KP.B)
    keyboardTap(KP.S)
    keyboardTap(KP.K)
    keyboardTap(KP.A)
    keyboardTap(KP.V)
    keyboardTap(KP.NUM4)
    keyboardTap(KP.NUM5)
    # Подтвердить
    keyboardTap(KP.ENTER)
    # значок инфоклиники
    FB.find(FB.secondInfoclinicaButton)
    mouseDoubleLKMTap()
    time.sleep(2)
    #поликлиника
    keyboardTap(KP.ENTER)
    WC.find(WC.authWindows)
    #смена поля ввода
    keyboardTap(KP.TAB)
    #ввод
    keyboardTap(KP.NUM1)
    keyboardTap(KP.NUM2)
    keyboardTap(KP.NUM3)
    keyboardTap(KP.NUM4)
    keyboardTap(KP.NUM5)
    keyboardTap(KP.NUM6)
    keyboardTap(KP.ENTER)
    time.sleep(1)
    #продолжить F2
    keyboardTap(KP.F2)
    #картотека
    FB.find(FB.cartotekaButton)
    mouseTap(MP.LKM_MOUSE)




def antiSleep():
    while True:
     initialMousePosition()
     mousePosition(200, 0)
     mouseTap(MP.LKM_MOUSE)
     time.sleep(300)


def endIK():
    # выход из инфоклиники
    FB.find(FB.exitFromInfoclinikaButton)
    mouseTap(MP.LKM_MOUSE)
    # завершение работы
    mousePosition(0, 20)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(2)
    # Пуск
    initialMousePosition()
    mousePosition(10, 1050)
    mouseTap(MP.LKM_MOUSE)
    # Значек пользователя
    mousePosition(10, -130)
    time.sleep(1)
    mouseTap(MP.LKM_MOUSE)
    # выход
    mousePosition(0, -50)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(3)


def restartIK():
     initialMousePosition()
     # выход
     mousePosition(1900, 50)
     mouseTap(MP.LKM_MOUSE)
     # выход
     FB.find(FB.exitButton)
     # подписать
     keyboardTap(KP.ENTER)
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
     # выход из инфоклиники
     FB.find(FB.exitFromInfoclinikaButton)
     mouseTap(MP.LKM_MOUSE)
     # завершение работы
     mousePosition(0, 20)
     mouseTap(MP.LKM_MOUSE)
     time.sleep(2)
     # Пуск
     initialMousePosition()
     mousePosition(10, 1050)
     mouseTap(MP.LKM_MOUSE)
     # Значек пользователя
     mousePosition(10, -130)
     time.sleep(1)
     mouseTap(MP.LKM_MOUSE)
     # выход
     mousePosition(0, -50)
     mouseTap(MP.LKM_MOUSE)
     time.sleep(3)
     # смена языка
     initialMousePosition()
     mousePosition(1780, 1060)
     mouseTap(MP.LKM_MOUSE)
     mousePosition(0, -120)
     mouseDoubleLKMTap()
     # Начало входа
     initialMousePosition()
     mousePosition(30, 150)
     mouseDoubleLKMTap()
     time.sleep(1)
     # подключить
     keyboardTap(KP.ENTER)
     # поле имени
     time.sleep(7)
     # имя
     keyboardTap(KP.A)
     keyboardTap(KP.K)
     keyboardTap(KP.O)
     keyboardTap(KP.N)
     keyboardTap(KP.O)
     keyboardTap(KP.R)
     keyboardTap(KP.E)
     keyboardTap(KP.V)
     # место работы
     keyboardTap(KP.TAB)
     keyboardLongTap(KP.LeftShift)
     keyboardTap(KP.C)
     keyboardTap(KP.R)
     keyboardTap(KP.B)
     keyboardTap(KP.S)
     keyboardTap(KP.K)
     keyboardTap(KP.A)
     keyboardTap(KP.V)
     keyboardTap(KP.NUM5)
     keyboardTap(KP.NUM8)
     # Подтвердить
     keyboardTap(KP.ENTER)
     time.sleep(10)
     # значок инфоклиники
     initialMousePosition()
     mousePosition(20, 650)
     mouseDoubleLKMTap()
     time.sleep(1)
     # поликлиника
     keyboardTap(KP.ENTER)
     time.sleep(5)
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
     time.sleep(25)
     # картотека
     initialMousePosition()
     mousePosition(100, 200)
     mouseTap(MP.LKM_MOUSE)
     time.sleep(4)














