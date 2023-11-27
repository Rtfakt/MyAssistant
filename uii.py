import sys
import time
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
import sys


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

from open_programs import readText
from filter_text import scan_text, writeText, writeOMC, OMCdata, first_name_data, last_name_data, middle_name_data, birth_date_data
from windows_control import WindowsControl as WC
from mouse import mouseTap, MousePackagesUdp as MP, mousePosition, initialMousePosition, mouseDoubleLKMTap

#antiSleep()
#writeOMC()
#startIK()
#writeText('Матвиенко Ольга Николаевна')
#writeText('1')
#fluraNorma()
#fluraNormaShort()
#rOGKPrint()
#rOGK()
# kneesJoints()
# ppnNorma()
#pop()
#craniumNorma()

#shop()




# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 800)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.family_text = QtWidgets.QLabel(self.centralwidget)
        self.family_text.setGeometry(QtCore.QRect(0, 40, 260, 50))
        self.family_text.setTextFormat(QtCore.Qt.RichText)
        self.family_text.setObjectName("family")
        self.name_text = QtWidgets.QLabel(self.centralwidget)
        self.name_text.setGeometry(QtCore.QRect(240, 40, 260, 50))
        self.name_text.setTextFormat(QtCore.Qt.RichText)
        self.name_text.setObjectName("name")
        self.middle_name_text = QtWidgets.QLabel(self.centralwidget)
        self.middle_name_text.setGeometry(QtCore.QRect(510, 40, 260, 50))
        self.middle_name_text.setTextFormat(QtCore.Qt.RichText)
        self.middle_name_text.setObjectName("middle_name")
        self.birth_date_text = QtWidgets.QLabel(self.centralwidget)
        self.birth_date_text.setGeometry(QtCore.QRect(800, 40, 260, 50))
        self.birth_date_text.setTextFormat(QtCore.Qt.RichText)
        self.birth_date_text.setObjectName("birth_date")
        self.DOA_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.DOA_2.setGeometry(QtCore.QRect(0, 100, 1121, 671))
        self.DOA_2.setObjectName("DOA_2")
        self.OGK_tab = QtWidgets.QWidget()
        self.OGK_tab.setObjectName("OGK_tab")
        self.OGKButton = QtWidgets.QPushButton(self.OGK_tab)
        self.OGKButton.setGeometry(QtCore.QRect(0, 20, 149, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.OGKButton.setPalette(palette)
        self.OGKButton.setObjectName("OGKButton")
        self.pushButton_fluraNorma = QtWidgets.QPushButton(self.OGK_tab)
        self.pushButton_fluraNorma.setGeometry(QtCore.QRect(420, 20, 201, 40))
        self.pushButton_fluraNorma.setObjectName("pushButton_fluraNorma")
        self.pushButton_fluraNormaShort = QtWidgets.QPushButton(self.OGK_tab)
        self.pushButton_fluraNormaShort.setGeometry(QtCore.QRect(650, 20, 281, 40))
        self.pushButton_fluraNormaShort.setObjectName("pushButton_fluraNormaShort")
        self.pushButton_TBCExodus = QtWidgets.QPushButton(self.OGK_tab)
        self.pushButton_TBCExodus.setGeometry(QtCore.QRect(0, 100, 361, 40))
        self.pushButton_TBCExodus.setObjectName("pushButton_TBCExodus")
        self.pushButton_TBCExodusRight = QtWidgets.QPushButton(self.OGK_tab)
        self.pushButton_TBCExodusRight.setGeometry(QtCore.QRect(370, 100, 291, 40))
        self.pushButton_TBCExodusRight.setObjectName("pushButton_TBCExodusRight")
        self.pushButton_TBCExodusRight_2 = QtWidgets.QPushButton(self.OGK_tab)
        self.pushButton_TBCExodusRight_2.setGeometry(QtCore.QRect(670, 100, 271, 40))
        self.pushButton_TBCExodusRight_2.setObjectName("pushButton_TBCExodusRight_2")
        self.OGKButton_OGKprint = QtWidgets.QPushButton(self.OGK_tab)
        self.OGKButton_OGKprint.setGeometry(QtCore.QRect(180, 20, 191, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.OGKButton_OGKprint.setPalette(palette)
        self.OGKButton_OGKprint.setObjectName("OGKButton_OGKprint")
        self.DOA_2.addTab(self.OGK_tab, "")
        self.joint_tab = QtWidgets.QWidget()
        self.joint_tab.setObjectName("joint_tab")
        self.DOA = QtWidgets.QGroupBox(self.joint_tab)
        self.DOA.setGeometry(QtCore.QRect(0, 10, 211, 221))
        self.DOA.setObjectName("DOA")
        self.pushButton_DOAHips = QtWidgets.QPushButton(self.DOA)
        self.pushButton_DOAHips.setGeometry(QtCore.QRect(0, 180, 211, 40))
        self.pushButton_DOAHips.setObjectName("pushButton_DOAHips")
        self.radioButton_rightHips = QtWidgets.QRadioButton(self.DOA)
        self.radioButton_rightHips.setGeometry(QtCore.QRect(20, 20, 91, 17))
        self.radioButton_rightHips.setObjectName("radioButton_rightHips")
        self.radioButton_leftHips = QtWidgets.QRadioButton(self.DOA)
        self.radioButton_leftHips.setGeometry(QtCore.QRect(20, 40, 91, 17))
        self.radioButton_leftHips.setObjectName("radioButton_leftHips")
        self.radioButton__rightLeftHips = QtWidgets.QRadioButton(self.DOA)
        self.radioButton__rightLeftHips.setGeometry(QtCore.QRect(20, 60, 171, 17))
        self.radioButton__rightLeftHips.setObjectName("radioButton__rightLeftHips")
        self.checkBox_Hips1 = QtWidgets.QCheckBox(self.DOA)
        self.checkBox_Hips1.setGeometry(QtCore.QRect(20, 100, 70, 17))
        self.checkBox_Hips1.setObjectName("checkBox_Hips1")
        self.checkBox_Hips2 = QtWidgets.QCheckBox(self.DOA)
        self.checkBox_Hips2.setGeometry(QtCore.QRect(20, 120, 70, 17))
        self.checkBox_Hips2.setObjectName("checkBox_Hips2")
        self.checkBox_Hips3 = QtWidgets.QCheckBox(self.DOA)
        self.checkBox_Hips3.setGeometry(QtCore.QRect(20, 140, 70, 17))
        self.checkBox_Hips3.setObjectName("checkBox_Hips3")
        self.checkBox_Hips4 = QtWidgets.QCheckBox(self.DOA)
        self.checkBox_Hips4.setGeometry(QtCore.QRect(20, 160, 70, 17))
        self.checkBox_Hips4.setObjectName("checkBox_Hips4")
        self.DOA_3 = QtWidgets.QGroupBox(self.joint_tab)
        self.DOA_3.setGeometry(QtCore.QRect(220, 10, 211, 221))
        self.DOA_3.setObjectName("DOA_3")
        self.pushButton_DOAKnees = QtWidgets.QPushButton(self.DOA_3)
        self.pushButton_DOAKnees.setGeometry(QtCore.QRect(0, 180, 211, 40))
        self.pushButton_DOAKnees.setObjectName("pushButton_DOAKnees")
        self.radioButton_rightKnee = QtWidgets.QRadioButton(self.DOA_3)
        self.radioButton_rightKnee.setGeometry(QtCore.QRect(20, 20, 91, 17))
        self.radioButton_rightKnee.setObjectName("radioButton_rightKnee")
        self.radioButton_LeftKnee = QtWidgets.QRadioButton(self.DOA_3)
        self.radioButton_LeftKnee.setGeometry(QtCore.QRect(20, 40, 91, 17))
        self.radioButton_LeftKnee.setObjectName("radioButton_LeftKnee")
        self.radioButton_rightLeftKnees = QtWidgets.QRadioButton(self.DOA_3)
        self.radioButton_rightLeftKnees.setGeometry(QtCore.QRect(20, 60, 171, 17))
        self.radioButton_rightLeftKnees.setObjectName("radioButton_rightLeftKnees")
        self.checkBox_knees1 = QtWidgets.QCheckBox(self.DOA_3)
        self.checkBox_knees1.setGeometry(QtCore.QRect(20, 100, 70, 17))
        self.checkBox_knees1.setObjectName("checkBox_knees1")
        self.checkBox_knees2 = QtWidgets.QCheckBox(self.DOA_3)
        self.checkBox_knees2.setGeometry(QtCore.QRect(20, 120, 70, 17))
        self.checkBox_knees2.setObjectName("checkBox_knees2")
        self.checkBox_knees3 = QtWidgets.QCheckBox(self.DOA_3)
        self.checkBox_knees3.setGeometry(QtCore.QRect(20, 140, 70, 17))
        self.checkBox_knees3.setObjectName("checkBox_knees3")
        self.checkBox_knees4 = QtWidgets.QCheckBox(self.DOA_3)
        self.checkBox_knees4.setGeometry(QtCore.QRect(20, 160, 70, 17))
        self.checkBox_knees4.setObjectName("checkBox_knees4")
        self.DOA_2.addTab(self.joint_tab, "")
        self.backbone_tab = QtWidgets.QWidget()
        self.backbone_tab.setObjectName("backbone_tab")
        self.pushButton_shopOX = QtWidgets.QPushButton(self.backbone_tab)
        self.pushButton_shopOX.setGeometry(QtCore.QRect(20, 30, 201, 40))
        self.pushButton_shopOX.setObjectName("pushButton_shopOX")
        self.pushButton_gopOX = QtWidgets.QPushButton(self.backbone_tab)
        self.pushButton_gopOX.setGeometry(QtCore.QRect(270, 30, 201, 40))
        self.pushButton_gopOX.setObjectName("pushButton_gopOX")
        self.pushButton_popOX = QtWidgets.QPushButton(self.backbone_tab)
        self.pushButton_popOX.setGeometry(QtCore.QRect(520, 30, 191, 40))
        self.pushButton_popOX.setObjectName("pushButton_popOX")
        self.pushButton_shopGopOX = QtWidgets.QPushButton(self.backbone_tab)
        self.pushButton_shopGopOX.setGeometry(QtCore.QRect(20, 110, 221, 40))
        self.pushButton_shopGopOX.setObjectName("pushButton_shopGopOX")
        self.pushButton_GopPopOX = QtWidgets.QPushButton(self.backbone_tab)
        self.pushButton_GopPopOX.setGeometry(QtCore.QRect(310, 110, 221, 40))
        self.pushButton_GopPopOX.setObjectName("pushButton_GopPopOX")
        self.DOA_2.addTab(self.backbone_tab, "")
        self.cranium_ppn_tab = QtWidgets.QWidget()
        self.cranium_ppn_tab.setObjectName("cranium_ppn_tab")
        self.pushButton_craniumNorma = QtWidgets.QPushButton(self.cranium_ppn_tab)
        self.pushButton_craniumNorma.setGeometry(QtCore.QRect(10, 10, 149, 40))
        self.pushButton_craniumNorma.setObjectName("pushButton_craniumNorma")
        self.pushButton_ppnNorma = QtWidgets.QPushButton(self.cranium_ppn_tab)
        self.pushButton_ppnNorma.setGeometry(QtCore.QRect(190, 10, 149, 40))
        self.pushButton_ppnNorma.setObjectName("pushButton_ppnNorma")
        self.pushButton_ppnSinusitRight = QtWidgets.QPushButton(self.cranium_ppn_tab)
        self.pushButton_ppnSinusitRight.setGeometry(QtCore.QRect(370, 10, 149, 40))
        self.pushButton_ppnSinusitRight.setObjectName("pushButton_ppnSinusitRight")
        self.pushButton_ppnSinusitLeft = QtWidgets.QPushButton(self.cranium_ppn_tab)
        self.pushButton_ppnSinusitLeft.setGeometry(QtCore.QRect(540, 10, 149, 40))
        self.pushButton_ppnSinusitLeft.setObjectName("pushButton_ppnSinusitLeft")
        self.pushButton_ppnSinusitRightLeft = QtWidgets.QPushButton(self.cranium_ppn_tab)
        self.pushButton_ppnSinusitRightLeft.setGeometry(QtCore.QRect(710, 10, 221, 40))
        self.pushButton_ppnSinusitRightLeft.setObjectName("pushButton_ppnSinusitRightLeft")
        self.DOA_2.addTab(self.cranium_ppn_tab, "")
        self.double_shablon_tab = QtWidgets.QWidget()
        self.double_shablon_tab.setObjectName("double_shablon_tab")
        self.DOA_2.addTab(self.double_shablon_tab, "")
        self.trauma_tab = QtWidgets.QWidget()
        self.trauma_tab.setObjectName("trauma_tab")
        self.pushButton_13 = QtWidgets.QPushButton(self.trauma_tab)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 20, 391, 40))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.trauma_tab)
        self.pushButton_14.setGeometry(QtCore.QRect(470, 20, 391, 40))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_BonesNorma = QtWidgets.QPushButton(self.trauma_tab)
        self.pushButton_BonesNorma.setGeometry(QtCore.QRect(20, 100, 391, 40))
        self.pushButton_BonesNorma.setObjectName("pushButton_BonesNorma")
        self.DOA_2.addTab(self.trauma_tab, "")
        self.mammography_tab = QtWidgets.QWidget()
        self.mammography_tab.setObjectName("mammography_tab")
        self.DOA_2.addTab(self.mammography_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButtonOBP = QtWidgets.QPushButton(self.tab)
        self.pushButtonOBP.setGeometry(QtCore.QRect(10, 10, 149, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButtonOBP.setPalette(palette)
        self.pushButtonOBP.setObjectName("pushButtonOBP")
        self.DOA_2.addTab(self.tab, "")
        self.OMC_text = QtWidgets.QLabel(self.centralwidget)
        self.OMC_text.setGeometry(QtCore.QRect(0, 0, 307, 49))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.OMC_text.setFont(font)
        self.OMC_text.setTextFormat(QtCore.Qt.RichText)
        self.OMC_text.setObjectName("OMC_number")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(310, 0, 619, 49))
        self.status.setObjectName("status")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.start_IK_Butt = QtWidgets.QAction(MainWindow)
        self.start_IK_Butt.setObjectName("start_IK_Butt")
        self.start_IK_Butt.triggered.connect(lambda: startIK())
        self.restart_IK_butt = QtWidgets.QAction(MainWindow)
        self.restart_IK_butt.setObjectName("restart_IK_butt")
        self.restart_IK_butt.triggered.connect(lambda: restartIK())
        self.menu.addSeparator()
        self.menu.addSeparator()
        self.menu.addAction(self.start_IK_Butt)
        self.menu.addAction(self.restart_IK_butt)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.DOA_2.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мой асисстент"))
        self.family_text.setText(_translate("MainWindow", "Фамилия"))
        self.family_text.setText(last_name_data)
        self.family_text.adjustSize()
        self.name_text.setText(_translate("MainWindow", "имя"))
        self.name_text.setText(first_name_data)
        self.name_text.adjustSize()
        self.middle_name_text.setText(_translate("MainWindow", "Отчество"))
        self.middle_name_text.setText(middle_name_data)
        self.middle_name_text.adjustSize()
        self.birth_date_text.setText(_translate("MainWindow", "Дата рождения"))
        self.birth_date_text.setText(birth_date_data)
        self.birth_date_text.adjustSize()
        self.OGKButton.setText(_translate("MainWindow", "ОГК норма"))
        self.pushButton_fluraNorma.setText(_translate("MainWindow", "Флюорография норма"))
        self.pushButton_fluraNormaShort.setText(_translate("MainWindow", "Флюорография норма \"короткая\""))
        self.pushButton_TBCExodus.setText(_translate("MainWindow", "Исход TBC в плотные очаги справа и слева"))
        self.pushButton_TBCExodusRight.setText(_translate("MainWindow", "Исход TBC в плотные очаги справа "))
        self.pushButton_TBCExodusRight_2.setText(_translate("MainWindow", "Исход TBC в плотные очаги слева"))
        self.OGKButton_OGKprint.setText(_translate("MainWindow", "ОГК норма(Печать)"))
        self.DOA_2.setTabText(self.DOA_2.indexOf(self.OGK_tab), _translate("MainWindow", "ОГК"))
        self.DOA.setTitle(_translate("MainWindow", "ДОА т/б сустава"))
        self.pushButton_DOAHips.setText(_translate("MainWindow", "ДОА Т/б сустава"))
        self.radioButton_rightHips.setText(_translate("MainWindow", "правого"))
        self.radioButton_leftHips.setText(_translate("MainWindow", "левого"))
        self.radioButton__rightLeftHips.setText(_translate("MainWindow", "правого и левого"))
        self.checkBox_Hips1.setText(_translate("MainWindow", "ст.1"))
        self.checkBox_Hips2.setText(_translate("MainWindow", "ст.2"))
        self.checkBox_Hips3.setText(_translate("MainWindow", "ст.3"))
        self.checkBox_Hips4.setText(_translate("MainWindow", "ст.4"))
        self.DOA_3.setTitle(_translate("MainWindow", "ДОА коленного сустава"))
        self.pushButton_DOAKnees.setText(_translate("MainWindow", "ДОА коленного сустава"))
        self.radioButton_rightKnee.setText(_translate("MainWindow", "правого"))
        self.radioButton_LeftKnee.setText(_translate("MainWindow", "левого"))
        self.radioButton_rightLeftKnees.setText(_translate("MainWindow", "правого и левого"))
        self.checkBox_knees1.setText(_translate("MainWindow", "ст.1"))
        self.checkBox_knees2.setText(_translate("MainWindow", "ст.2"))
        self.checkBox_knees3.setText(_translate("MainWindow", "ст.3"))
        self.checkBox_knees4.setText(_translate("MainWindow", "ст.4"))
        self.DOA_2.setTabText(self.DOA_2.indexOf(self.joint_tab), _translate("MainWindow", "Суставы, кости"))
        self.pushButton_shopOX.setText(_translate("MainWindow", "ШОП остеохондроз"))
        self.pushButton_gopOX.setText(_translate("MainWindow", "ГОП Остеохондроз"))
        self.pushButton_popOX.setText(_translate("MainWindow", "ПОП Остеохондроз"))
        self.pushButton_shopGopOX.setText(_translate("MainWindow", "ШОП и ГОП Остеохондроз"))
        self.pushButton_GopPopOX.setText(_translate("MainWindow", "ГОП и ПОП Остеохондроз"))
        self.DOA_2.setTabText(self.DOA_2.indexOf(self.backbone_tab), _translate("MainWindow", "Позвоночник"))
        self.pushButton_craniumNorma.setText(_translate("MainWindow", "Череп норма"))
        self.pushButton_ppnNorma.setText(_translate("MainWindow", "ППН норма"))
        self.pushButton_ppnSinusitRight.setText(_translate("MainWindow", "синусит справа"))
        self.pushButton_ppnSinusitLeft.setText(_translate("MainWindow", "синусит слева"))
        self.pushButton_ppnSinusitRightLeft.setText(_translate("MainWindow", "синусит справа и слева"))
        self.DOA_2.setTabText(self.DOA_2.indexOf(self.cranium_ppn_tab), _translate("MainWindow", "Череп, Пазухи"))
        self.DOA_2.setTabText(self.DOA_2.indexOf(self.double_shablon_tab), _translate("MainWindow", "Двойные шаблоны"))
        self.pushButton_13.setText(_translate("MainWindow", "перелом левой/л кости в типичном месте"))
        self.pushButton_14.setText(_translate("MainWindow", "перелом правой/л кости в типичном месте"))
        self.pushButton_BonesNorma.setText(_translate("MainWindow", "без видимой костной патологии"))
        self.DOA_2.setTabText(self.DOA_2.indexOf(self.trauma_tab), _translate("MainWindow", "Травмы"))
        self.DOA_2.setTabText(self.DOA_2.indexOf(self.mammography_tab), _translate("MainWindow", "Маммография"))
        self.pushButtonOBP.setText(_translate("MainWindow", "Живот норма"))
        self.DOA_2.setTabText(self.DOA_2.indexOf(self.tab), _translate("MainWindow", "Живот"))
        self.OMC_text.setText(_translate("MainWindow", "Номер полиса"))
        self.OMC_text.setText(OMCdata)
        self.OMC_text.adjustSize()



        self.status.setText(_translate("MainWindow", "Статус - не выполнено"))
        self.menu.setTitle(_translate("MainWindow", "инфоклиника"))
        self.start_IK_Butt.setText(_translate("MainWindow", "запустить инфоклинику"))
        self.restart_IK_butt.setText(_translate("MainWindow", "перезапустить инфоклинику"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())