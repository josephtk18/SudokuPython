'''
Created on 26/07/2013

@author: Charlie Medina
'''
import sys
from PyQt4 import QtGui 
from Ui_ventana_jugar import Ui_Ventana_Jugar

class VentanaJugar(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ventana=Ui_Ventana_Jugar()
        self.ventana.setupUi(self)
        self.setWindowTitle("Iniciar Partida")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        #self.connect(self.ventana.Btn_Salir,QtCore.SIGNAL('clicked()'), self.salir)