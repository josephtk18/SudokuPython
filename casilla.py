'''
Created on 03/08/2013

@author: Joseph Gallardo
'''

from PyQt4 import QtCore, QtGui 

class Casilla(QtGui.QLabel):

    

    def __init__(self,contenido,fila,columna,region):
        self.contenido=contenido
        self.fila=fila
        self.columna=columna
        self.region=region
        self.ocupada=True
        self.modificable=False
        self.setGrafic(contenido)
        QtGui.QLabel.setMinimumSize(50,50)
        QtGui.QLabel.setVisible(True)
        
    
    def getContenido(self):
        return self.contenido
    def getFila(self):
        return self.fila
    def getColumna(self):
        return self.columna
    def getRegion(self):
        return self.region
    def isOcupada(self):
        return self.ocupada
    def isModificable(self):
        return self.modificable
    
    def setContenido(self,cont):
        self.contenido=cont
    def setFila(self,fila):
        self.fila=fila
    def setColumna(self,col):
        self.columna=col
    def setRegion(self,reg):
        self.region=reg
    def setOcupada(self,ocup):
        self.ocupada=ocup
    def setModificable(self,mod):
        self.modificable=mod
    
        
    
    def setGrafic(self,cont):
        {'0':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/0.jpg")),
         '1':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/1.jpg")),
         '2':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/2.jpg")),
         '3':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/3.jpg")),
         '4':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/4.jpg")),
         '5':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/5.jpg")),
         '6':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/6.jpg")),
         '7':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/7.jpg")),
         '8':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/8.jpg")),
         '9':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/9.jpg"))}[cont]
        
    def buscarRegion(self,f,c):
        if(f>=1 & f<=3):
            if(c>=1 & c<=3): return 1
            if(c>=4 & c<=6): return 2
            if(c>=6 & c<=9): return 3
        if(f>=4 & f<=6):
            if(c>=1 & c<=3): return 4
            if(c>=4 & c<=6): return 5
            if(c>=6 & c<=9): return 6
        if(f>=7 & f<=9):
            if(c>=1 & c<=3): return 7
            if(c>=4 & c<=6): return 8
            if(c>=6 & c<=9): return 9
            
    def setGrafic2(self,cont):
        {'0':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/ds0.jpg")),
         '1':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/ds1.jpg")),
         '2':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/ds2.jpg")),
         '3':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/ds3.jpg")),
         '4':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/ds4.jpg")),
         '5':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/ds5.jpg")),
         '6':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/ds6.jpg")),
         '7':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/ds7.jpg")),
         '8':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/ds8.jpg")),
         '9':QtGui.QLabel.setPixmap(QtGui.QPixmap("Imagenes/ds9.jpg"))}[cont]
    