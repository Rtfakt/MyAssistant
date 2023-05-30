
from tkinter import *

from keyboard import keyboardTap, KeyboardPackagesUdp
from mouse import mouseTap, MousePackagesUdp

keyboardClick = KeyboardPackagesUdp
mouseClick = MousePackagesUdp

#РЕНТГЕНОГРАФИЯ ОРГАНОВ ГРУДНОЙ КЛЕТКИ
mouseTap(MousePackagesUdp.INITIAL_MOUSE_POSITION)
#Начало


keyboardTap(KeyboardPackagesUdp.RightArrow)
keyboardTap(KeyboardPackagesUdp.ENTER)

