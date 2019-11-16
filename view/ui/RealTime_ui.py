# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RealTime.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RealTime(object):
    def setupUi(self, RealTime):
        RealTime.setObjectName("RealTime")
        RealTime.resize(1400, 860)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/favicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RealTime.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(RealTime)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        RealTime.setCentralWidget(self.centralwidget)

        self.retranslateUi(RealTime)
        QtCore.QMetaObject.connectSlotsByName(RealTime)

    def retranslateUi(self, RealTime):
        _translate = QtCore.QCoreApplication.translate
        RealTime.setWindowTitle(_translate("RealTime", "实时监控"))


import resource.main_rc
