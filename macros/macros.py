import time

from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, mouseDoubleLKMTap, initialMousePosition




def restartIK():

    #Начало входа
    initialMousePosition()
    mousePosition(30, 150)
    mouseDoubleLKMTap()
    #подключить
    keyboardTap(KP.ENTER)
    time.sleep(5)
    # имя

    keyboardTap(KP.A)
    keyboardTap(KP.K)
    keyboardTap(KP.O)
    keyboardTap(KP.N)
    keyboardTap(KP.O)
    keyboardTap(KP.R)
    keyboardTap(KP.E)
    keyboardTap(KP.V)
    #место работы










def antiSleep():
    while True:
     initialMousePosition()
     mousePosition(200, 0)
     mouseTap(MP.LKM_MOUSE)
     time.sleep(300)





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
     mouseTap(MP.LKM_MOUSE)
     # выход
     mousePosition(0, -50)
     mouseTap(MP.LKM_MOUSE)
     time.sleep(3)