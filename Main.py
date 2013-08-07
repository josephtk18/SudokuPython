'''
Created on 20/07/2013

@author: Charlie Medina
'''
import sys
from PyQt4 import QtGui  
from VentanaPrincipal import VentanaPrincipal
from xml.dom.minidom import Document
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    vPrincipal = VentanaPrincipal()
    #pic = QtGui.QLabel(vPrincipal)
    #pic.setGeometry(10,10,400,100)
    #pic.setPixmap(QtGui.QPixmap("Imagenes/yingyangsudoku.jpg"))
    vPrincipal.show()
    cad = "Ola k ase"
    coded = cad.encode('base64','strict')
    print "Encoded String: " + coded
    print "Decoded String: " + coded.decode('base64','strict')
    
    doc = Document()
    wml = doc.createElement("Sudoku")
    doc.appendChild(wml)
    maincard = doc.createElement("Juego")
    maincard.setAttribute("save","true")
    wml.appendChild(maincard)
    paragraph1 = doc.createElement("Nombre")
    maincard.appendChild(paragraph1)
    ptext = doc.createTextNode("Charlie")
    paragraph1.appendChild(ptext)
    print doc.toprettyxml(indent=" ")
    
    tree = ET.parse('partida.XML')
    root = tree.getroot()
    print root[0][0].text
    
    sys.exit(app.exec_())