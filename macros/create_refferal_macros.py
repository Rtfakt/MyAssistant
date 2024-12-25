from find_button import FindButton as FB
from mouse import mouseTap, Mouse as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap
from keyboard import keyboardTap, keyboardLongTap, Keyboard as KP
def create_referal():
    #Нажимаем
    FB.find(FB.plusButton, operator_w=FB.subtraction, w_value=60)
    mouseTap(MP.LKM_MOUSE)
    # смена языка на русский
    initialMousePosition()
    mousePosition(1780, 1060)
    mouseTap(MP.LKM_MOUSE)
    mousePosition(0, -180)
    mouseTap(MP.LKM_MOUSE)
    # фильтруем тип направления
    keyboardTap(KP.H)
    keyboardTap(KP.T)
    keyboardTap(KP.Y)
    keyboardTap(KP.N)
    keyboardTap(KP.U)
    # выбираем тип направления рентген
    keyboardTap(KP.F2)
    #кнопка внутреннее
    FB.find(FB.vnutrennee)
    mouseTap(MP.LKM_MOUSE)
    # кнопка с тремя точками
    FB.find(FB.threePointsButton)
    mouseTap(MP.LKM_MOUSE)
    # Диагноз МКБ
    keyboardTap(KP.Z)
    keyboardTap(KP.NUM0)
    keyboardTap(KP.NUM1)
    keyboardTap(KP.Ю)
    keyboardTap(KP.NUM8)
    keyboardTap(KP.ENTER)
    # кнопка plus Ins
    FB.find(FB.plusIns)
    mouseTap(MP.LKM_MOUSE)
    # вводим код услуги
    '''
    keyboardTap(KP.NUM7)
    keyboardTap(KP.Ю)
    keyboardTap(KP.NUM6)
    keyboardTap(KP.NUM1)
    keyboardTap(KP.Ю)
    keyboardTap(KP.NUM3)
    keyboardTap(KP.ENTER)
    '''
    #код услуги
    FB.find(FB.kodUslugi)
    mouseDoubleLKMTap()
    #поиск добавленной услуги
    #FB.find(FB.usluga)
    # сохранить
    keyboardTap(KP.F2)
    # сохранить
    keyboardTap(KP.F2)




