'''
Created on 26/07/2013

@author: Charlie Medina
'''
import sys
from PyQt4 import QtGui 
from Ui_acercade import Ui_AcercaDe

class VentanaAcercaDe(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ventana=Ui_AcercaDe()
        self.ventana.setupUi(self)
        self.setWindowTitle("Acerca De")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        #self.connect(self.ventana.Btn_Salir,QtCore.SIGNAL('clicked()'), self.salir)