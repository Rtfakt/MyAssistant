import time
import pyperclip

import keyboard
from keyboard import keyboardTap, keyboardLongTap, KeyboardPackagesUdp as KP
from filter_text import scan_text, writeOMC
from open_programs import OpenPrograms as OP
import pyautogui as pag
from collections import deque, defaultdict


OMCList = deque([])


def getTextFromOTRT():
    #разворачиваем программу OCTRT
    OP.findButtonInMyComputer(OP.OTRT)
    pag.click()
    #нажимаем кнопку сделать фото
    OP.findButtonInMyComputer(OP.take_photo)
    pag.click()
    #нопка сделать документ
    OP.findButtonInMyComputer(OP.document_photo)
    pag.click()
    time.sleep(3)
    #принять
    OP.findButtonInMyComputer(OP.OKTRT)
    pag.click()
    #применить
    OP.findButtonInMyComputer(OP.prymenit)
    pag.click()
    time.sleep(1)
    #распознать текст
    OP.findButtonInMyComputer(OP.find_textTRT)
    pag.click()
    #Закрыть
    OP.findButtonInMyComputer(OP.closeTRT)
    pag.click()
    #добавить в буфер обмена
    OP.findButtonInMyComputer(OP.addTRT)
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

    OMCList.appendleft(s[5])

    print(OMCList)
    #Пишем номер ОМС
    writeOMC(s[5])
    keyboard.keyboardTap(KP.ENTER)






