import socket
import time

from udp_client import sock, UDP_IP, UDP_PORT


# Пакеты для UDP мыши

class MousePackagesUdp():
    ALL_KEYS_MOUSE_UP = "345640006053660536"
    INITIAL_MOUSE_POSITION = "345640006053660536"
    LKM_MOUSE = "345640016053660536"
    PKM_MOUSE = "345640026053660536"
    SKM_MOUSE = "345640046053660536"
    SCROLL_UP_MOUSE = "345670000000100000"
    SCROLL_DOWN_MOUSE = "345670000025500000"


def mouseTap(MESSAGE):  # метод нажимает и отпускает кнопку мыши
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
    time.sleep(0.2)
    sock.sendto(MousePackagesUdp.ALL_KEYS_MOUSE_UP.encode(), (UDP_IP, UDP_PORT))
    time.sleep(0.2)


def calc(a, b):
    sock.sendto('34564000{:05d}{:05d}'.format(a if a>=0 else 65536-a, b if b>=0 else 65536-b).encode(), (UDP_IP, UDP_PORT))


