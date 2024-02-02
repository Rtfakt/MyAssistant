import time

from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_errors import FindErrors as FE
from find_refferal import FindRefferal as FR



def craniumLungsMacros():
    # Поиск кнопки Рентгено
    FR.findRefferalButton(templateBlue=FR.rentgenoBlueButton, template=FR.rentgenoButton)
    # Дата
    FB.find(FB.okButton)
    mouseTap(MP.LKM_MOUSE)
    # Подтвердить случай?
    mouseTap(MP.LKM_MOUSE)
    # ?
    keyboardTap(KP.RightArrow)
    keyboardTap(KP.ENTER)
    # Продолжить без создания случая
    FB.findWithTime(FB.prodBezSozSlu)
    # История болезни
    FB.findF8()
    mouseTap(MP.LKM_MOUSE)
    # Рентгенологическое исследование
    FB.find(FB.doubleShablon)
    mouseTap(MP.LKM_MOUSE)
    # шаблоны
    FB.find(FB.shablonButton)
    mouseTap(MP.LKM_MOUSE)
    # Выбрать
    FB.find(FB.vybratButton)
    mouseTap(MP.LKM_MOUSE)
    # Череп легкие




