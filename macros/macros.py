import time

from keyboard import keyboardTap, KeyboardPackagesUdp as KP, keyboardLongTap
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, mouseDoubleLKMTap, initialMousePosition




def startIK():
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
    time.sleep(10)
    # имя
    #keyboardTap(KP.A)
    #keyboardTap(KP.K)
    #keyboardTap(KP.O)
    #keyboardTap(KP.N)
    #keyboardTap(KP.O)
    #keyboardTap(KP.R)
    #keyboardTap(KP.E)
    #keyboardTap(KP.V)
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
    keyboardTap(KP.NUM5)
    keyboardTap(KP.NUM8)
    # Подтвердить
    keyboardTap(KP.ENTER)
    time.sleep(11)
    # значок инфоклиники
    initialMousePosition()
    mousePosition(20, 650)
    mouseDoubleLKMTap()
    time.sleep(2)
    #поликлиника
    keyboardTap(KP.ENTER)
    time.sleep(6)
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
    time.sleep(25)
    #картотека
    initialMousePosition()
    mousePosition(100, 200)
    mouseTap(MP.LKM_MOUSE)
    time.sleep(4)





















def antiSleep():
    while True:
     initialMousePosition()
     mousePosition(200, 0)
     mouseTap(MP.LKM_MOUSE)
     time.sleep(300)




def restartIK():
     initialMousePosition()
     # выход

     mousePosition(1900, 50)
     mouseTap(MP.LKM_MOUSE)
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
     initialMousePosition()
     # выход
     mousePosition(455, 35)
     time.sleep(2)
     mouseTap(MP.LKM_MOUSE)
     # завершение работы
     mousePosition(0, 20)
     mouseTap(MP.LKM_MOUSE)
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













