# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialogtext.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogText(object):
    def setupUi(self, DialogText):
        DialogText.setObjectName("DialogText")
        DialogText.resize(446, 348)
        self.gridLayout = QtWidgets.QGridLayout(DialogText)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(DialogText)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.retranslateUi(DialogText)
        QtCore.QMetaObject.connectSlotsByName(DialogText)

    def retranslateUi(self, DialogText):
        _translate = QtCore.QCoreApplication.translate
        DialogText.setWindowTitle(_translate("DialogText", "Dialog"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogText = QtWidgets.QDialog()
    ui = Ui_DialogText()
    ui.setupUi(DialogText)
    DialogText.show()
    sys.exit(app.exec_())
