'''
Created on 04/08/2013

@author: Charlie Medina
'''
from PyQt4 import QtCore, QtGui 
from Ui_sudoku import Ui_Sudoku
import Tablero
import digito
import random
#import VentanaPrincipal

class Sudoku(QtGui.QMainWindow):

    def __init__(self,nivel,cargar):
        QtGui.QMainWindow.__init__(self)
        self.ventana=Ui_Sudoku()
        self.ventana.setupUi(self)
        self.setWindowTitle("Sudoku")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        
        if(cargar==False):
            self.nombre = QtGui.QInputDialog.getText(self, 'Juego Nuevo', 'Ingrese el nombre del jugador:')
        
        self.t=Tablero.Tablero()
        self.inicializarMatriz()
        self.iniciarTeclado()
        self.t.generarTablero()
        self.pasarTableroAMatriz(self.t.casillas)
        self.inicializarTablasUI(self.t.casillas)
        self.ocultarCasillas(nivel)
        #cargarPartida
        self.pasarMatrizAUI()
        
    def inicializarMatriz(self):
        for i in range(9):
            for j in range(9):
                self.matriz[i][j]=0
    
    def pasarTableroAMatriz(self,casillas):
        pos=0
        cas_tmp=casillas
        
        for i in range(9):
            for j in range(9):
                self.matriz[i][j]=cas_tmp.pop(pos)
                pos=pos+1
    
    def inicializarTablasUI(self,casillas):
        z=0
        cas_tmp=casillas
        for i in range(3):
            for j in range(3):
                self.ventana.bloque1.addWidget(cas_tmp.pop(z),i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.ventana.bloque2.addWidget(cas_tmp.pop(z),i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.ventana.bloque3.addWidget(cas_tmp.pop(z),i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.ventana.bloque4.addWidget(cas_tmp.pop(z),i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.ventana.bloque5.addWidget(cas_tmp.pop(z),i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.ventana.bloque6.addWidget(cas_tmp.pop(z),i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.ventana.bloque7.addWidget(cas_tmp.pop(z),i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.ventana.bloque8.addWidget(cas_tmp.pop(z),i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.ventana.bloque9.addWidget(cas_tmp.pop(z),i,j)
                z=z+1
    
    def pasarMatrizAUI(self):
        i1=0
        i2=0
        i3=0
        i4=0
        i5=0
        i6=0
        i7=0
        i8=0
        i9=0
        j1=0
        j2=0
        j3=0
        j4=0
        j5=0
        j6=0
        j7=0
        j8=0
        j9=0
        cas=Tablero.casilla.Casilla(0,0,0,0)
        for i in range(9):
            for j in range(9):
                region=cas.buscarRegion(i+1,j+1)
                if(region==1):
                    cas=self.ventana.bloque1.itemAtPosition(i1,j1)
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j1=j1+1
                    if(j1==3):
                        i1=i1+1
                        j1=0
                if(region==2):
                    cas=self.ventana.bloque2.itemAtPosition(i2,j2)
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j2=j2+1
                    if(j2==3):
                        i2=i2+1
                        j2=0
                if(region==3):
                    cas=self.ventana.bloque3.itemAtPosition(i3,j3)
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j3=j3+1
                    if(j3==3):
                        i3=i3+1
                        j3=0
                if(region==4):
                    cas=self.ventana.bloque4.itemAtPosition(i4,j4)
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j4=j4+1
                    if(j4==3):
                        i4=i4+1
                        j4=0
                if(region==5):
                    cas=self.ventana.bloque5.itemAtPosition(i5,j5)
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j5=j5+1
                    if(j5==3):
                        i5=i5+1
                        j5=0
                if(region==6):
                    cas=self.ventana.bloque6.itemAtPosition(i6,j6)
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j6=j6+1
                    if(j6==3):
                        i6=i6+1
                        j6=0
                if(region==7):
                    cas=self.ventana.bloque7.itemAtPosition(i7,j7)
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j7=j7+1
                    if(j7==3):
                        i7=i7+1
                        j7=0
                if(region==8):
                    cas=self.ventana.bloque8.itemAtPosition(i8,j8)
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j8=j8+1
                    if(j8==3):
                        i8=i8+1
                        j8=0
                if(region==9):
                    cas=self.ventana.bloque9.itemAtPosition(i9,j9)
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j9=j9+1
                    if(j9==3):
                        i9=i9+1
                        j9=0 
    
    def iniciarTeclado(self):
        for i in range(9):            
            self.teclado[i]=digito.Digito(i+1)
            self.ventana.gridTeclado.addItem(self.teclado[i])
    
    def ocultarCasillas(self,nivel):
        if(nivel==1): tmp=3
        if(nivel==2): tmp=5
        if(nivel==3): tmp=6
        cont=tmp
        bloque=1
        c = Tablero.casilla.Casilla(0,0,0,0) #instancia de casilla, para llamar metodo buscarRegion
        
        for bloque in range(10):
            while cont>0:
                for i in range(9):
                    for j in range(9):
                        if(cont>0):
                            if(c.buscarRegion(i+1,j+1)==bloque):
                                if(random.randint(0,1)==1):
                                    self.matriz[i][j]=0
                                    cont = cont-1
            cont=tmp    
    
    def pasarUIAMatriz(self):
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque1.itemAtPosition(i,j)
                cont = cas.contenido
                self.matriz[i][j]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque2.itemAtPosition(i,j)
                cont = cas.contenido
                self.matriz[i][j+3]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque3.itemAtPosition(i,j)
                cont = cas.contenido
                self.matriz[i][j+6]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque4.itemAtPosition(i,j)
                cont = cas.contenido
                self.matriz[i+3][j]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque5.itemAtPosition(i,j)
                cont = cas.contenido
                self.matriz[i+3][j+3]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque6.itemAtPosition(i,j)
                cont = cas.contenido
                self.matriz[i+3][j+6]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque7.itemAtPosition(i,j)
                cont = cas.contenido
                self.matriz[i+6][j]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque8.itemAtPosition(i,j)
                cont = cas.contenido
                self.matriz[i+6][j+3]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque9.itemAtPosition(i,j)
                cont = cas.contenido
                self.matriz[i+6][j+6]=cont
    
    def pasarMatrizAString(self):
        linea=""
        for i in range(9):
            for j in range(9):                
                linea+self.matriz[i][j]
                if(j==8): linea+"\n"
        return linea
    
    def pasarStringAMatriz(self,linea):
        for i in range(9):
            for j in range(9):
                self.matriz[i][j]=int(linea[0])
                linea = linea[1:]
                if(j==8): linea = linea[1:]
    
    def validarFila(self,fila,columna):
        for i in range(9):
            if(i!=columna):
                if(self.matriz[fila][i]==self.matriz[fila][columna] | self.matriz[fila][i]>9): return False
        return True
    
    def validarColumna(self,fila,columna):
        for i in range(9):
            if(i!=fila):
                if(self.matriz[i][columna]==self.matriz[fila][columna] | self.matriz[i][columna]>9): return False;
        return True
    
    def validarBloque(self,fila,columna):
        ancho=fila/3
        largo=columna/3
        i=ancho*3
        j=largo*3
        
        for i in range(ancho*3+3):
            for j in range(largo*3+3):
                if((i==fila & j==columna)==False):
                    if(self.matriz[fila][columna]==self.matriz[i][j]): return False
        return True
    
    def validacion(self,fila,columna):
        if(self.validarFila(fila, columna) & self.validarColumna(fila, columna) & self.validarBloque(fila, columna)): return True
        return False