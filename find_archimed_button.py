import numpy as np
import cv2 as cv
import time
from monitor_capture import MonitorCapture
from udp_client import sock, UDP_IP, UDP_PORT
from mouse import mouseTap, Mouse as MP, initialMousePosition, mousePosition, mouseDoubleLKMTap
from find_objects import FindObjects

class FindArchimedButton(FindObjects):
    # шаблоны кнопок
    redaktirovanie = cv.imread('images/archimed_buttons/redaktirovanie.png', 0)
    zona_issledovania = cv.imread('images/archimed_buttons/zonaIssledovania.png', 0)
    ellipsis = cv.imread('images/archimed_buttons/ellipsis.png', 0)
    plus_grud = cv.imread('images/archimed_buttons/plusGrud.png', 0)
    plus_grudnaya_polost = cv.imread('images/archimed_buttons/plusGrunayapolost.png', 0)
    rentgenografia_ogk = cv.imread('images/archimed_buttons/rentgenografia_ogk.png', 0)
    shablons = cv.imread('images/archimed_buttons/ArchimedShablon.png', 0)
    legkie_norma = cv.imread('images/archimed_buttons/legkieNorma.png', 0)
    zapis_v_bd = cv.imread('images/archimed_buttons/zapisVbd.png', 0)
    archimed_print = cv.imread('images/archimed_buttons/ArchimedPrint.png', 0)
    archimed_patient = cv.imread('images/archimed_buttons/archimedPatient.png', 0)
    vydelit_vse = cv.imread('images/archimed_buttons/vydelitVse.png', 0)
    infoclinika_down_button = cv.imread('images/archimed_buttons/infoclinikaDownButton.png', 0)
    exit_archimed = cv.imread('images/archimed_buttons/exitArchimed.png', 0)
    infoclinika_full_screen = cv.imread('images/archimed_buttons/infoklinikaFullScreen.png', 0)
    svernut_infokliniku = cv.imread('images/archimed_buttons/svernutInfokliniku.png', 0)
    number_patient = cv.imread('images/archimed_buttons/numberPatient.png', 0)
    current_date_time = cv.imread('images/archimed_buttons/currentDateTime.png', 0)
    birthsday = cv.imread('images/archimed_buttons/birthday.png', 0)