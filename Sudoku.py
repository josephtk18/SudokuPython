# coding=utf-8
'''
Created on 04/08/2013

@author: Charlie Medina & Joseph Gallardo
'''

from PyQt4 import QtCore, QtGui 
from Ui_sudoku import Ui_Sudoku
from xml.dom.minidom import Document
import xml.etree.ElementTree as ET
import Tablero
import digito
import random
import VentanaPrincipal
import ctypes

class Sudoku(QtGui.QMainWindow):

    def __init__(self,nivel,cargar):
        QtGui.QMainWindow.__init__(self)
        self.ventana=Ui_Sudoku()
        self.ventana.setupUi(self)
        self.setWindowTitle("Sudoku")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.nombre=""
        self.matriz = [ [0 for i in range(9)] for j in range(9) ]
        self.teclado=[]
        self.casSelect = Tablero.casilla.Casilla(0,0,0,0)
        self.seconds=0
        self.num=QtGui.QLCDNumber()
        self.time=QtCore.QTime()
        if(cargar==False):
            self.nombre,ok = QtGui.QInputDialog.getText(self, 'Juego Nuevo', 'Ingrese el nombre del jugador:')
        
        self.t=Tablero.Tablero()
        self.inicializarMatriz()
        self.iniciarTeclado()
        self.t.generarTablero()
        self.pasarTableroAMatriz(self.t.casillas)
        self.inicializarTablasUI(self.t.casillas)
        self.ocultarCasillas(nivel)
        if (cargar==True):
            self.cargar()
        self.pasarMatrizAUI()
        self.inicializarCronometro()
        self.startTime()
        
        self.connect(self.ventana.actionVolver_al_men_principal,QtCore.SIGNAL('triggered()'), self.volver)
        self.connect(self.ventana.actionSalir,QtCore.SIGNAL('triggered()'), self.salir)
        self.connect(self.ventana.actionGuardar_partida,QtCore.SIGNAL('triggered()'), self.guardar)
        
    def inicializarCronometro(self):
        self.time.setHMS(0,0,0,0)
        self.timer=QtCore.QTimer()
        
        self.connect(self.timer,QtCore.SIGNAL("timeout()"),self.showTime)
        
        self.seconds=0
        
        self.text=self.time.toString("hh:mm:ss")
        self.num.display(self.text)
        self.num.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.ventana.LayoutCronometro.addWidget(self.num)
    
    def startTime(self):
        self.timer.start(1000)
    def stopTime(self):
        self.timer.stop()
        
    def showTime(self):
        self.seconds = self.seconds + 1
        self.newTime = self.time.addSecs(self.seconds)
        self.text2=self.newTime.toString("hh:mm:ss")
        self.num.display(self.text2)
        
        
    def inicializarMatriz(self):
        for i in range(9):
            for j in range(9):
                self.matriz[i][j]=0
    
    def pasarTableroAMatriz(self,casillas):
        pos=0

        for i in range(9):
            for j in range(9):
                self.matriz[i][j]=casillas[pos].contenido
                pos=pos+1
    
    def changeSelected(self,ob):
        if(ob is None):
            return
        self.casSelect=ob
    
    def inicializarTablasUI(self,casillas):
        z=0
        for i in range(3):
            for j in range(3):
                self.connect(casillas[z], QtCore.SIGNAL("clickedChange"),self.changeSelected)
                self.ventana.bloque1.addWidget(casillas[z],i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.connect(casillas[z], QtCore.SIGNAL("clickedChange"),self.changeSelected)
                self.ventana.bloque2.addWidget(casillas[z],i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.connect(casillas[z], QtCore.SIGNAL("clickedChange"),self.changeSelected)
                self.ventana.bloque3.addWidget(casillas[z],i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.connect(casillas[z], QtCore.SIGNAL("clickedChange"),self.changeSelected)
                self.ventana.bloque4.addWidget(casillas[z],i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.connect(casillas[z], QtCore.SIGNAL("clickedChange"),self.changeSelected)
                self.ventana.bloque5.addWidget(casillas[z],i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.connect(casillas[z], QtCore.SIGNAL("clickedChange"),self.changeSelected)
                self.ventana.bloque6.addWidget(casillas[z],i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.connect(casillas[z], QtCore.SIGNAL("clickedChange"),self.changeSelected)
                self.ventana.bloque7.addWidget(casillas[z],i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.connect(casillas[z], QtCore.SIGNAL("clickedChange"),self.changeSelected)
                self.ventana.bloque8.addWidget(casillas[z],i,j)
                z=z+1
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                self.connect(casillas[z], QtCore.SIGNAL("clickedChange"),self.changeSelected)
                self.ventana.bloque9.addWidget(casillas[z],i,j)
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
                    cas=self.ventana.bloque1.itemAtPosition(i1,j1).widget()
                    n = self.matriz[i][j]
                    cas.contenido=n
                    cas.setGrafic(n)
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j1=j1+1
                    if(j1==3):
                        i1=i1+1
                        j1=0
                if(region==2):
                    cas=self.ventana.bloque2.itemAtPosition(i2,j2).widget()
                    n = self.matriz[i][j]
                    cas.contenido=n
                    cas.setGrafic(n)
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j2=j2+1
                    if(j2==3):
                        i2=i2+1
                        j2=0
                if(region==3):
                    cas=self.ventana.bloque3.itemAtPosition(i3,j3).widget()
                    n = self.matriz[i][j]
                    cas.contenido=n
                    cas.setGrafic(n)
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j3=j3+1
                    if(j3==3):
                        i3=i3+1
                        j3=0
                if(region==4):
                    cas=self.ventana.bloque4.itemAtPosition(i4,j4).widget()
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j4=j4+1
                    if(j4==3):
                        i4=i4+1
                        j4=0
                if(region==5):
                    cas=self.ventana.bloque5.itemAtPosition(i5,j5).widget()
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j5=j5+1
                    if(j5==3):
                        i5=i5+1
                        j5=0
                if(region==6):
                    cas=self.ventana.bloque6.itemAtPosition(i6,j6).widget()
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j6=j6+1
                    if(j6==3):
                        i6=i6+1
                        j6=0
                if(region==7):
                    cas=self.ventana.bloque7.itemAtPosition(i7,j7).widget()
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j7=j7+1
                    if(j7==3):
                        i7=i7+1
                        j7=0
                if(region==8):
                    cas=self.ventana.bloque8.itemAtPosition(i8,j8).widget()
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j8=j8+1
                    if(j8==3):
                        i8=i8+1
                        j8=0
                if(region==9):
                    cas=self.ventana.bloque9.itemAtPosition(i9,j9).widget()
                    cas.contenido=self.matriz[i][j]
                    cas.setGrafic(self.matriz[i][j])
                    if(self.matriz[i][j]==0):
                        cas.modificable=True
                    j9=j9+1
                    if(j9==3):
                        i9=i9+1
                        j9=0 
    
    def tableroLleno(self):
        for i in range(3):
            for j in range(3):
                cas= self.ventana.bloque1.itemAtPosition(i,j).widget()
                if(cas.contenido==0):
                    return False
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas= self.ventana.bloque2.itemAtPosition(i,j).widget()
                if(cas.contenido==0):
                    return False            
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas= self.ventana.bloque3.itemAtPosition(i,j).widget()
                if(cas.contenido==0):
                    return False            
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas= self.ventana.bloque4.itemAtPosition(i,j).widget()
                if(cas.contenido==0):
                    return False            
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas= self.ventana.bloque5.itemAtPosition(i,j).widget()
                if(cas.contenido==0):
                    return False            
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas= self.ventana.bloque6.itemAtPosition(i,j).widget()
                if(cas.contenido==0):
                    return False            
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas= self.ventana.bloque7.itemAtPosition(i,j).widget()
                if(cas.contenido==0):
                    return False            
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas= self.ventana.bloque8.itemAtPosition(i,j).widget()
                if(cas.contenido==0):
                    return False            
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas= self.ventana.bloque9.itemAtPosition(i,j).widget()
                if(cas.contenido==0):
                    return False
        return True
    
    def asignToSelect(self,ob):
        valido=True
        if(ob is None): return
        if(self.casSelect.modificable==True):
            self.d=ob
            self.dig=self.d.getDigito()
            self.casSelect.contenido=self.dig
            self.casSelect.setGrafic2(self.dig)
            
        if(self.tableroLleno()==True):
            self.pasarUIAMatriz() 
            for i in range(3):
                for j in range(3):
                    if(self.validacion(i,j)==False): valido=False
            messageBox = ctypes.windll.user32.MessageBoxW             
            if(valido==False): 
                messageBox(None,"El tablero esta mal llenado", "Error", 0)
            else:
                messageBox(None,"El tablero esta correcto!", "Felicidades", 0)
                self.v = VentanaPrincipal.VentanaPrincipal()
                self.v.show()
                self.close() 
        
    def iniciarTeclado(self):
        i=0
        for i in range(9):            
            self.teclado.append(digito.Digito(i+1))
            self.connect(self.teclado[i], QtCore.SIGNAL("changeToSelect"), self.asignToSelect)
            self.ventana.gridTeclado.addWidget(self.teclado[i])
    
    def ocultarCasillas(self,nivel):
        tmp = 0
        if(nivel==1): tmp=3
        if(nivel==2): tmp=5
        if(nivel==3): tmp=6
        cont=tmp
        c = Tablero.casilla.Casilla(0,0,0,0)
        
        for bloque in range(9):
            while cont>0:
                for i in range(9):
                    for j in range(9):
                        if(cont>0):
                            if(c.buscarRegion(i+1,j+1)==bloque+1):
                                if(random.randint(0,1)==1):
                                    self.matriz[i][j]=0
                                    cont = cont-1
            cont=tmp    
    
    def pasarUIAMatriz(self):
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque1.itemAtPosition(i,j).widget()
                cont = cas.contenido
                self.matriz[i][j]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque2.itemAtPosition(i,j).widget()
                cont = cas.contenido
                self.matriz[i][j+3]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque3.itemAtPosition(i,j).widget()
                cont = cas.contenido
                self.matriz[i][j+6]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque4.itemAtPosition(i,j).widget()
                cont = cas.contenido
                self.matriz[i+3][j]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque5.itemAtPosition(i,j).widget()
                cont = cas.contenido
                self.matriz[i+3][j+3]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque6.itemAtPosition(i,j).widget()
                cont = cas.contenido
                self.matriz[i+3][j+6]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque7.itemAtPosition(i,j).widget()
                cont = cas.contenido
                self.matriz[i+6][j]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque8.itemAtPosition(i,j).widget()
                cont = cas.contenido
                self.matriz[i+6][j+3]=cont
        
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                cas = self.ventana.bloque9.itemAtPosition(i,j).widget()
                cont = cas.contenido
                self.matriz[i+6][j+6]=cont
    
    def pasarMatrizAString(self):
        linea=""
        for i in range(9):
            for j in range(9):                
                linea=linea+str(self.matriz[i][j])
                if(j==8): linea+"\n"
        return linea
    
    def pasarStringAMatriz(self,linea):
        for i in range(9):
            for j in range(9):
                self.matriz[i][j]=int(linea[0])
                linea = linea[1:]
                #if(j==8): linea = linea[1:]
    
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
        ancho= int(fila/3) 
        largo= int(columna/3)
        i=ancho*3
        j=largo*3
        rangoi = (ancho*3)+3
        rangoj = (largo*3)+3
        
        for i in range(rangoi):
            for j in range(rangoj):
                if((i==fila & j==columna)==False):
                    if(self.matriz[fila][columna]==self.matriz[i][j]): return False
        return True
    
    def validacion(self,fila,columna):
        if(self.validarFila(fila, columna) & self.validarColumna(fila, columna) & self.validarBloque(fila, columna)): return True
        return False
    
    def volver(self):
        self.v = VentanaPrincipal.VentanaPrincipal()
        self.v.show()
        self.close() 
    
    def salir(self):
        messageBox = ctypes.windll.user32.MessageBoxA        
        salir = messageBox(None,'Seguro que desea salir?', 'Salir', 0x40 | 0x1)
        if salir==1:
            messageBox(None,"Vuelva pronto", "Salir", 0)
            self.close()
            
    def guardar(self):
        messageBox = ctypes.windll.user32.MessageBoxA        
        guardar = messageBox(None,'Desea guardar la partida?', 'Guardar', 0x40 | 0x1)
        if guardar==1:
            self.pasarUIAMatriz()
            linea = self.pasarMatrizAString()
            crypted = linea.encode('base64','strict')
            
            root = ET.Element("Sudoku")
            doc = ET.SubElement(root,"partida")
            field1 = ET.SubElement(doc,"Nombre")
            field1.text = str(self.nombre)
            print str(self.nombre)
            field2 = ET.SubElement(doc,"Tablero")
            field2.text = crypted
            print crypted
            field3 = ET.SubElement(doc,"Tiempo")
            field3.text = str(self.seconds)
            print str(self.seconds)
            tree = ET.ElementTree(root)
            tree.write("partida.xml")
            messageBox(None,"La partida se ha guardado exitosamente!", "Guardar", 0)
            
    
    def cargar(self):
        tree = ET.parse('partida.xml')
        root = tree.getroot()
        self.nombre = root[0][0].text
        
        crypted = root[0][1].text
        tablero = crypted.decode('base64','strict')
        self.pasarStringAMatriz(tablero)
        self.pasarMatrizAUI()
        
        tiempo = root[0][2].text
        self.seconds = int(tiempo)
        '''self.newTime = self.time.addSecs(self.seconds)
        self.text2=self.newTime.toString("hh:mm:ss")
        self.num.display(self.text2)'''
        