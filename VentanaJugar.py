'''
Created on 26/07/2013

@author: Charlie Medina
'''

from PyQt4 import QtCore, QtGui 
from Ui_ventana_jugar import Ui_Ventana_Jugar
import VentanaPrincipal
import Sudoku

class VentanaJugar(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ventana=Ui_Ventana_Jugar()
        self.ventana.setupUi(self)
        self.setWindowTitle("Iniciar Partida")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.connect(self.ventana.Btn_facil,QtCore.SIGNAL('clicked()'), self.facil)
        self.connect(self.ventana.Btn_normal,QtCore.SIGNAL('clicked()'), self.normal)
        self.connect(self.ventana.Btn_dificil,QtCore.SIGNAL('clicked()'), self.dificil)
        self.connect(self.ventana.Btn_cargar,QtCore.SIGNAL('clicked()'), self.cargar)
        self.connect(self.ventana.Btn_menu,QtCore.SIGNAL('clicked()'), self.regresar)
    
    def facil(self):
        self.v = Sudoku.Sudoku(1,False)
        self.v.show()
        self.close()
        
    def normal(self):
        self.v = Sudoku.Sudoku(2,False)
        self.v.show()
        self.close()
        
    def dificil(self):
        self.v = Sudoku.Sudoku(3,False)
        self.v.show()
        self.close()
        
    def cargar(self):
        self.v = Sudoku.Sudoku(0,True)
        self.v.show()
        self.close()
        
    def regresar(self):
        self.v = VentanaPrincipal.VentanaPrincipal()
        self.v.show()
        self.close() 
    