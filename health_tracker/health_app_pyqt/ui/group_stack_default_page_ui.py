# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Study\University\Y2T1\OOP\Health-Tracker\health_tracker\health_app_pyqt\ui\group_stack_default_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GroupStackDefaultPage(object):
    def setupUi(self, GroupStackDefaultPage):
        GroupStackDefaultPage.setObjectName("GroupStackDefaultPage")
        GroupStackDefaultPage.resize(725, 510)
        self.gridLayout = QtWidgets.QGridLayout(GroupStackDefaultPage)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(GroupStackDefaultPage)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(GroupStackDefaultPage)
        QtCore.QMetaObject.connectSlotsByName(GroupStackDefaultPage)

    def retranslateUi(self, GroupStackDefaultPage):
        _translate = QtCore.QCoreApplication.translate
        GroupStackDefaultPage.setWindowTitle(_translate("GroupStackDefaultPage", "Form"))
        self.textBrowser.setHtml(_translate("GroupStackDefaultPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Default Page</p></body></html>"))
