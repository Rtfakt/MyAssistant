import time

from keyboard_emulator import keyboardTap, Keyboard as KP
from macros.cranium_macros import craniumNorma
from macros.lungs_macros import rOGKNorma, fluraNormaCT
from macros.obp_macros import OBPNorma, urografiaNorma
from mouse import mouseTap, Mouse as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_errors import FindErrors as FE
from find_refferal import FindRefferal as FR
from find_objects import FindObjects


def ogkObpSeparatedCT():
    rOGKNorma()
    FB.find(FB.searchMain, operator_w=FindObjects.subtraction, w_value=150)#находим поле поиска в инфоклинике
    OBPNorma()


def fluraObpSeparatedCT():
    fluraNormaCT()
    FB.find(FB.searchMain, operator_w=FindObjects.subtraction, w_value=150)#находим поле поиска в инфоклинике
    OBPNorma()


def ogkObpUrografiaSeparatedCT():
    OGKNormaCT()
    FB.find(FB.searchMain, operator_w=FindObjects.subtraction, w_value=150)#находим поле поиска в инфоклинике
    OBPNorma()
    FB.find(FB.searchMain, operator_w=FindObjects.subtraction, w_value=150)#находим поле поиска в инфоклинике
    urografiaNorma()


def craniumOgkSeparatedCT():
    craniumNorma()
    FB.find(FB.searchMain, operator_w=FindObjects.subtraction, w_value=150)#находим поле поиска в инфоклинике
    OGKNormaCT()
