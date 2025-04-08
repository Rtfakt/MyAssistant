import numpy as np
import cv2 as cv
import time
from monitor_capture import MonitorCapture
from udp_client import sock, UDP_IP, UDP_PORT
from mouse import mouseTap, Mouse as MP, initialMousePosition, mousePosition, mouseDoubleLKMTap
from find_objects import FindObjects



class FindDigiPaxButton(FindObjects):
    in_work = cv.imread('images/digi_pax_button/inWork.png', 0)
    protocol_issledovania = cv.imread('images/digi_pax_button/protocolIssledovania.png', 0)
    legkie_norma = cv.imread('images/digi_pax_button/legkieNorma.png', 0)
    podpisat = cv.imread('images/digi_pax_button/podpisat.png', 0)
    da = cv.imread('images/digi_pax_button/da.png', 0)
    podpisanoEP = cv.imread('images/digi_pax_button/podpisanoEP.png', 0)
    podpisanoEPOrganization = cv.imread('images/digi_pax_button/podpisanoEPOrganization.png', 0)
    dobavit_podpis_med_organization = cv.imread('images/digi_pax_button/dobavitPodpisMedOrganization.png', 0)
    nazad = cv.imread('images/digi_pax_button/nazad.png', 0)