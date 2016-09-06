# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_TurningGrill(object):
    def setupUi(self, TurningGrill):
        TurningGrill.setObjectName(_fromUtf8("TurningGrill"))
        TurningGrill.resize(513, 635)
        self.centralwidget = QtGui.QWidget(TurningGrill)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 471, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.PlainText = QtGui.QPlainTextEdit(self.layoutWidget)
        self.PlainText.setObjectName(_fromUtf8("PlainText"))
        self.verticalLayout.addWidget(self.PlainText)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 550, 311, 41))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.EncryptButton = QtGui.QPushButton(self.layoutWidget1)
        self.EncryptButton.setObjectName(_fromUtf8("EncryptButton"))
        self.horizontalLayout.addWidget(self.EncryptButton)
        self.DecryptButton = QtGui.QPushButton(self.layoutWidget1)
        self.DecryptButton.setObjectName(_fromUtf8("DecryptButton"))
        self.horizontalLayout.addWidget(self.DecryptButton)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 460, 301, 81))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.layoutWidget2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.clockwiseButton = QtGui.QRadioButton(self.layoutWidget2)
        self.clockwiseButton.setObjectName(_fromUtf8("clockwiseButton"))
        self.horizontalLayout_2.addWidget(self.clockwiseButton)
        self.AnticlockwiseButton = QtGui.QRadioButton(self.layoutWidget2)
        self.AnticlockwiseButton.setObjectName(_fromUtf8("AnticlockwiseButton"))
        self.horizontalLayout_2.addWidget(self.AnticlockwiseButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.layoutWidget2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(21, 91, 34, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Matrix = QtGui.QTableWidget(self.centralwidget)
        self.Matrix.setGeometry(QtCore.QRect(21, 110, 301, 241))
        self.Matrix.setObjectName(_fromUtf8("Matrix"))
        self.Matrix.setColumnCount(0)
        self.Matrix.setRowCount(0)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 90, 50, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Rotation1 = QtGui.QTableWidget(self.centralwidget)
        self.Rotation1.setGeometry(QtCore.QRect(340, 110, 150, 150))
        self.Rotation1.setObjectName(_fromUtf8("Rotation1"))
        self.Rotation1.setColumnCount(0)
        self.Rotation1.setRowCount(0)
        self.Rotation2 = QtGui.QTableWidget(self.centralwidget)
        self.Rotation2.setGeometry(QtCore.QRect(340, 270, 150, 150))
        self.Rotation2.setObjectName(_fromUtf8("Rotation2"))
        self.Rotation2.setColumnCount(0)
        self.Rotation2.setRowCount(0)
        self.Rotation3 = QtGui.QTableWidget(self.centralwidget)
        self.Rotation3.setGeometry(QtCore.QRect(340, 430, 150, 150))
        self.Rotation3.setObjectName(_fromUtf8("Rotation3"))
        self.Rotation3.setColumnCount(0)
        self.Rotation3.setRowCount(0)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 360, 301, 92))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.KeyShow = QtGui.QPlainTextEdit(self.widget)
        self.KeyShow.setObjectName(_fromUtf8("KeyShow"))
        self.gridLayout_2.addWidget(self.KeyShow, 1, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.TableSize = QtGui.QSpinBox(self.widget)
        self.TableSize.setObjectName(_fromUtf8("TableSize"))
        self.verticalLayout_4.addWidget(self.TableSize)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        TurningGrill.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TurningGrill)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        TurningGrill.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TurningGrill)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TurningGrill.setStatusBar(self.statusbar)

        self.retranslateUi(TurningGrill)
        QtCore.QMetaObject.connectSlotsByName(TurningGrill)

    def retranslateUi(self, TurningGrill):
        TurningGrill.setWindowTitle(_translate("TurningGrill", "Turning Grill", None))
        self.label_4.setText(_translate("TurningGrill", "Plain Text:", None))
        self.EncryptButton.setText(_translate("TurningGrill", "Encrypt", None))
        self.DecryptButton.setText(_translate("TurningGrill", "Decrypt", None))
        self.label_6.setText(_translate("TurningGrill", "Decrypted Text", None))
        self.clockwiseButton.setText(_translate("TurningGrill", "Clockwise", None))
        self.AnticlockwiseButton.setText(_translate("TurningGrill", "Anticlockwise", None))
        self.label_2.setText(_translate("TurningGrill", "Matrix:", None))
        self.label_3.setText(_translate("TurningGrill", "Rotations:", None))
        self.label.setText(_translate("TurningGrill", "Key:", None))
        self.label_5.setText(_translate("TurningGrill", "Table Rows", None))

