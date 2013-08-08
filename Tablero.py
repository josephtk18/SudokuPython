'''
Created on 03/08/2013

@author: Charlie Medina
'''
import casilla
import random

class Tablero(object):

    def __init__(self):
        self.casillas=[]
        self.inicializarCasillas()
        
    def inicializarCasillas(self):
        for i in range(9):
            for j in range(9):
                region = casilla.Casilla.buscarRegion(self, i+1, j+1)
                c = casilla.Casilla(0,i+1,j+1,region)
                self.casillas.append(c)
    
    def hayRepetidoFila(self,c,cont):
        for x in self.casillas:
            if(x.fila==c.fila):
                if(x.contenido==cont):
                    return True
        return False
    
    def pasarBloquesAFila(self,F,B1,B2,B3):
        B1tmp=B1
        B2tmp=B2
        B3tmp=B3
        for i in range(3):
            F.append(B1tmp.pop())
        for j in range(3):
            F.append(B2tmp.pop())
        for k in range(3):
            F.append(B3tmp.pop())
    
    def cambiarOrdenBloques(self,B1,B2,B3):
        i=B1.pop(0) 
        j=B1.pop(0)
        k=B1.pop(0)
        B1.append(k)
        B1.append(i)
        B1.append(j)
        
        i=B2.pop(0) 
        j=B2.pop(0)
        k=B2.pop(0)
        B2.append(k)
        B2.append(i)
        B2.append(j)
        
        i=B3.pop(0) 
        j=B3.pop(0)
        k=B3.pop(0)
        B3.append(k)
        B3.append(i)
        B3.append(j)
    
    def generarTablero(self):
        col=1
        bloque1=[]
        bloque2=[]
        bloque3=[]
        fila=[]
        fila_actual=2
        k=1
        pos_bloque=0
        
        listo=False
        
        for c in self.casillas:
            while listo==False:
                cont = random.randint(1,9)
                if(self.hayRepetidoFila(c, cont)==False):
                    c.contenido=cont
                    c.ocupada=True
                    if(col>=1 & col<=3):
                        bloque1.append(cont)
                    if(col>=4 & col<=6):
                        bloque2.append(cont)
                    if(col>=7 & col<=9):
                        bloque3.append(cont)
                    col=col +1
                    listo=True  
            listo=False    
        
        while fila_actual<=9:
            if(k==0):
                self.pasarBloquesAFila(fila,bloque1,bloque2,bloque3)
            if(k==1):
                self.pasarBloquesAFila(fila,bloque2,bloque3,bloque1)
            if(k==2):
                self.pasarBloquesAFila(fila,bloque3,bloque1,bloque2)
            for c in self.casillas:
                if(c.fila==fila_actual):
                    c.contenido=fila[pos_bloque]
                    c.ocupada=True
                    pos_bloque=pos_bloque + 1
            if(fila_actual==3 | fila_actual==6):
                self.cambiarOrdenBloques(bloque1,bloque2,bloque3)
            if(k==2):
                k=0
            else:
                k= k + 1
            fila_actual=fila_actual + 1