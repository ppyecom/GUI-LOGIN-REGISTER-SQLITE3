# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wlogUPFzgD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_log(object):
    def setupUi(self, log):
        if not log.objectName():
            log.setObjectName(u"log")
        log.resize(394, 464)
        log.setAutoFillBackground(False)
        self.centralwidget = QWidget(log)
        self.centralwidget.setObjectName(u"centralwidget")
        self.fondo = QLabel(self.centralwidget)
        self.fondo.setObjectName(u"fondo")
        self.fondo.setGeometry(QRect(70, 40, 271, 381))
        self.fondo.setStyleSheet(u"border-radius:8px;")
        self.fondo.setPixmap(QPixmap(u"fon.gif"))
        self.fondo.setScaledContents(True)
        self.usuLine = QLineEdit(self.centralwidget)
        self.usuLine.setObjectName(u"usuLine")
        self.usuLine.setGeometry(QRect(120, 180, 171, 31))
        self.usuLine.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.usuLine.setAlignment(Qt.AlignCenter)
        self.usuLine.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.passLine = QLineEdit(self.centralwidget)
        self.passLine.setObjectName(u"passLine")
        self.passLine.setGeometry(QRect(120, 240, 171, 31))
        self.passLine.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.passLine.setAlignment(Qt.AlignCenter)
        self.logButton = QPushButton(self.centralwidget)
        self.logButton.setObjectName(u"logButton")
        self.logButton.setGeometry(QRect(100, 300, 211, 31))
        self.logButton.setStyleSheet(u"QPushButton {\n"
"background-color: #ff5722;\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")
        self.regButton = QPushButton(self.centralwidget)
        self.regButton.setObjectName(u"regButton")
        self.regButton.setGeometry(QRect(100, 350, 211, 31))
        self.regButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 170, 0);\n"
"		border-radius: 4px;\n"
"		color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"\n"
"}")
        self.icono = QLabel(self.centralwidget)
        self.icono.setObjectName(u"icono")
        self.icono.setGeometry(QRect(160, 60, 91, 91))
        self.icono.setPixmap(QPixmap(u"icon.png"))
        self.icono.setScaledContents(True)
        self.error = QLabel(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(110, 280, 191, 20))
        self.error.setStyleSheet(u"color:#ffffff;")
        self.exitLog = QPushButton(self.centralwidget)
        self.exitLog.setObjectName(u"exitLog")
        self.exitLog.setGeometry(QRect(300, 50, 31, 31))
        self.exitLog.setStyleSheet(u"QPushButton{\n"
"background-color: Transparent;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgb(255, 0, 255);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitLog.setIcon(icon)
        self.exitLog.setIconSize(QSize(31, 31))
        log.setCentralWidget(self.centralwidget)

        self.retranslateUi(log)

        QMetaObject.connectSlotsByName(log)
    # setupUi

    def retranslateUi(self, log):
        log.setWindowTitle(QCoreApplication.translate("log", u"MainWindow", None))
        self.fondo.setText("")
        self.usuLine.setPlaceholderText(QCoreApplication.translate("log", u"Usuario", None))
        self.passLine.setPlaceholderText(QCoreApplication.translate("log", u"Password", None))
        self.logButton.setText(QCoreApplication.translate("log", u"Log in", None))
        self.regButton.setText(QCoreApplication.translate("log", u"Register", None))
        self.icono.setText("")
        self.error.setText("")
        self.exitLog.setText("")
    # retranslateUi

