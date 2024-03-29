# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Study\University\Y2T1\OOP\Health-Tracker\health_tracker\health_app_pyqt\ui\group_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GroupInterface(object):
    def setupUi(self, GroupInterface):
        GroupInterface.setObjectName("GroupInterface")
        GroupInterface.resize(1066, 813)
        self.verticalLayout = QtWidgets.QVBoxLayout(GroupInterface)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(966, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TitleLabel = TitleLabel(GroupInterface)
        self.TitleLabel.setProperty("pixelFontSize", 50)
        self.TitleLabel.setObjectName("TitleLabel")
        self.horizontalLayout.addWidget(self.TitleLabel)
        self.groupThemeButton = ToolButton(GroupInterface)
        self.groupThemeButton.setObjectName("groupThemeButton")
        self.horizontalLayout.addWidget(self.groupThemeButton)
        self.GitHubButton = ToolButton(GroupInterface)
        self.GitHubButton.setObjectName("GitHubButton")
        self.horizontalLayout.addWidget(self.GitHubButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SimpleCardWidget = SimpleCardWidget(GroupInterface)
        self.SimpleCardWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SimpleCardWidget)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SearchLineEdit = SearchLineEdit(self.SimpleCardWidget)
        self.SearchLineEdit.setObjectName("SearchLineEdit")
        self.horizontalLayout_4.addWidget(self.SearchLineEdit)
        self.createButton = ToolButton(self.SimpleCardWidget)
        self.createButton.setMinimumSize(QtCore.QSize(32, 32))
        self.createButton.setObjectName("createButton")
        self.horizontalLayout_4.addWidget(self.createButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.listWidget = ListWidget(self.SimpleCardWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_3.addWidget(self.SimpleCardWidget)
        self.SimpleCardWidget_2 = SimpleCardWidget(GroupInterface)
        self.SimpleCardWidget_2.setObjectName("SimpleCardWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.SimpleCardWidget_2)
        self.verticalLayout_4.setContentsMargins(-1, 2, 2, 2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.SimpleCardWidget_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.defaultPage = QtWidgets.QWidget()
        self.defaultPage.setObjectName("defaultPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.defaultPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.LargeTitleLabel = LargeTitleLabel(self.defaultPage)
        self.LargeTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LargeTitleLabel.setObjectName("LargeTitleLabel")
        self.verticalLayout_3.addWidget(self.LargeTitleLabel)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem2)
        self.createGroupButton = PrimaryPushButton(self.defaultPage)
        self.createGroupButton.setObjectName("createGroupButton")
        self.horizontalLayout_20.addWidget(self.createGroupButton)
        self.BodyLabel_3 = BodyLabel(self.defaultPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy)
        self.BodyLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.horizontalLayout_20.addWidget(self.BodyLabel_3)
        self.joinByCodeButton = PrimaryPushButton(self.defaultPage)
        self.joinByCodeButton.setObjectName("joinByCodeButton")
        self.horizontalLayout_20.addWidget(self.joinByCodeButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_20)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.stackedWidget.addWidget(self.defaultPage)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addWidget(self.SimpleCardWidget_2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(GroupInterface)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GroupInterface)

    def retranslateUi(self, GroupInterface):
        _translate = QtCore.QCoreApplication.translate
        GroupInterface.setWindowTitle(_translate("GroupInterface", "Form"))
        self.TitleLabel.setText(_translate("GroupInterface", "Group"))
        self.LargeTitleLabel.setText(_translate("GroupInterface", "Join a New Group"))
        self.createGroupButton.setText(_translate("GroupInterface", "Create a Group"))
        self.BodyLabel_3.setText(_translate("GroupInterface", "or"))
        self.joinByCodeButton.setText(_translate("GroupInterface", "Join by Group ID"))
from qfluentwidgets import BodyLabel, LargeTitleLabel, ListWidget, PrimaryPushButton, SearchLineEdit, SimpleCardWidget, TitleLabel, ToolButton
