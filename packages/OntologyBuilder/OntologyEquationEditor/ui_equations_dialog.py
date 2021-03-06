# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_equations_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(773, 452)
        self.labelNetwork = QtWidgets.QLabel(Dialog)
        self.labelNetwork.setGeometry(QtCore.QRect(20, 20, 741, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelNetwork.setFont(font)
        self.labelNetwork.setObjectName("labelNetwork")
        self.groupEquationEditor = QtWidgets.QGroupBox(Dialog)
        self.groupEquationEditor.setGeometry(QtCore.QRect(10, 90, 741, 271))
        self.groupEquationEditor.setObjectName("groupEquationEditor")
        self.lineNewVariable = QtWidgets.QLineEdit(self.groupEquationEditor)
        self.lineNewVariable.setGeometry(QtCore.QRect(11, 50, 181, 27))
        self.lineNewVariable.setObjectName("lineNewVariable")
        self.label_7 = QtWidgets.QLabel(self.groupEquationEditor)
        self.label_7.setGeometry(QtCore.QRect(200, 50, 16, 17))
        self.label_7.setObjectName("label_7")
        self.lineExpression = QtWidgets.QLineEdit(self.groupEquationEditor)
        self.lineExpression.setGeometry(QtCore.QRect(220, 50, 511, 27))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.lineExpression.setFont(font)
        self.lineExpression.setObjectName("lineExpression")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupEquationEditor)
        self.textBrowser.setGeometry(QtCore.QRect(10, 90, 721, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(self.groupEquationEditor)
        self.layoutWidget.setGeometry(QtCore.QRect(430, -11, 178, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushAccept = QtWidgets.QPushButton(self.layoutWidget)
        self.pushAccept.setMinimumSize(QtCore.QSize(85, 0))
        self.pushAccept.setMaximumSize(QtCore.QSize(85, 16777215))
        self.pushAccept.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color :rgb(255, 255, 255)")
        self.pushAccept.setText("")
        self.pushAccept.setObjectName("pushAccept")
        self.horizontalLayout_13.addWidget(self.pushAccept)
        self.pushDeleteEquation = QtWidgets.QPushButton(self.layoutWidget)
        self.pushDeleteEquation.setMinimumSize(QtCore.QSize(85, 0))
        self.pushDeleteEquation.setMaximumSize(QtCore.QSize(85, 16777215))
        self.pushDeleteEquation.setStyleSheet("background-color: rgb(255, 17, 0);\n"
"color:rgb(255, 255, 255)")
        self.pushDeleteEquation.setText("")
        self.pushDeleteEquation.setObjectName("pushDeleteEquation")
        self.horizontalLayout_13.addWidget(self.pushDeleteEquation)
        self.lineDocumentation = QtWidgets.QLineEdit(self.groupEquationEditor)
        self.lineDocumentation.setGeometry(QtCore.QRect(10, 230, 721, 27))
        self.lineDocumentation.setText("")
        self.lineDocumentation.setObjectName("lineDocumentation")
        self.layoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_5.setGeometry(QtCore.QRect(20, 370, 711, 61))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_8.setStyleSheet("background-color: rgb(148, 148, 56);\n"
"color :rgb(255, 255, 255)")
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_15.addWidget(self.label_8)
        self.pushPickVariables = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushPickVariables.setObjectName("pushPickVariables")
        self.horizontalLayout_15.addWidget(self.pushPickVariables)
        self.pushPickIndices = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushPickIndices.setObjectName("pushPickIndices")
        self.horizontalLayout_15.addWidget(self.pushPickIndices)
        self.pushPickOperations = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushPickOperations.setObjectName("pushPickOperations")
        self.horizontalLayout_15.addWidget(self.pushPickOperations)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushCancel = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushCancel.setText("")
        self.pushCancel.setObjectName("pushCancel")
        self.horizontalLayout_16.addWidget(self.pushCancel)
        self.pushResetInterface = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushResetInterface.setText("")
        self.pushResetInterface.setObjectName("pushResetInterface")
        self.horizontalLayout_16.addWidget(self.pushResetInterface)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_16)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelNetwork.setText(_translate("Dialog", "TextLabel"))
        self.groupEquationEditor.setToolTip(_translate("Dialog", "Equation editor"))
        self.groupEquationEditor.setTitle(_translate("Dialog", "Equation Editor:  Variable := Expression"))
        self.lineNewVariable.setToolTip(_translate("Dialog", "variable field"))
        self.label_7.setText(_translate("Dialog", ":="))
        self.lineExpression.setToolTip(_translate("Dialog", "equation editor field -- press return when finished"))
        self.pushAccept.setToolTip(_translate("Dialog", "puts things in place and closes equation editor"))
        self.lineDocumentation.setPlaceholderText(_translate("Dialog", "describe equation"))
        self.label_8.setToolTip(_translate("Dialog", "Pick tables"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">  pick tables  </span></p></body></html>"))
        self.pushPickVariables.setToolTip(_translate("Dialog", "pick variable table"))
        self.pushPickVariables.setText(_translate("Dialog", "variables"))
        self.pushPickIndices.setToolTip(_translate("Dialog", "pick index table"))
        self.pushPickIndices.setText(_translate("Dialog", "indices"))
        self.pushPickOperations.setToolTip(_translate("Dialog", "pick operations"))
        self.pushPickOperations.setText(_translate("Dialog", "operations"))
        self.pushCancel.setToolTip(_translate("Dialog", "reset closes equation editor clears alias table"))
        self.pushResetInterface.setToolTip(_translate("Dialog", "reset closes equation editor clears alias table"))
