'''
Created on 20/07/2013

@author: Charlie Medina
'''
import sys
from PyQt4 import QtGui  
from VentanaPrincipal import VentanaPrincipal
from VentanaJugar import VentanaJugar


if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    vPrincipal = VentanaPrincipal()
    #pic = QtGui.QLabel(vPrincipal)
    #pic.setGeometry(10,10,400,100)
    #pic.setPixmap(QtGui.QPixmap("Imagenes/yingyangsudoku.jpg"))
    vPrincipal.show()
    sys.exit(app.exec_())