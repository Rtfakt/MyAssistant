import time

from keyboard import keyboardTap, Keyboard as KP
from macros.cranium_macros import craniumNorma
from macros.lungs_macros import rOGKNorma, fluraNormaCT
from macros.obp_macros import OBPNorma, urografiaNorma
from mouse import mouseTap, Mouse as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_errors import FindErrors as FE
from find_refferal import FindRefferal as FR


def ogkObpSeparatedCT():
    OGKNormaCT()
    FB.findSearchMainButton()
    OBPNorma()


def fluraObpSeparatedCT():
    fluraNormaCT()
    FB.findSearchMainButton()
    OBPNorma()


def ogkObpUrografiaSeparatedCT():
    OGKNormaCT()
    FB.findSearchMainButton()
    OBPNorma()
    FB.findSearchMainButton()
    urografiaNorma()


def craniumOgkSeparatedCT():
    craniumNorma()
    FB.findSearchMainButton()
    OGKNormaCT()
