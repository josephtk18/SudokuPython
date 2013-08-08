'''
Created on 04/08/2013

@author: Joseph Gallardo
'''

from PyQt4 import QtCore,QtGui 

class Digito(QtGui.QLabel):
    
    def __init__(self,num):
        QtGui.QLabel.__init__(self)
        self.dig=num
        self.setMinimumSize(50,50)
        self.setGrafic(num)
        self.setVisible(True)
        
        
    def getDigito(self):
        return self.dig
    
    def setDigito(self,num):
        self.dig=num
    
    def mousePressEvent(self,event):
        super(Digito,self).mousePressEvent(event)
        self.emit(QtCore.SIGNAL("changeToSelect"),self)
        
    
    def setGrafic(self,cont):
        if(cont==1):
            self.setPixmap(QtGui.QPixmap("Imagenes/d1.jpg"))
            return
        if(cont==2):
            self.setPixmap(QtGui.QPixmap("Imagenes/d2.jpg"))
            return
        if(cont==3):
            self.setPixmap(QtGui.QPixmap("Imagenes/d3.jpg"))
            return
        if(cont==4):
            self.setPixmap(QtGui.QPixmap("Imagenes/d4.jpg"))
            return
        if(cont==5):
            self.setPixmap(QtGui.QPixmap("Imagenes/d5.jpg"))
            return
        if(cont==6):
            self.setPixmap(QtGui.QPixmap("Imagenes/d6.jpg"))
            return
        if(cont==7):
            self.setPixmap(QtGui.QPixmap("Imagenes/d7.jpg"))
            return
        if(cont==8):
            self.setPixmap(QtGui.QPixmap("Imagenes/d8.jpg"))
            return
        if(cont==9):
            self.setPixmap(QtGui.QPixmap("Imagenes/d9.jpg"))
            return