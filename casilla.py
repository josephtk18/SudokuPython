'''
Created on 03/08/2013

@author: Joseph Gallardo
'''

from PyQt4 import QtCore, QtGui 

class Casilla(QtGui.QLabel):

    def __init__(self,contenido,fila,columna,region):
        QtGui.QLabel.__init__(self)
        self.contenido=contenido
        self.fila=fila
        self.columna=columna
        self.region=region
        self.ocupada=True
        self.modificable=False
        self.setMinimumSize(50,50)
        self.setVisible(True)
        #QtGui.QLabel.setMinimumSize(50,50)
        #QtGui.QLabel.setVisible(True)
        
    '''def mousePressEvent(self):
        self.emit(QtCore.SIGNAL("clickedChange"),self)
     '''   
    def mousePressEvent(self, event):
        super(Casilla,self).mousePressEvent(event)
        self.emit(QtCore.SIGNAL("clickedChange"),self)
    
    def setGrafic(self,cont):
        if(cont==0):
            self.setPixmap(QtGui.QPixmap("Imagenes/0.jpg"))
            return
        if(cont==1):
            self.setPixmap(QtGui.QPixmap("Imagenes/1.jpg"))
            return
        if(cont==2):
            self.setPixmap(QtGui.QPixmap("Imagenes/2.jpg"))
            return
        if(cont==3):
            self.setPixmap(QtGui.QPixmap("Imagenes/3.jpg"))
            return
        if(cont==4):
            self.setPixmap(QtGui.QPixmap("Imagenes/4.jpg"))
            return
        if(cont==5):
            self.setPixmap(QtGui.QPixmap("Imagenes/5.jpg"))
            return
        if(cont==6):
            self.setPixmap(QtGui.QPixmap("Imagenes/6.jpg"))
            return
        if(cont==7):
            self.setPixmap(QtGui.QPixmap("Imagenes/7.jpg"))
            return
        if(cont==8):
            self.setPixmap(QtGui.QPixmap("Imagenes/8.jpg"))
            return
        if(cont==9):
            self.setPixmap(QtGui.QPixmap("Imagenes/9.jpg"))
            return
        
            
         
        
    def buscarRegion(self,f,c):
        if(f>=1 and f<=3):
            if(c>=1 and c<=3): return 1
            if(c>=4 and c<=6): return 2
            if(c>=6 and c<=9): return 3
        if(f>=4 and f<=6):
            if(c>=1 and c<=3): return 4
            if(c>=4 and c<=6): return 5
            if(c>=6 and c<=9): return 6
        if(f>=7 and f<=9):
            if(c>=1 and c<=3): return 7
            if(c>=4 and c<=6): return 8
            if(c>=6 and c<=9): return 9
            
    def setGrafic2(self,cont):
        if(cont==1):
            self.setPixmap(QtGui.QPixmap("Imagenes/ds1.jpg"))
            return
        if(cont==2):
            self.setPixmap(QtGui.QPixmap("Imagenes/ds2.jpg"))
            return
        if(cont==3):
            self.setPixmap(QtGui.QPixmap("Imagenes/ds3.jpg"))
            return
        if(cont==4):
            self.setPixmap(QtGui.QPixmap("Imagenes/ds4.jpg"))
            return
        if(cont==5):
            self.setPixmap(QtGui.QPixmap("Imagenes/ds5.jpg"))
            return
        if(cont==6):
            self.setPixmap(QtGui.QPixmap("Imagenes/ds6.jpg"))
            return
        if(cont==7):
            self.setPixmap(QtGui.QPixmap("Imagenes/ds7.jpg"))
            return
        if(cont==8):
            self.setPixmap(QtGui.QPixmap("Imagenes/ds8.jpg"))
            return
        if(cont==9):
            self.setPixmap(QtGui.QPixmap("Imagenes/ds9.jpg"))
            return
