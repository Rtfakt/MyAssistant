import time
from dict_rus_letters import dictRusLetters
from udp_client import sock, UDP_IP, UDP_PORT
from keyboard import keyboardTap, Keyboard as KP, keyboardLongTap
from find_button import FindButton as FB
from mouse import Mouse as MP, mouseTap

def writeTextAuto(name):
    for letter in name:
        if letter in dictRusLetters:
            res = dictRusLetters[letter]
            time.sleep(0.1)
            sock.sendto(res.encode(), (UDP_IP, UDP_PORT))
            sock.sendto(KP.All_KEYS_KEYBOARD_UP.encode(), (UDP_IP, UDP_PORT))
            time.sleep(0.1)


def writeText(name):
    FB.find(template=FB.searchMain, operator_w=FB.subtraction, w_value=150)  # находим поле поиска
    mouseTap(MP.LKM_MOUSE)
    keyboardLongTap(KP.LeftControl)
    keyboardTap(KP.A)
    for letter in name:
        if letter in dictRusLetters:
            res = dictRusLetters[letter]
            time.sleep(0.1)
            sock.sendto(res.encode(), (UDP_IP, UDP_PORT))
            sock.sendto(KP.All_KEYS_KEYBOARD_UP.encode(), (UDP_IP, UDP_PORT))
            time.sleep(0.1)


def writeOMC(OMCdata):
    time.sleep(0.2)  # важно
    keyboardLongTap(KP.LeftShift)
    keyboardTap(KP.F5)
    for letter in OMCdata:
        if letter in dictRusLetters:
            res = dictRusLetters[letter]
            time.sleep(0.1)
            sock.sendto(res.encode(), (UDP_IP, UDP_PORT))
            sock.sendto(KP.All_KEYS_KEYBOARD_UP.encode(), (UDP_IP, UDP_PORT))
            time.sleep(0.1)


def writePass():
    keyboardLongTap(KP.LeftShift)
    keyboardTap(KP.C)
    keyboardTap(KP.R)
    keyboardTap(KP.B)
    keyboardTap(KP.S)
    keyboardTap(KP.K)
    keyboardTap(KP.A)
    keyboardTap(KP.V)
    keyboardTap(KP.NUM6)
    # Подтвердить
    keyboardTap(KP.ENTER)


def writeKey():
    keyboardTap(KP.NUM1)
    keyboardTap(KP.NUM2)
    keyboardTap(KP.NUM3)
    keyboardTap(KP.NUM4)
    keyboardTap(KP.NUM5)
    keyboardTap(KP.NUM6)
    keyboardTap(KP.NUM7)
    keyboardTap(KP.NUM8)
    keyboardTap(KP.ENTER)

