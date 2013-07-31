'''
Created on 26/07/2013

@author: Charlie Medina
'''

from PyQt4 import QtCore, QtGui 
from Ui_ventana_jugar import Ui_Ventana_Jugar
import VentanaPrincipal

class VentanaJugar(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ventana=Ui_Ventana_Jugar()
        self.ventana.setupUi(self)
        self.setWindowTitle("Iniciar Partida")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        #self.connect(self.ventana.Btn_facil,QtCore.SIGNAL('clicked()'), self.facil)
        #self.connect(self.ventana.Btn_normal,QtCore.SIGNAL('clicked()'), self.facil)
        #self.connect(self.ventana.Btn_dificil,QtCore.SIGNAL('clicked()'), self.facil)
        #self.connect(self.ventana.Btn_cargar,QtCore.SIGNAL('clicked()'), self.facil)
        self.connect(self.ventana.Btn_menu,QtCore.SIGNAL('clicked()'), self.regresar)

    def regresar(self):
        self.v = VentanaPrincipal.VentanaPrincipal()
        self.v.show()
        self.close() 
    