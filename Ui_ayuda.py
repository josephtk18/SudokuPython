# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ayuda.ui'
#
# Created: Thu Jul 25 18:59:42 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Ayuda(object):
    def setupUi(self, Ayuda):
        Ayuda.setObjectName(_fromUtf8("Ayuda"))
        Ayuda.resize(394, 365)
        self.centralwidget = QtGui.QWidget(Ayuda)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(170, 30, 121, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 111, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.titulo.setPalette(palette)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        self.leyenda = QtGui.QLabel(self.centralwidget)
        self.leyenda.setGeometry(QtCore.QRect(110, 110, 261, 241))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 111, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.leyenda.setPalette(palette)
        self.leyenda.setObjectName(_fromUtf8("leyenda"))
        Ayuda.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Ayuda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Ayuda.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Ayuda)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Ayuda.setStatusBar(self.statusbar)

        self.retranslateUi(Ayuda)
        QtCore.QMetaObject.connectSlotsByName(Ayuda)

    def retranslateUi(self, Ayuda):
        Ayuda.setWindowTitle(_translate("Ayuda", "MainWindow", None))
        self.titulo.setText(_translate("Ayuda", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Ayuda</span></p></body></html>", None))
        self.leyenda.setText(_translate("Ayuda", "<html><head/><body><p align=\"justify\">- El sudoku se presenta normalmente como una<br/>tabla de 9 × 9, compuesta por subtablas de 3x3<br/>denominadas &quot;regiones&quot; (también se le llaman <br/>&quot;cajas&quot; o &quot;bloques&quot;).</p><p align=\"justify\">- Algunas celdas ya contienen números, cono-<br/>cidos como &quot;números dados&quot; (o a veces &quot;pistas&quot;).<br/>El objetivo es rellenar las celdas vacías, con un <br/>número en cada una de ellas, de tal forma que <br/>cada columna, fila y región contenga los números <br/>1–9 sólo una vez.</p><p>- Además, cada número de la solución aparece <br/>sólo una vez en cada una de las tres &quot;direccio-<br/>nes&quot;, de ahí el &quot;los números deben estar solos&quot; <br/>que evoca el nombre del juego.<br/><br/>Fuente: Wikipedia.</p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Ayuda = QtGui.QMainWindow()
    ui = Ui_Ayuda()
    ui.setupUi(Ayuda)
    Ayuda.show()
    sys.exit(app.exec_())

