# coding=utf-8

'''
Created on 20/07/2013

@author: Charlie Medina
'''

from PyQt4 import QtCore, QtGui 
from Ui_ventana_principal import Ui_Ventana_principal
from VentanaJugar import VentanaJugar
from VentanaAyuda import VentanaAyuda
from VentanaAcercaDe import VentanaAcercaDe
import ctypes

 

class VentanaPrincipal(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ventana=Ui_Ventana_principal()
        self.ventana.setupUi(self)
        self.setWindowTitle("PySudoku")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.connect(self.ventana.Btn_Iniciar,QtCore.SIGNAL('clicked()'), self.iniciar_partida)
        #self.connect(self.ventana.Btn_estadisticas,QtCore.SIGNAL('clicked()'), self.estadisticas)
        self.connect(self.ventana.Btn_acercaDe,QtCore.SIGNAL('clicked()'), self.acercade)
        self.connect(self.ventana.Btn_Ayuda,QtCore.SIGNAL('clicked()'), self.ayuda)
        self.connect(self.ventana.Btn_Salir,QtCore.SIGNAL('clicked()'), self.salir)
    
    def iniciar_partida(self):        
        self.v = VentanaJugar()
        self.v.show()
        self.close() 
        
    def acercade(self):
        self.v = VentanaAcercaDe()
        self.v.show()
    
    def ayuda(self):
        self.v = VentanaAyuda()
        self.v.show()
            
    def salir(self):
        messageBox = ctypes.windll.user32.MessageBoxA        
        salir = messageBox(None,'Seguro que desea salir?', 'Salir', 0x40 | 0x1)
        if salir==1:
            messageBox(None,"Vuelva pronto", "Salir", 0)
            self.close()
