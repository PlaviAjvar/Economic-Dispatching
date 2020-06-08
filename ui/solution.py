# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solution.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.total_cost = QtWidgets.QLabel(self.centralwidget)
        self.total_cost.setMinimumSize(QtCore.QSize(0, 25))
        self.total_cost.setText("")
        self.total_cost.setObjectName("total_cost")
        self.verticalLayout.addWidget(self.total_cost)
        self.supplied_power = QtWidgets.QLabel(self.centralwidget)
        self.supplied_power.setMinimumSize(QtCore.QSize(0, 25))
        self.supplied_power.setText("")
        self.supplied_power.setObjectName("supplied_power")
        self.verticalLayout.addWidget(self.supplied_power)
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_btn.sizePolicy().hasHeightForWidth())
        self.refresh_btn.setSizePolicy(sizePolicy)
        self.refresh_btn.setMinimumSize(QtCore.QSize(0, 39))
        self.refresh_btn.setObjectName("refresh_btn")
        self.verticalLayout.addWidget(self.refresh_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 21))
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
        self.refresh_btn.setText(_translate("MainWindow", "Refresh Solution"))
