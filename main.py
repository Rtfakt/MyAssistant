import time
from tkinter import *

from keyboard import keyboardTap, KeyboardPackagesUdp
from mouse import mouseTap, MousePackagesUdp as MP, calc



#РЕНТГЕНОГРАФИЯ ОРГАНОВ ГРУДНОЙ КЛЕТКИ

#Начало

mouseTap(MousePackagesUdp.INITIAL_MOUSE_POSITION)
mouseTap(MP.INITIAL_MOUSE_POSITION)

calc(1500, 500)
time.sleep(1)
calc(100, 100)