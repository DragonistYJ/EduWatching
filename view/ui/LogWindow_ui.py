# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogWindow(object):
    def setupUi(self, LogWindow):
        LogWindow.setObjectName("LogWindow")
        LogWindow.resize(480, 360)
        LogWindow.setMinimumSize(QtCore.QSize(480, 360))
        LogWindow.setMaximumSize(QtCore.QSize(480, 360))
        self.centralwidget = QtWidgets.QWidget(LogWindow)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
                                         "    border-image: url(:/log/background.png);\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_title = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_title.sizePolicy().hasHeightForWidth())
        self.widget_title.setSizePolicy(sizePolicy)
        self.widget_title.setMinimumSize(QtCore.QSize(0, 25))
        self.widget_title.setObjectName("widget_title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_title)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_logo = QtWidgets.QLabel(self.widget_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/log/logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout.addWidget(self.label_logo)
        spacerItem = QtWidgets.QSpacerItem(99, 4, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_author = QtWidgets.QLabel(self.widget_title)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(12)
        self.label_author.setFont(font)
        self.label_author.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_author.setObjectName("label_author")
        self.horizontalLayout.addWidget(self.label_author)
        self.pushButton_close = QtWidgets.QPushButton(self.widget_title)
        self.pushButton_close.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_close.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close.setStyleSheet("#pushButton_close {\n"
                                            "    background-color: rgba(255, 255, 255, 0);\n"
                                            "}")
        self.pushButton_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/log/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout_3.addWidget(self.widget_title)
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setStyleSheet("#label_name {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    margin-top: 10px;\n"
                                      "    margin-bottom: 10px\n"
                                      "}")
        self.label_name.setObjectName("label_name")
        self.verticalLayout_3.addWidget(self.label_name)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.widget_input = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_input.sizePolicy().hasHeightForWidth())
        self.widget_input.setSizePolicy(sizePolicy)
        self.widget_input.setStyleSheet("#widget_input {\n"
                                        "    background-color: rgba(0, 0, 0, 80);\n"
                                        "    border-style: solid;\n"
                                        "    border-radius: 2px\n"
                                        "}")
        self.widget_input.setObjectName("widget_input")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_input)
        self.verticalLayout_2.setContentsMargins(16, 20, 16, 20)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_username.sizePolicy().hasHeightForWidth())
        self.lineEdit_username.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setStyleSheet("#lineEdit_username {\n"
                                             "    padding-left: 18px;\n"
                                             "    font: 12pt \"宋体\";\n"
                                             "    border-style: solid;\n"
                                             "    border-width: 2px;\n"
                                             "    border-radius: 4px;\n"
                                             "    \n"
                                             "    border-color: rgb(255, 255, 255);\n"
                                             "}\n"
                                             "#lineEdit_username:hover {\n"
                                             "    border-style: solid;\n"
                                             "    border-color: rgb(25, 185, 231);\n"
                                             "}")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout_2.addWidget(self.lineEdit_username)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("#lineEdit_password {\n"
                                             "    padding-left: 18px;\n"
                                             "    font: 12pt \"宋体\";\n"
                                             "    border-style: solid;\n"
                                             "    border-width: 2px;\n"
                                             "    border-radius: 4px;\n"
                                             "    border-color: rgb(255, 255, 255);\n"
                                             "}\n"
                                             "#lineEdit_password:hover {\n"
                                             "    border-style: solid;\n"
                                             "    border-color: rgb(25, 185, 231);\n"
                                             "}")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout_2.addWidget(self.lineEdit_password)
        self.pushButton_login = QtWidgets.QPushButton(self.widget_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login.setSizePolicy(sizePolicy)
        self.pushButton_login.setStyleSheet("#pushButton_login {\n"
                                            "    background-color: rgb(25, 185, 231);\n"
                                            "    border-style: solid;\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    font: 12pt \"宋体\";\n"
                                            "    border-radius: 4px\n"
                                            "}\n"
                                            "\n"
                                            "#pushButton_login:hover {\n"
                                            "    background-color: rgba(25, 185, 231, 128)\n"
                                            "}")
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout_2.addWidget(self.pushButton_login)
        self.widget_forget = QtWidgets.QWidget(self.widget_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_forget.sizePolicy().hasHeightForWidth())
        self.widget_forget.setSizePolicy(sizePolicy)
        self.widget_forget.setObjectName("widget_forget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_forget)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton_forget = QtWidgets.QPushButton(self.widget_forget)
        self.pushButton_forget.setStyleSheet("#pushButton_forget {\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    font: 11pt \"宋体\";\n"
                                             "    text-decoration: underline;\n"
                                             "    background-color: rgba(255, 255, 255, 00);\n"
                                             "}")
        self.pushButton_forget.setObjectName("pushButton_forget")
        self.horizontalLayout_4.addWidget(self.pushButton_forget)
        self.verticalLayout_2.addWidget(self.widget_forget)
        self.horizontalLayout_3.addWidget(self.widget_input)
        spacerItem3 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addWidget(self.widget_3)
        LogWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogWindow)
        self.pushButton_close.clicked.connect(LogWindow.close)
        QtCore.QMetaObject.connectSlotsByName(LogWindow)

    def retranslateUi(self, LogWindow):
        _translate = QtCore.QCoreApplication.translate
        LogWindow.setWindowTitle(_translate("LogWindow", "MainWindow"))
        self.label_author.setText(_translate("LogWindow", "四川大学智慧三剑客     "))
        self.label_name.setText(_translate("LogWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:792;\">智慧课堂实时监测系统</span></p></body></html>"))
        self.lineEdit_username.setPlaceholderText(_translate("LogWindow", "请输入您的帐号"))
        self.lineEdit_password.setPlaceholderText(_translate("LogWindow", "请输入您的密码"))
        self.pushButton_login.setText(_translate("LogWindow", "登录"))
        self.pushButton_forget.setText(_translate("LogWindow", "忘记密码"))


from resource import log_rc
