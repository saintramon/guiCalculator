

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calcWindow(object):
    def setupUi(self, calcWindow):
        calcWindow.setObjectName("calcWindow")
        calcWindow.resize(201, 249)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(calcWindow.sizePolicy().hasHeightForWidth())
        calcWindow.setSizePolicy(sizePolicy)
        calcWindow.setFixedSize(201, 249)
        calcWindow.setWindowTitle("Calculator")
        self.caluclationBox = QtWidgets.QTextEdit(calcWindow)
        self.caluclationBox.setGeometry(QtCore.QRect(0, 0, 201, 51))
        self.caluclationBox.setStyleSheet("background-color:rgb(128, 128, 128)")
        self.caluclationBox.setObjectName("caluclationBox")

        self.num7_button = QtWidgets.QPushButton(calcWindow)
        self.num7_button.setGeometry(QtCore.QRect(0, 50, 51, 51))
        self.num7_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255);")
        self.num7_button.setObjectName("num7_button")

        self.num8_button = QtWidgets.QPushButton(calcWindow)
        self.num8_button.setGeometry(QtCore.QRect(50, 50, 51, 51))
        self.num8_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255);")
        self.num8_button.setObjectName("num8_button")

        self.num9_button = QtWidgets.QPushButton(calcWindow)
        self.num9_button.setGeometry(QtCore.QRect(100, 50, 51, 51))
        self.num9_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255);")
        self.num9_button.setObjectName("num9_button")

        self.operatorAddition = QtWidgets.QPushButton(calcWindow)
        self.operatorAddition.setGeometry(QtCore.QRect(150, 50, 51, 51))
        self.operatorAddition.setStyleSheet("background-color:rgb(255, 170, 0);")
        self.operatorAddition.setObjectName("operatorAddition")

        self.num4_button = QtWidgets.QPushButton(calcWindow)
        self.num4_button.setGeometry(QtCore.QRect(0, 100, 51, 51))
        self.num4_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255)")
        self.num4_button.setObjectName("num4_button")

        self.num5_button = QtWidgets.QPushButton(calcWindow)
        self.num5_button.setGeometry(QtCore.QRect(50, 100, 51, 51))
        self.num5_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255)")
        self.num5_button.setObjectName("num5_button")

        self.num6_button = QtWidgets.QPushButton(calcWindow)
        self.num6_button.setGeometry(QtCore.QRect(100, 100, 51, 51))
        self.num6_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255)")
        self.num6_button.setObjectName("num6_button")

        self.operatorSubtraction = QtWidgets.QPushButton(calcWindow)
        self.operatorSubtraction.setGeometry(QtCore.QRect(150, 100, 51, 51))
        self.operatorSubtraction.setStyleSheet("background-color:rgb(255, 170, 0)")
        self.operatorSubtraction.setObjectName("operatorSubtraction")

        self.num1_button = QtWidgets.QPushButton(calcWindow)
        self.num1_button.setGeometry(QtCore.QRect(0, 150, 51, 51))
        self.num1_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255)")
        self.num1_button.setObjectName("num1_button")

        self.num2_button = QtWidgets.QPushButton(calcWindow)
        self.num2_button.setGeometry(QtCore.QRect(50, 150, 51, 51))
        self.num2_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255)")
        self.num2_button.setObjectName("num2_button")

        self.num3_button = QtWidgets.QPushButton(calcWindow)
        self.num3_button.setGeometry(QtCore.QRect(100, 150, 51, 51))
        self.num3_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255)")
        self.num3_button.setObjectName("num3_button")

        self.clearButton = QtWidgets.QPushButton(calcWindow)
        self.clearButton.setGeometry(QtCore.QRect(150, 150, 51, 51))
        self.clearButton.setStyleSheet("background-color:rgb(255, 170, 0)")
        self.clearButton.setObjectName("clearButton")

        self.numPoint_button = QtWidgets.QPushButton(calcWindow)
        self.numPoint_button.setGeometry(QtCore.QRect(0, 200, 51, 51))
        self.numPoint_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255)")
        self.numPoint_button.setObjectName("numPoint_button")

        self.num0_button = QtWidgets.QPushButton(calcWindow)
        self.num0_button.setGeometry(QtCore.QRect(50, 200, 51, 51))
        self.num0_button.setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255)")
        self.num0_button.setObjectName("num0_button")

        self.numEquals_button = QtWidgets.QPushButton(calcWindow)
        self.numEquals_button.setGeometry(QtCore.QRect(100, 200, 101, 51))
        self.numEquals_button.setStyleSheet("background-color:rgb(150, 150, 150)")
        self.numEquals_button.setObjectName("numEquals_button")

        self.retranslateUi(calcWindow)
        QtCore.QMetaObject.connectSlotsByName(calcWindow)

    def retranslateUi(self, calcWindow):
        _translate = QtCore.QCoreApplication.translate
        calcWindow.setWindowTitle(_translate("calcWindow", "Dialog"))
        self.caluclationBox.setHtml(_translate(
        "calcWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">0</span></p></body></html>"))
        self.num7_button.setText(_translate("calcWindow", "7"))

        self.num8_button.setText(_translate("calcWindow", "8"))

        self.num9_button.setText(_translate("calcWindow", "9"))

        self.operatorAddition.setText(_translate("calcWindow", "+"))

        self.num4_button.setText(_translate("calcWindow", "4"))

        self.num5_button.setText(_translate("calcWindow", "5"))

        self.num6_button.setText(_translate("calcWindow", "6"))

        self.operatorSubtraction.setText(_translate("calcWindow", "-"))

        self.num1_button.setText(_translate("calcWindow", "1"))

        self.num2_button.setText(_translate("calcWindow", "2"))

        self.num3_button.setText(_translate("calcWindow", "3"))

        self.clearButton.setText(_translate("calcWindow", "AC"))

        self.numPoint_button.setText(_translate("calcWindow", "."))

        self.num0_button.setText(_translate("calcWindow", "0"))

        self.numEquals_button.setText(_translate("calcWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calcWindow = QtWidgets.QDialog()
    ui = Ui_calcWindow()
    ui.setupUi(calcWindow)
    calcWindow.show()
    sys.exit(app.exec_())
