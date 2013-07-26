# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estadisticas.ui'
#
# Created: Thu Jul 25 19:00:02 2013
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

class Ui_Estadisticas(object):
    def setupUi(self, Estadisticas):
        Estadisticas.setObjectName(_fromUtf8("Estadisticas"))
        Estadisticas.resize(395, 467)
        self.centralwidget = QtGui.QWidget(Estadisticas)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(90, 30, 221, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 143, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 143, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 111, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.titulo.setPalette(palette)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 90, 221, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 143, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 143, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 111, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        self.label.setObjectName(_fromUtf8("label"))
        self.ganadores = QtGui.QLabel(self.centralwidget)
        self.ganadores.setGeometry(QtCore.QRect(120, 120, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 143, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 143, 143))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 111, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.ganadores.setPalette(palette)
        self.ganadores.setText(_fromUtf8(""))
        self.ganadores.setObjectName(_fromUtf8("ganadores"))
        Estadisticas.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Estadisticas)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Estadisticas.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Estadisticas)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Estadisticas.setStatusBar(self.statusbar)

        self.retranslateUi(Estadisticas)
        QtCore.QMetaObject.connectSlotsByName(Estadisticas)

    def retranslateUi(self, Estadisticas):
        Estadisticas.setWindowTitle(_translate("Estadisticas", "MainWindow", None))
        self.titulo.setText(_translate("Estadisticas", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">Estadísticas</span></p></body></html>", None))
        self.label.setText(_translate("Estadisticas", "Lista de jugadores que finalizaron el juego:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Estadisticas = QtGui.QMainWindow()
    ui = Ui_Estadisticas()
    ui.setupUi(Estadisticas)
    Estadisticas.show()
    sys.exit(app.exec_())

