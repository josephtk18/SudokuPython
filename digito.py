'''
Created on 04/08/2013

@author: Joseph Gallardo
'''

from PyQt4 import QtCore, QtGui 

class Digito(QtGui.QLabel):
    

    def __init__(self,num):
        self.dig=num
        QtGui.QLabel.setMinimumSize(50,50)
        QtGui.QLabel.setVisible(True)
        
        
    def getDigito(self):
        return self.dig
    
    def setDigito(self,num):
        self.dig=num
    
    def setGrafic(self,cont):
        {'1':QtGui.QLabel.setPixmap(QtGui.QPixmap(":/Imagenes/d1.jpg")),
         '2':QtGui.QLabel.setPixmap(QtGui.QPixmap(":/Imagenes/d2.jpg")),
         '3':QtGui.QLabel.setPixmap(QtGui.QPixmap(":/Imagenes/d3.jpg")),
         '4':QtGui.QLabel.setPixmap(QtGui.QPixmap(":/Imagenes/d4.jpg")),
         '5':QtGui.QLabel.setPixmap(QtGui.QPixmap(":/Imagenes/d5.jpg")),
         '6':QtGui.QLabel.setPixmap(QtGui.QPixmap(":/Imagenes/d6.jpg")),
         '7':QtGui.QLabel.setPixmap(QtGui.QPixmap(":/Imagenes/d7.jpg")),
         '8':QtGui.QLabel.setPixmap(QtGui.QPixmap(":/Imagenes/d8.jpg")),
         '9':QtGui.QLabel.setPixmap(QtGui.QPixmap(":/Imagenes/d9.jpg"))}[cont]