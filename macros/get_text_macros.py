import time
import pyperclip

import keyboard
from keyboard import keyboardTap, keyboardLongTap, KeyboardPackagesUdp as KP
from filter_text import scan_text, writeOMC
from find_otrt import FindOTRT
import pyautogui as pag
from collections import deque, defaultdict


OMCList = deque([])


def getText():
    #разворачиваем программу OCTRT
    FindOTRT.findORTR(FindOTRT.OTRT)
    pag.click()
    #нажимаем кнопку сделать фото
    FindOTRT.findORTR(FindOTRT.take_photo)
    pag.click()
    #нопка сделать документ
    FindOTRT.findORTR(FindOTRT.document_photo)
    pag.click()
    time.sleep(3)
    #принять
    FindOTRT.findORTR(FindOTRT.OKTRT)
    pag.click()
    #распознать текст
    FindOTRT.findORTR(FindOTRT.find_textTRT)
    pag.click()
    #Закрыть
    FindOTRT.findORTR(FindOTRT.closeTRT)
    pag.click()
    #добавить в буфер обмена
    FindOTRT.findORTR(FindOTRT.addTRT)
    pag.click()
    #получение данных из буфера обмена
    full_text = pyperclip.paste()
    text = full_text
    s = scan_text(text)
    print(s[0])
    print(s[1])
    print(s[2])
    print(s[3])
    print(s[4])
    print(s[5])
    #открываем поле поиска
    keyboardLongTap(KP.LeftShift)
    keyboardTap(KP.F5)
    OMCList.appendleft(s[5])

    print(OMCList)
    #Пишем номер ОМС
    writeOMC(s[5])
    keyboard.keyboardTap(KP.ENTER)






