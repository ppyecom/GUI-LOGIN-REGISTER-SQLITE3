
import sys
from PyQt5 import *
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PySide2 import *
from ui_wlog import *
from ui_wreg import *
from Interfaz_de_trabajo1 import *
import sqlite3


class window_login(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui=Ui_log()
        self.ui.setupUi(self)
        #ELIMINAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        #TRANSPARENTE
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.passLine.setEchoMode(QLineEdit.Password)
        self.ui.logButton.clicked.connect(self.funcionlogin)
        self.ui.regButton.clicked.connect(self.gotoregister)
        self.ui.exitLog.clicked.connect(self.salirlog)

    def salirlog(self):
        sys.exit()

    def gotoregister(self):
        #CERRAR VENTANA
        self.hide()
        #ABRIR VENTANA DE REGISTRO
        self.regis=window_register()
        self.regis.show()

    

    def funcionlogin(self):

        global user

        user=self.ui.usuLine.text()
        password=self.ui.passLine.text()

        if len(user)==0 or len(password)==0:
            self.ui.error.setText("Ingrese Dato")

        else:
            conn=sqlite3.connect("usu.db")
            cur=conn.cursor()
            cur.execute('SELECT * FROM registro_info WHERE username=? AND password=?',(user,password))
            if cur.fetchall():
                #CERRAR VENTANA
                self.hide()
                #ABRIR VENTANA DE ENTRADA
                self.ent=login_entrada()
                self.ent.show()

            else:
                self.ui.error.setText("Usuario y/o Contraseña incorrecta")


class window_register(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.re=Ui_reg()
        self.re.setupUi(self)
        #ELIMINAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        #TRANSPARENTE
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.re.passRe.setEchoMode(QLineEdit.Password)
        self.re.regisBRe.clicked.connect(self.funcionRegistrar)
        self.re.back.clicked.connect(self.retroceder)

    def retroceder(self):
        self.hide()
        self.wind1=window_login()
        self.wind1.show()

    def funcionRegistrar(self):
        name=self.re.nombreRe.text()
        ape=self.re.apeRe.text()
        fecha=self.re.fechaRe.text()
        telef=self.re.telefonoRe.text()
        correo=self.re.correoRe.text()
        user=self.re.userRe.text()
        password=self.re.passRe.text()

        if len(name)==0 or len(ape)==0 or len(fecha)==0 or len(telef)==0 or len(correo)==0 or len(user)==0 or len(password)==0:
            self.re.errorre.setText("Escriba Datos")
        else:
            conn=sqlite3.connect("usu.db")
            cur=conn.cursor()
            cur.execute('SELECT * FROM registro_info WHERE email=? OR username=?',(correo,user))
            if cur.fetchall():
                self.re.errorre.setText("Email o Username ya existen.")
            else:
                usuarios_reg=[name, ape, fecha, telef, correo, user, password]
                cur.execute('INSERT INTO registro_info (name, apell, fecha, telefono, email, username, password) VALUES (?,?,?,?,?,?,?)', usuarios_reg)
                conn.commit()
                conn.close()
                #CERRAR VENTANA
                self.hide()
                #REGRESO
                self.inicio=window_login()
                self.inicio.show()

class login_entrada(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.entra=Ui_MainWindow()
        self.entra.setupUi(self)
        self.entra.label_4.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0000ff;\">{user}</span></p></body></html>")


            
#EXECUTE

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=window_login()
    window.show()
    sys.exit(app.exec_())
