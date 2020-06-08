# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grid.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(318, 556)
        MainWindow.setMaximumSize(QtCore.QSize(450, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_img.sizePolicy().hasHeightForWidth())
        self.grid_img.setSizePolicy(sizePolicy)
        self.grid_img.setMinimumSize(QtCore.QSize(300, 200))
        self.grid_img.setMaximumSize(QtCore.QSize(60000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.grid_img.setFont(font)
        self.grid_img.setStyleSheet("background-image: url(:/grid_prefix/tuv-rheinland-power-grid-modelling-and-simulation-ts-515999506.jpg);")
        self.grid_img.setAlignment(QtCore.Qt.AlignCenter)
        self.grid_img.setObjectName("grid_img")
        self.verticalLayout.addWidget(self.grid_img)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.PowerUsageLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PowerUsageLineEdit.setObjectName("PowerUsageLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.PowerUsageLineEdit)
        self.powerLossLabel = QtWidgets.QLabel(self.centralwidget)
        self.powerLossLabel.setObjectName("powerLossLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.powerLossLabel)
        self.powerLossLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.powerLossLineEdit.setObjectName("powerLossLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.powerLossLineEdit)
        self.PowerUsageLabel = QtWidgets.QLabel(self.centralwidget)
        self.PowerUsageLabel.setObjectName("PowerUsageLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.PowerUsageLabel)
        self.iDLineEditin = QtWidgets.QLineEdit(self.centralwidget)
        self.iDLineEditin.setObjectName("iDLineEditin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.iDLineEditin)
        self.iDLabelin = QtWidgets.QLabel(self.centralwidget)
        self.iDLabelin.setObjectName("iDLabelin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.iDLabelin)
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.add_ele_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_ele_btn.sizePolicy().hasHeightForWidth())
        self.add_ele_btn.setSizePolicy(sizePolicy)
        self.add_ele_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.add_ele_btn.setObjectName("add_ele_btn")
        self.verticalLayout.addWidget(self.add_ele_btn)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.iDLabel = QtWidgets.QLabel(self.centralwidget)
        self.iDLabel.setMinimumSize(QtCore.QSize(95, 0))
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.iDLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.iDLineEdit.setObjectName("iDLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.iDLineEdit)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.rem_ele_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rem_ele_btn.sizePolicy().hasHeightForWidth())
        self.rem_ele_btn.setSizePolicy(sizePolicy)
        self.rem_ele_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.rem_ele_btn.setObjectName("rem_ele_btn")
        self.verticalLayout.addWidget(self.rem_ele_btn)
        self.disp_data_btn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.disp_data_btn.setObjectName("disp_data_btn")
        self.verticalLayout.addWidget(self.disp_data_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 318, 21))
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
        self.grid_img.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Grid</span></p></body></html>"))
        self.powerLossLabel.setText(_translate("MainWindow", "Power loss [kW]:"))
        self.PowerUsageLabel.setText(_translate("MainWindow", "Power usage [kW]: "))
        self.iDLabelin.setText(_translate("MainWindow", "ID:"))
        self.nameLabel.setText(_translate("MainWindow", "Name: "))
        self.add_ele_btn.setText(_translate("MainWindow", "Add Element"))
        self.iDLabel.setText(_translate("MainWindow", "ID: "))
        self.rem_ele_btn.setText(_translate("MainWindow", "Remove Element"))
        self.disp_data_btn.setText(_translate("MainWindow", "Display Database"))
import grid_img_rc