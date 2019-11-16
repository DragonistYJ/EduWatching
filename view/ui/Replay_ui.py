# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Replay.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RecordWindow(object):
    def setupUi(self, RecordWindow):
        RecordWindow.setObjectName("RecordWindow")
        RecordWindow.resize(998, 748)
        self.centralwidget = QtWidgets.QWidget(RecordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        RecordWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RecordWindow)
        QtCore.QMetaObject.connectSlotsByName(RecordWindow)

    def retranslateUi(self, RecordWindow):
        _translate = QtCore.QCoreApplication.translate
        RecordWindow.setWindowTitle(_translate("RecordWindow", "MainWindow"))

