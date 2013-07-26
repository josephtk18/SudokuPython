# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_jugar.ui'
#
# Created: Thu Jul 25 18:59:06 2013
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

class Ui_Ventana_Jugar(object):
    def setupUi(self, Ventana_Jugar):
        Ventana_Jugar.setObjectName(_fromUtf8("Ventana_Jugar"))
        Ventana_Jugar.resize(398, 369)
        self.centralwidget = QtGui.QWidget(Ventana_Jugar)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(80, 0, 271, 51))
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
        self.leyenda.setGeometry(QtCore.QRect(110, 60, 121, 16))
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
        self.Btn_facil = QtGui.QPushButton(self.centralwidget)
        self.Btn_facil.setGeometry(QtCore.QRect(150, 100, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 111, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.Btn_facil.setPalette(palette)
        self.Btn_facil.setObjectName(_fromUtf8("Btn_facil"))
        self.Btn_normal = QtGui.QPushButton(self.centralwidget)
        self.Btn_normal.setGeometry(QtCore.QRect(150, 150, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 111, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.Btn_normal.setPalette(palette)
        self.Btn_normal.setObjectName(_fromUtf8("Btn_normal"))
        self.Btn_dificil = QtGui.QPushButton(self.centralwidget)
        self.Btn_dificil.setGeometry(QtCore.QRect(150, 200, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 111, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.Btn_dificil.setPalette(palette)
        self.Btn_dificil.setObjectName(_fromUtf8("Btn_dificil"))
        self.Btn_cargar = QtGui.QPushButton(self.centralwidget)
        self.Btn_cargar.setGeometry(QtCore.QRect(150, 250, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 111, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.Btn_cargar.setPalette(palette)
        self.Btn_cargar.setObjectName(_fromUtf8("Btn_cargar"))
        self.Btn_menu = QtGui.QPushButton(self.centralwidget)
        self.Btn_menu.setGeometry(QtCore.QRect(150, 300, 141, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 140, 140))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 111, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.Btn_menu.setPalette(palette)
        self.Btn_menu.setObjectName(_fromUtf8("Btn_menu"))
        Ventana_Jugar.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Ventana_Jugar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Ventana_Jugar.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Ventana_Jugar)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Ventana_Jugar.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Jugar)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Jugar)

    def retranslateUi(self, Ventana_Jugar):
        Ventana_Jugar.setWindowTitle(_translate("Ventana_Jugar", "MainWindow", None))
        self.titulo.setText(_translate("Ventana_Jugar", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">Jugar</span></p></body></html>", None))
        self.leyenda.setText(_translate("Ventana_Jugar", "<html><head/><body><p><span style=\" font-size:10pt;\">Seleccione un nivel:</span></p></body></html>", None))
        self.Btn_facil.setText(_translate("Ventana_Jugar", "Fácil", None))
        self.Btn_normal.setText(_translate("Ventana_Jugar", "Normal", None))
        self.Btn_dificil.setText(_translate("Ventana_Jugar", "Dificil", None))
        self.Btn_cargar.setText(_translate("Ventana_Jugar", "Cargar Partida", None))
        self.Btn_menu.setText(_translate("Ventana_Jugar", "Regresar al menú", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Ventana_Jugar = QtGui.QMainWindow()
    ui = Ui_Ventana_Jugar()
    ui.setupUi(Ventana_Jugar)
    Ventana_Jugar.show()
    sys.exit(app.exec_())

