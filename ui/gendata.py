# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gendata.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 513)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.generatorIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.generatorIDLabel.setObjectName("generatorIDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.generatorIDLabel)
        self.generatorIDLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.generatorIDLineEdit.setObjectName("generatorIDLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.generatorIDLineEdit)
        self.generatorNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.generatorNameLabel.setObjectName("generatorNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.generatorNameLabel)
        self.generatorNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.generatorNameLineEdit.setObjectName("generatorNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.generatorNameLineEdit)
        self.dateAfterLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateAfterLabel.setObjectName("dateAfterLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dateAfterLabel)
        self.dateAfterLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dateAfterLineEdit.setObjectName("dateAfterLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateAfterLineEdit)
        self.dateBeforeLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateBeforeLabel.setObjectName("dateBeforeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dateBeforeLabel)
        self.dateBeforeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dateBeforeLineEdit.setObjectName("dateBeforeLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateBeforeLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.refresh_btn.setObjectName("refresh_btn")
        self.verticalLayout.addWidget(self.refresh_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generatorIDLabel.setText(_translate("MainWindow", "Generator ID:"))
        self.generatorNameLabel.setText(_translate("MainWindow", "Generator Name:"))
        self.dateAfterLabel.setText(_translate("MainWindow", "Date After:"))
        self.dateBeforeLabel.setText(_translate("MainWindow", "Date Before:"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh List"))
