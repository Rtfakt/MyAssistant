import socket
import time
import Keyboards
from tkinter import *

#Пакеты для UDP клавиатуры

All_KEYS_KEYBOARD_UP = "345680000000000000"

#ЗАДАЧА

def calc(a,b):
    s = '34564000'
    for i in range(5, len(str(a))): s+='0'
    s+=str(a)
    for i in range(5, len(str(b))): s+='0'
    s+=str(b)
    return s

"3456 4 000 00000 00000"  #распиши как будут выглядеть реальные примеры
ID = "3456"
b1 = "4"
b2 = "000"
b3 = "00000"
b4 = "00000"

#Если значение положительное то должно получиться вот так
# введя значение x = 234. находим b3.  00000 + 234 b3 должен быть равен  00234
# введя значение y = 1234. находим b4. 00000 + 1234 должен быть равен 01234


# дальше изи решать Не надо
#Если x y отрицательные то
# 65536 - 234 = 65 302
# 65536 - 1234 = 64302

#           345640000012300321
#Если Null "345640000000000000"

#Отправка пакета по UDP

UDP_IP = "192.168.0.222"
UDP_PORT = 12345
MESSAGE = NONE
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def sendToUDP(MESSAGE) :
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
    time.sleep(0.2)



#РЕНТГЕНОГРАФИЯ ОРГАНОВ ГРУДНОЙ КЛЕТКИ
sendToUDP(INITIAL_MOUSE_POSITION)
#Начало


