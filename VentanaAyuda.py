'''
Created on 26/07/2013

@author: Charlie Medina
'''

from PyQt4 import QtGui 
from Ui_ayuda import Ui_Ayuda

class VentanaAyuda(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ventana=Ui_Ayuda()
        self.ventana.setupUi(self)
        self.setWindowTitle("Ayuda")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
