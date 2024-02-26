# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# Form implementation generated from reading ui file '主界面ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.





class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(1280, 832)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.listView = QtWidgets.QListView(self.dockWidgetContents)
        self.listView.setGeometry(QtCore.QRect(-190, -40, 1471, 861))
        self.listView.setStyleSheet("background-image: url(:/001/bk.jpg);")
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(170, 240, 171, 51))
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 159);\n"
"font: 24pt \"Lantinghei SC\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 330, 171, 51))
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 159);\n"
"font: 24pt \"Lantinghei SC\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 420, 171, 51))
        self.pushButton_3.setStyleSheet("background-color: rgba(255, 255, 255, 159);\n"
"font: 24pt \"Lantinghei SC\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.dockWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(370, 70, 621, 111))
        self.textEdit.setStyleSheet("background-color: rgba(255, 255, 255, 159);\n"
"font: 24pt \"Lantinghei SC\";")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        DockWidget.setWidget(self.dockWidgetContents)
        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "DockWidget"))
        self.pushButton.setText(_translate("DockWidget", "景点榜单"))
        self.pushButton_2.setText(_translate("DockWidget", "地图查询"))
        self.pushButton_3.setText(_translate("DockWidget", "个性化定制"))
        self.textEdit.setHtml(_translate("DockWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lantinghei SC\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600; vertical-align:sub;\">威海旅游咨询系统</span></p></body></html>"))
import bkground_rc



#以上内容为“主界面ui.ui”通过pycharm外部工具转换而来
#以下为自主编写内容
class DockWidget(QtWidgets.QDockWidget, Ui_DockWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('威海旅游咨询系统')
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)#设置高分屏适应
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dockWidget = DockWidget()
    dockWidget.show()
    sys.exit(app.exec_())