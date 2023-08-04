from tkinter import *

from find_button import FindButton as FB, FindButtonF8 as FBF8
from macros.lungs_macros import rOGK, rOGKPrint, fluraEnd, fluraStart
from macros.joints_macros import hipsJoints, kneesJoints
from macros.macros import antiSleep, startIK, restartIK

from read_text import readText
from find_text import scan_text, writeText, writeOMC

#antiSleep()
#writeOMC()
#startIK()
#writeText('огула михаил иосифович')
#fluraStart()
#fluraEnd()
#rOGK()
#kneesJoints()


#FB.find(FB.playButton)

FBF8.find(FBF8.F8Button, debug_mode=True)