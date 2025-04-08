import time
from keyboard_emulator import keyboardTap, keyboardLongTap, Keyboard as KP
from mouse import mouseTap, Mouse as MP, mousePosition, mouseDoubleLKMTap
from find_button import FindButton as FB
from windows_control import WindowsControl as WC
from find_errors import FindErrors as FE
from find_refferal import FindRefferal as FR
from find_objects import FindObjects
from find_archimed_button import FindArchimedButton as FAB
from macros.lungs_macros import rOGKNorma
def archimedNorma():
 FAB.find(FAB.redaktirovanie)
 mouseTap(MP.LKM_MOUSE)
 time.sleep(1)
 FAB.find(FAB.zona_issledovania)
 mouseTap(MP.LKM_MOUSE)
 FAB.find(FAB.ellipsis)
 mouseTap(MP.LKM_MOUSE)
 FAB.find(template=FAB.plus_grud, operator_h=FindObjects.division, operator_w=FindObjects.division, w_value=5, h_value=1.2)
 mouseTap(MP.LKM_MOUSE)
 FAB.find(template=FAB.plus_grudnaya_polost, operator_h=FindObjects.division, operator_w=FindObjects.division, w_value=9, h_value=1.2)
 mouseTap(MP.LKM_MOUSE)
 FAB.find(FAB.rentgenografia_ogk)
 mouseTap(MP.LKM_MOUSE)
 FAB.find(FAB.shablons, operator_w=FindObjects.subtraction, w_value=15)
 mouseTap(MP.LKM_MOUSE)
 FAB.find(FAB.legkie_norma)
 mouseTap(MP.LKM_MOUSE)
 FAB.find(FAB.zapis_v_bd)
 mouseTap(MP.LKM_MOUSE)
 FAB.find(FAB.archimed_print)
 mouseTap(MP.LKM_MOUSE)
 FAB.find(FAB.archimed_patient, operator_w=FindObjects.addition, w_value=50)
 mouseTap(MP.LKM_MOUSE)
 mouseTap(MP.PKM_MOUSE)
 FAB.find(FAB.vydelit_vse)
 mouseTap(MP.LKM_MOUSE)
 keyboardLongTap(KP.LeftControl)
 keyboardTap(KP.C)
 FAB.find(FAB.exit_archimed)
 mouseTap(MP.LKM_MOUSE)
 keyboardTap(KP.ENTER)
 FAB.find(FAB.infoclinika_down_button, debug_mode=True)
 mouseTap(MP.LKM_MOUSE)
 time.sleep(1)
 FB.findWithTime(FAB.infoclinika_full_screen, timeWait=2)
 mouseTap(MP.LKM_MOUSE)
 time.sleep(1)
 FB.find(FB.searchMain, operator_w=FindObjects.subtraction, w_value=150  )  # находим поле поиска в инфоклинике
 mouseTap(MP.LKM_MOUSE)
 keyboardLongTap(KP.LeftControl)
 keyboardTap(KP.A)
 time.sleep(0.5)
 keyboardLongTap(KP.LeftControl)
 keyboardTap(KP.V)
 FB.find(FB.searchMain, operator_w=FindObjects.subtraction, w_value=85  )  # кнопка "фильтровать"
 mouseTap(MP.LKM_MOUSE)
 time.sleep(3)
 rOGKNorma()
 FB.find(FAB.svernut_infokliniku, debug_mode=True)
 mouseTap(MP.LKM_MOUSE)




