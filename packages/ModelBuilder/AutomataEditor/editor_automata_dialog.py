# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor_automata_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(1224, 968)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeIncrement(QtCore.QSize(10, 10))
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 1201, 881))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_mouse_automat = QtWidgets.QWidget()
        self.tab_mouse_automat.setObjectName("tab_mouse_automat")
        self.groupSelections = QtWidgets.QGroupBox(self.tab_mouse_automat)
        self.groupSelections.setGeometry(QtCore.QRect(10, 10, 1021, 281))
        self.groupSelections.setObjectName("groupSelections")
        self.layoutWidget = QtWidgets.QWidget(self.groupSelections)
        self.layoutWidget.setGeometry(QtCore.QRect(680, 30, 321, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.listCursors = QtWidgets.QListWidget(self.layoutWidget)
        self.listCursors.setObjectName("listCursors")
        self.verticalLayout_4.addWidget(self.listCursors)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupSelections)
        self.layoutWidget1.setGeometry(QtCore.QRect(16, 30, 651, 241))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listSelectState = QtWidgets.QListWidget(self.layoutWidget1)
        self.listSelectState.setObjectName("listSelectState")
        self.verticalLayout.addWidget(self.listSelectState)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.listActions = QtWidgets.QListWidget(self.layoutWidget1)
        self.listActions.setObjectName("listActions")
        self.verticalLayout_3.addWidget(self.listActions)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.listStates = QtWidgets.QListWidget(self.layoutWidget1)
        self.listStates.setObjectName("listStates")
        self.verticalLayout_2.addWidget(self.listStates)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.tableState = QtWidgets.QTableWidget(self.tab_mouse_automat)
        self.tableState.setGeometry(QtCore.QRect(30, 310, 1141, 521))
        self.tableState.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableState.setObjectName("tableState")
        self.tableState.setColumnCount(6)
        self.tableState.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableState.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableState.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableState.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableState.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableState.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableState.setHorizontalHeaderItem(5, item)
        self.tableState.horizontalHeader().setDefaultSectionSize(150)
        self.tabWidget.addTab(self.tab_mouse_automat, "")
        self.tab_key_automat = QtWidgets.QWidget()
        self.tab_key_automat.setObjectName("tab_key_automat")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_key_automat)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 300, 1001, 461))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridlayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridlayout.setContentsMargins(5, 5, 5, 5)
        self.gridlayout.setObjectName("gridlayout")
        self.tableKeyAutomaton = QtWidgets.QTableWidget(self.layoutWidget_2)
        self.tableKeyAutomaton.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableKeyAutomaton.setObjectName("tableKeyAutomaton")
        self.tableKeyAutomaton.setColumnCount(3)
        self.tableKeyAutomaton.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableKeyAutomaton.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableKeyAutomaton.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableKeyAutomaton.setHorizontalHeaderItem(2, item)
        self.tableKeyAutomaton.horizontalHeader().setDefaultSectionSize(150)
        self.gridlayout.addWidget(self.tableKeyAutomaton, 0, 0, 1, 3)
        self.pushAddKey = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushAddKey.setObjectName("pushAddKey")
        self.gridlayout.addWidget(self.pushAddKey, 1, 0, 1, 1)
        self.pushDeleteKey = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushDeleteKey.setObjectName("pushDeleteKey")
        self.gridlayout.addWidget(self.pushDeleteKey, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 2, 1, 1)
        self.groupSelection = QtWidgets.QGroupBox(self.tab_key_automat)
        self.groupSelection.setGeometry(QtCore.QRect(10, 10, 1031, 281))
        self.groupSelection.setObjectName("groupSelection")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupSelection)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 20, 951, 231))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 2, 1, 1)
        self.listKeysForKeyAutomaton = QtWidgets.QListWidget(self.layoutWidget2)
        self.listKeysForKeyAutomaton.setObjectName("listKeysForKeyAutomaton")
        self.gridLayout.addWidget(self.listKeysForKeyAutomaton, 1, 0, 1, 1)
        self.listStatesForKeyAutomaton = QtWidgets.QListWidget(self.layoutWidget2)
        self.listStatesForKeyAutomaton.setObjectName("listStatesForKeyAutomaton")
        self.gridLayout.addWidget(self.listStatesForKeyAutomaton, 1, 1, 1, 1)
        self.listActionsForKeyAutomaton = QtWidgets.QListWidget(self.layoutWidget2)
        self.listActionsForKeyAutomaton.setObjectName("listActionsForKeyAutomaton")
        self.gridLayout.addWidget(self.listActionsForKeyAutomaton, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_key_automat, "")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 271, 61))
        self.groupBox.setObjectName("groupBox")
        self.comboPhase = QtWidgets.QComboBox(self.groupBox)
        self.comboPhase.setGeometry(QtCore.QRect(10, 20, 151, 22))
        self.comboPhase.setObjectName("comboPhase")
        self.pushSaveAutomaton = QtWidgets.QPushButton(Dialog)
        self.pushSaveAutomaton.setGeometry(QtCore.QRect(500, 10, 71, 25))
        self.pushSaveAutomaton.setObjectName("pushSaveAutomaton")
        self.pushLaTex = QtWidgets.QPushButton(Dialog)
        self.pushLaTex.setGeometry(QtCore.QRect(500, 50, 97, 27))
        self.pushLaTex.setObjectName("pushLaTex")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupSelections.setTitle(_translate("Dialog", "Selections"))
        self.label_3.setText(_translate("Dialog", "cusor"))
        self.label.setText(_translate("Dialog", "selector"))
        self.label_2.setText(_translate("Dialog", "action"))
        self.label_4.setText(_translate("Dialog", "state"))
        item = self.tableState.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "object"))
        item = self.tableState.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "mouse left"))
        item = self.tableState.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "left: next state"))
        item = self.tableState.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "mouse right"))
        item = self.tableState.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "right: mouse"))
        item = self.tableState.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "cursor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mouse_automat), _translate("Dialog", "mouse"))
        item = self.tableKeyAutomaton.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "key"))
        item = self.tableKeyAutomaton.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "next state"))
        item = self.tableKeyAutomaton.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "GUI action"))
        self.pushAddKey.setText(_translate("Dialog", "add key"))
        self.pushDeleteKey.setText(_translate("Dialog", "delete key"))
        self.groupSelection.setTitle(_translate("Dialog", "Selection"))
        self.label_21.setText(_translate("Dialog", "key"))
        self.label_20.setText(_translate("Dialog", "state"))
        self.label_19.setText(_translate("Dialog", "action"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_key_automat), _translate("Dialog", "key"))
        self.groupBox.setTitle(_translate("Dialog", "select phase"))
        self.pushSaveAutomaton.setToolTip(_translate("Dialog", "saves and makes backup"))
        self.pushSaveAutomaton.setText(_translate("Dialog", "save"))
        self.pushLaTex.setText(_translate("Dialog", "LaTex"))