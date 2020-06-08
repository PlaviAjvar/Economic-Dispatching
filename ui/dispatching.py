# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dispatching.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 360)
        MainWindow.setMinimumSize(QtCore.QSize(0, 360))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 360))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lecture_image = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lecture_image.sizePolicy().hasHeightForWidth())
        self.lecture_image.setSizePolicy(sizePolicy)
        self.lecture_image.setMinimumSize(QtCore.QSize(300, 300))
        self.lecture_image.setStyleSheet("background-image: url(:/dispatching_prefix/Screenshot_16.png);")
        self.lecture_image.setText("")
        self.lecture_image.setObjectName("lecture_image")
        self.gridLayout.addWidget(self.lecture_image, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.editgen_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editgen_btn.sizePolicy().hasHeightForWidth())
        self.editgen_btn.setSizePolicy(sizePolicy)
        self.editgen_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.editgen_btn.setObjectName("editgen_btn")
        self.verticalLayout.addWidget(self.editgen_btn)
        self.editnetwork_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editnetwork_btn.sizePolicy().hasHeightForWidth())
        self.editnetwork_btn.setSizePolicy(sizePolicy)
        self.editnetwork_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.editnetwork_btn.setObjectName("editnetwork_btn")
        self.verticalLayout.addWidget(self.editnetwork_btn)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.max_iter_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_iter_label.sizePolicy().hasHeightForWidth())
        self.max_iter_label.setSizePolicy(sizePolicy)
        self.max_iter_label.setMinimumSize(QtCore.QSize(0, 25))
        self.max_iter_label.setObjectName("max_iter_label")
        self.horizontalLayout_2.addWidget(self.max_iter_label)
        self.max_iter_txt = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_iter_txt.sizePolicy().hasHeightForWidth())
        self.max_iter_txt.setSizePolicy(sizePolicy)
        self.max_iter_txt.setMinimumSize(QtCore.QSize(130, 25))
        self.max_iter_txt.setMaximumSize(QtCore.QSize(200, 25))
        self.max_iter_txt.setObjectName("max_iter_txt")
        self.horizontalLayout_2.addWidget(self.max_iter_txt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.optimize_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optimize_btn.sizePolicy().hasHeightForWidth())
        self.optimize_btn.setSizePolicy(sizePolicy)
        self.optimize_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.optimize_btn.setObjectName("optimize_btn")
        self.verticalLayout.addWidget(self.optimize_btn)
        self.resultHistory = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultHistory.sizePolicy().hasHeightForWidth())
        self.resultHistory.setSizePolicy(sizePolicy)
        self.resultHistory.setMinimumSize(QtCore.QSize(0, 30))
        self.resultHistory.setObjectName("resultHistory")
        self.verticalLayout.addWidget(self.resultHistory)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.editgen_btn.setText(_translate("MainWindow", "Edit Generators"))
        self.editnetwork_btn.setText(_translate("MainWindow", "Edit Network"))
        self.max_iter_label.setText(_translate("MainWindow", "Maximum number of iterations:"))
        self.optimize_btn.setText(_translate("MainWindow", "Optimize"))
        self.resultHistory.setText(_translate("MainWindow", "Display Results"))
import dispatching_img_rc
