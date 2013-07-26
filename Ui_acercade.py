# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acercade.ui'
#
# Created: Thu Jul 25 18:59:28 2013
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

class Ui_AcercaDe(object):
    def setupUi(self, AcercaDe):
        AcercaDe.setObjectName(_fromUtf8("AcercaDe"))
        AcercaDe.resize(395, 274)
        self.centralwidget = QtGui.QWidget(AcercaDe)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.acercaDe = QtGui.QLabel(self.centralwidget)
        self.acercaDe.setGeometry(QtCore.QRect(120, 20, 191, 61))
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
        self.acercaDe.setPalette(palette)
        self.acercaDe.setObjectName(_fromUtf8("acercaDe"))
        self.contenido = QtGui.QLabel(self.centralwidget)
        self.contenido.setGeometry(QtCore.QRect(50, 100, 311, 151))
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
        self.contenido.setPalette(palette)
        self.contenido.setObjectName(_fromUtf8("contenido"))
        AcercaDe.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AcercaDe)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 395, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        AcercaDe.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(AcercaDe)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AcercaDe.setStatusBar(self.statusbar)

        self.retranslateUi(AcercaDe)
        QtCore.QMetaObject.connectSlotsByName(AcercaDe)

    def retranslateUi(self, AcercaDe):
        AcercaDe.setWindowTitle(_translate("AcercaDe", "MainWindow", None))
        self.acercaDe.setText(_translate("AcercaDe", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; font-style:italic;\">Acerca De</span></p></body></html>", None))
        self.contenido.setText(_translate("AcercaDe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Sudoku V1.0</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Proyecto creado por:<br /></span>- Joseph Gallardo<br />- Charlie Medina<br />- Kevin Zambrano</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Lenguajes de Programación</span><br /><span style=\" font-weight:600;\">2013</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AcercaDe = QtGui.QMainWindow()
    ui = Ui_AcercaDe()
    ui.setupUi(AcercaDe)
    AcercaDe.show()
    sys.exit(app.exec_())

