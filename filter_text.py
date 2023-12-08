import re
import time
from dict_rus_letters import dictRusLetters
from keyboard import KeyboardPackagesUdp
from udp_client import sock, UDP_IP, UDP_PORT
from keyboard import keyboardTap, KeyboardPackagesUdp as KP, keyboardLongTap


def filter_text(text):
    scan = []
    # Использование регулярных выражений для поиска:
    scan.append(re.findall(r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}', text)[1])
    scan.extend(re.findall(r'[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+', text)[0].split()[0:3])
    scan.append(re.findall(r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}', text)[2])
    scan.append(re.findall(r'[0-9]{16}', text)[0])
    return scan


# Считываем текст из файла
#with open("example_texts/1.txt", encoding="UTF-8") as f:
#    text = f.read()

#s = scan_text(text)

#print(s)  # Выводит список из 5 элементов, можно обратиться к каждому элементу:
#print(s[0])
#print(s[1])
#print(s[2])
#print(s[3])
#print(s[4])
#print(s[5])

#current_date = s[0]
#last_name_data = s[1]
#first_name_data = s[2]
#middle_name_data = s[3]
#birthdate_data = s[4]
#OMCdata = s[5]

#name = "%s %s %s" % (last_name_data, first_name_data, middle_name_data)


def writeTextAuto(name):
    for letter in name:
       if letter in dictRusLetters:
          res = dictRusLetters[letter]
          time.sleep(0.1)
          sock.sendto(res.encode(), (UDP_IP, UDP_PORT))
          sock.sendto(KP.All_KEYS_KEYBOARD_UP.encode(), (UDP_IP, UDP_PORT))
          time.sleep(0.1)


def writeFIO(name):

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


def writeText():
    keyboardLongTap(KP.LeftShift)
    keyboardTap(KP.C)
    keyboardTap(KP.R)
    keyboardTap(KP.B)
    keyboardTap(KP.S)
    keyboardTap(KP.K)
    keyboardTap(KP.A)
    keyboardTap(KP.V)
    keyboardTap(KP.NUM5)
    keyboardTap(KP.NUM6)
    # Подтвердить
    keyboardTap(KP.ENTER)