'''
Created on 20/07/2013

@author: Charlie Medina
'''
import sys
from PyQt4 import QtGui  
from VentanaPrincipal import VentanaPrincipal

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    vPrincipal = VentanaPrincipal()
    vPrincipal.show()    
    sys.exit(app.exec_())