import socket
import time

from udp_client import sock, UDP_IP, UDP_PORT


# Пакеты для UDP мыши

class MousePackagesUdp():
    ALL_KEYS_MOUSE_UP = "345640000000000000"
    LKM_MOUSE = "345640010000000000"
    PKM_MOUSE = "345640020000000000"
    SKM_MOUSE = "345640040000000000"
    SCROLL_UP_MOUSE = "345670000000100000"
    SCROLL_DOWN_MOUSE = "345670000025500000"


def initialMousePosition():
    INITIAL_MOUSE_POSITION = "345640006053660536"
    sock.sendto(INITIAL_MOUSE_POSITION.encode(), (UDP_IP, UDP_PORT))
    time.sleep(0.1)
    sock.sendto(MousePackagesUdp.ALL_KEYS_MOUSE_UP.encode(), (UDP_IP, UDP_PORT))
    time.sleep(0.1)


def mouseDoubleLKMTap():
        sock.sendto(MousePackagesUdp.LKM_MOUSE.encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.1)
        sock.sendto(MousePackagesUdp.ALL_KEYS_MOUSE_UP.encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.1)
        sock.sendto(MousePackagesUdp.LKM_MOUSE.encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.1)
        sock.sendto(MousePackagesUdp.ALL_KEYS_MOUSE_UP.encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.1)


def mouseTap(MESSAGE):  # метод нажимает и отпускает кнопку мыши
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.1)
        sock.sendto(MousePackagesUdp.ALL_KEYS_MOUSE_UP.encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.1)


def mousePosition(x, y):
    sock.sendto('34564000{:05d}{:05d}'.format(x if x>=0 else 65536+x, y if y>=0 else 65536+y).encode(), (UDP_IP, UDP_PORT))
    time.sleep(0.1)

def mouseScrollDown():  # метод нажимает и отпускает кнопку мыши
        sock.sendto(MousePackagesUdp.SCROLL_DOWN_MOUSE.encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.1)
        sock.sendto(MousePackagesUdp.ALL_KEYS_MOUSE_UP.encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.1)