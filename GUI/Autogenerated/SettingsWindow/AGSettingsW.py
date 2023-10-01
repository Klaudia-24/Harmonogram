# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AGSettingsW.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1000, 700))
        Form.setMaximumSize(QtCore.QSize(1000, 700))
        Form.setStyleSheet("background-color: rgb(221, 233, 238);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.applyBtn = QtWidgets.QPushButton(Form)
        self.applyBtn.setMinimumSize(QtCore.QSize(120, 40))
        self.applyBtn.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.applyBtn.setFont(font)
        self.applyBtn.setStyleSheet("background-color: rgb(135, 189, 216);")
        self.applyBtn.setObjectName("applyBtn")
        self.gridLayout_2.addWidget(self.applyBtn, 1, 5, 1, 1)
        self.okBtn = QtWidgets.QPushButton(Form)
        self.okBtn.setMinimumSize(QtCore.QSize(120, 40))
        self.okBtn.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.okBtn.setFont(font)
        self.okBtn.setStyleSheet("background-color: rgb(0, 204, 0);")
        self.okBtn.setObjectName("okBtn")
        self.gridLayout_2.addWidget(self.okBtn, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton(Form)
        self.cancelBtn.setMinimumSize(QtCore.QSize(120, 40))
        self.cancelBtn.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setStyleSheet("background-color: rgb(255, 51, 51);")
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout_2.addWidget(self.cancelBtn, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(183, 215, 232);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(2)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget.setIconSize(QtCore.QSize(0, 0))
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setGridSize(QtCore.QSize(0, 35))
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 3, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        self.applyBtn.setText(_translate("Form", "Apply"))
        self.okBtn.setText(_translate("Form", "Ok"))
        self.cancelBtn.setText(_translate("Form", "Cancel"))
