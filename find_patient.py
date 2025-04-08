from find_button import FindButton as FB
from keyboard_emulator import keyboardTap, Keyboard as KP
from write_text import writeText
from mouse import mouseTap, Mouse as MP, mousePosition, mouseDoubleLKMTap


PatientDict = {}

i = 0
def find_patient(dict):# Находит пациента по ФИО и дате рождения
    fioList = list(dict.keys())
    dateList = list(dict.values())
    while i < len(fioList):
      keyboardTap(KP.F10)
      fio = fioList.pop(0)
      #print(fio)
      FB.find(FB.familyField)
      writeText(fio)
      birth = dateList.pop(0)
      FB.find(FB.birthField)
      mouseTap(MP.LKM_MOUSE)
      writeText(birth)
      #print(birth)
      FB.find(FB.prodolgitButton)
      mouseTap(MP.LKM_MOUSE)




