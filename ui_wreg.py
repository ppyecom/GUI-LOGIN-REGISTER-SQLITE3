# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wregcCVuZL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_reg(object):
    def setupUi(self, reg):
        if not reg.objectName():
            reg.setObjectName(u"reg")
        reg.resize(441, 468)
        self.centralwidget = QWidget(reg)
        self.centralwidget.setObjectName(u"centralwidget")
        self.fondore = QLabel(self.centralwidget)
        self.fondore.setObjectName(u"fondore")
        self.fondore.setGeometry(QRect(80, 10, 281, 431))
        self.fondore.setStyleSheet(u"border-radius:25px")
        self.fondore.setPixmap(QPixmap(u"fond.jpg"))
        self.fondore.setScaledContents(True)
        self.nombreRe = QLineEdit(self.centralwidget)
        self.nombreRe.setObjectName(u"nombreRe")
        self.nombreRe.setGeometry(QRect(122, 79, 201, 21))
        self.nombreRe.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.nombreRe.setAlignment(Qt.AlignCenter)
        self.apeRe = QLineEdit(self.centralwidget)
        self.apeRe.setObjectName(u"apeRe")
        self.apeRe.setGeometry(QRect(122, 119, 201, 21))
        self.apeRe.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.apeRe.setAlignment(Qt.AlignCenter)
        self.telefonoRe = QLineEdit(self.centralwidget)
        self.telefonoRe.setObjectName(u"telefonoRe")
        self.telefonoRe.setGeometry(QRect(122, 199, 201, 21))
        self.telefonoRe.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.telefonoRe.setAlignment(Qt.AlignCenter)
        self.correoRe = QLineEdit(self.centralwidget)
        self.correoRe.setObjectName(u"correoRe")
        self.correoRe.setGeometry(QRect(122, 249, 201, 21))
        self.correoRe.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.correoRe.setAlignment(Qt.AlignCenter)
        self.userRe = QLineEdit(self.centralwidget)
        self.userRe.setObjectName(u"userRe")
        self.userRe.setGeometry(QRect(122, 289, 201, 21))
        self.userRe.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.userRe.setAlignment(Qt.AlignCenter)
        self.passRe = QLineEdit(self.centralwidget)
        self.passRe.setObjectName(u"passRe")
        self.passRe.setGeometry(QRect(120, 339, 201, 21))
        self.passRe.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.passRe.setAlignment(Qt.AlignCenter)
        self.titulore = QLabel(self.centralwidget)
        self.titulore.setObjectName(u"titulore")
        self.titulore.setGeometry(QRect(160, 10, 141, 61))
        self.titulore.setStyleSheet(u"font: 57 28pt \"Rhinos rocks\";")
        self.regisBRe = QPushButton(self.centralwidget)
        self.regisBRe.setObjectName(u"regisBRe")
        self.regisBRe.setGeometry(QRect(110, 390, 221, 31))
        self.regisBRe.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        self.errorre = QLabel(self.centralwidget)
        self.errorre.setObjectName(u"errorre")
        self.errorre.setGeometry(QRect(110, 370, 221, 20))
        self.errorre.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.fechaRe = QDateEdit(self.centralwidget)
        self.fechaRe.setObjectName(u"fechaRe")
        self.fechaRe.setGeometry(QRect(120, 160, 201, 22))
        self.fechaRe.setCursor(QCursor(Qt.PointingHandCursor))
        self.fechaRe.setMouseTracking(False)
        self.fechaRe.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.fechaRe.setWrapping(False)
        self.fechaRe.setAlignment(Qt.AlignCenter)
        self.fechaRe.setMaximumDate(QDate(2021, 1, 1))
        self.fechaRe.setMinimumDate(QDate(1970, 1, 1))
        self.fechaRe.setDate(QDate(2002, 1, 1))
        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(90, 20, 31, 31))
        self.back.setStyleSheet(u"QPushButton{\n"
"background-color: Transparent;\n"
"}")
        icon = QIcon()
        icon.addFile(u"atras2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back.setIcon(icon)
        self.back.setIconSize(QSize(25, 25))
        reg.setCentralWidget(self.centralwidget)

        self.retranslateUi(reg)

        QMetaObject.connectSlotsByName(reg)
    # setupUi

    def retranslateUi(self, reg):
        reg.setWindowTitle(QCoreApplication.translate("reg", u"MainWindow", None))
        self.fondore.setText("")
        self.nombreRe.setText("")
        self.nombreRe.setPlaceholderText(QCoreApplication.translate("reg", u"Nombre", None))
        self.apeRe.setPlaceholderText(QCoreApplication.translate("reg", u"Apellido", None))
        self.telefonoRe.setPlaceholderText(QCoreApplication.translate("reg", u"Telefono", None))
        self.correoRe.setPlaceholderText(QCoreApplication.translate("reg", u"Correo", None))
        self.userRe.setPlaceholderText(QCoreApplication.translate("reg", u"Username", None))
        self.passRe.setText("")
        self.passRe.setPlaceholderText(QCoreApplication.translate("reg", u"Password", None))
        self.titulore.setText(QCoreApplication.translate("reg", u"REGISTER", None))
        self.regisBRe.setText(QCoreApplication.translate("reg", u"Registrar", None))
        self.errorre.setText("")
#if QT_CONFIG(accessibility)
        self.fechaRe.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.fechaRe.setSpecialValueText("")
        self.back.setText("")
    # retranslateUi

