# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\echoserver.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(755, 520)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 110, 150, 46))
        self.pushButton.setObjectName("pushButton")
        self.input_edit = QtWidgets.QLineEdit(Dialog)
        self.input_edit.setGeometry(QtCore.QRect(270, 110, 231, 41))
        self.input_edit.setObjectName("input_edit")
        self.input_label = QtWidgets.QLabel(Dialog)
        self.input_label.setGeometry(QtCore.QRect(80, 110, 151, 41))
        self.input_label.setObjectName("input_label")
        self.output_label = QtWidgets.QLabel(Dialog)
        self.output_label.setGeometry(QtCore.QRect(60, 220, 641, 241))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output_label.setFont(font)
        self.output_label.setText("")
        self.output_label.setObjectName("output_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.input_label.setText(_translate("Dialog", "Message:"))

