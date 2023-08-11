import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from find_errors import FindErrors as FE
from keyboard import keyboardTap, KeyboardPackagesUdp as KP
from find_button import FindButton as FB
from find_title import FindTitles as FT
from macros.backbone_macros import pop, shop
from macros.cranium_macros import craniumNorma
from macros.lungs_macros import rOGK, rOGKPrint, fluraEnd, fluraNorma, fluraNormaShort
from macros.joints_macros import hipsJoints, kneesJoints
from macros.macros import antiSleep, startIK, restartIK
from macros.ppn_macros import ppnNorma

from read_text import readText
from find_text import scan_text, writeText, writeOMC
from windows_control import WindowsControl as WC
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap

# antiSleep()
# writeOMC()
#startIK()
#writeText('рубцова Татьяна Владимировна')
#writeText('1')
#fluraNorma()
#fluraNormaShort()
#rOGKPrint()
#rOGK()
# kneesJoints()
# ppnNorma()
#pop(scolioz=True)
#craniumNorma()

shop()







'''
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Мой асисстент")
        self.setGeometry(0, 0, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Фамилия Имя Отчество")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("жми")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()


def main():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == "main":
    main()
'''
#main()
