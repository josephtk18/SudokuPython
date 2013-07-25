# coding=utf-8

'''
Created on 20/07/2013

@author: Charlie Medina
'''

from PyQt4 import QtCore, QtGui 
from Ui_ventana_principal import Ui_Ventana_principal
import ctypes
 

class VentanaPrincipal(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ventana=Ui_Ventana_principal()
        self.ventana.setupUi(self)
        self.setWindowTitle("PySudoku")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        
        self.connect(self.ventana.Btn_Salir,QtCore.SIGNAL('clicked()'), self.salir)
        
    def salir(self):
        messageBox = ctypes.windll.user32.MessageBoxA        
        salir = messageBox(None,'Seguro que desea salir?', 'Salir', 0x40 | 0x1)
        if salir==1:
            messageBox(None,"Vuelva pronto", "Salir", 0)
            self.close()
