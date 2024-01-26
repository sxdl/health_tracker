# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GroupPage(object):
    def setupUi(self, GroupPage):
        GroupPage.setObjectName("GroupPage")
        GroupPage.resize(866, 571)
        self.horizontalLayout = QtWidgets.QHBoxLayout(GroupPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.nameLabel_0 = TitleLabel(GroupPage)
        self.nameLabel_0.setObjectName("nameLabel_0")
        self.verticalLayout_20.addWidget(self.nameLabel_0)
        self.SimpleCardWidget_5 = SimpleCardWidget(GroupPage)
        self.SimpleCardWidget_5.setMinimumSize(QtCore.QSize(0, 20))
        self.SimpleCardWidget_5.setObjectName("SimpleCardWidget_5")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.SimpleCardWidget_5)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(-1, 2, -1, -1)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.SubtitleLabel_10 = SubtitleLabel(self.SimpleCardWidget_5)
        self.SubtitleLabel_10.setObjectName("SubtitleLabel_10")
        self.horizontalLayout_19.addWidget(self.SubtitleLabel_10)
        self.announEditButton_0 = ToolButton(self.SimpleCardWidget_5)
        self.announEditButton_0.setObjectName("announEditButton_0")
        self.horizontalLayout_19.addWidget(self.announEditButton_0)
        self.verticalLayout_21.addLayout(self.horizontalLayout_19)
        self.announcementLabel_0 = CaptionLabel(self.SimpleCardWidget_5)
        self.announcementLabel_0.setObjectName("announcementLabel_0")
        self.verticalLayout_21.addWidget(self.announcementLabel_0)
        self.verticalLayout_20.addWidget(self.SimpleCardWidget_5)
        self.ElevatedCardWidget_3 = ElevatedCardWidget(GroupPage)
        self.ElevatedCardWidget_3.setObjectName("ElevatedCardWidget_3")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.ElevatedCardWidget_3)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.IconWidget_3 = IconWidget(self.ElevatedCardWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_3.sizePolicy().hasHeightForWidth())
        self.IconWidget_3.setSizePolicy(sizePolicy)
        self.IconWidget_3.setMinimumSize(QtCore.QSize(80, 80))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("health_tracker/health_app_pyqt/resource/images/icon/step.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_3.setIcon(icon)
        self.IconWidget_3.setObjectName("IconWidget_3")
        self.horizontalLayout_21.addWidget(self.IconWidget_3)
        self.verticalLayout_22.addLayout(self.horizontalLayout_21)
        self.SubtitleLabel_3 = SubtitleLabel(self.ElevatedCardWidget_3)
        self.SubtitleLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel_3.setObjectName("SubtitleLabel_3")
        self.verticalLayout_22.addWidget(self.SubtitleLabel_3)
        self.BodyLabel_3 = BodyLabel(self.ElevatedCardWidget_3)
        self.BodyLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.verticalLayout_22.addWidget(self.BodyLabel_3)
        self.horizontalLayout_20.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.IconWidget_10 = IconWidget(self.ElevatedCardWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_10.sizePolicy().hasHeightForWidth())
        self.IconWidget_10.setSizePolicy(sizePolicy)
        self.IconWidget_10.setMinimumSize(QtCore.QSize(80, 80))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("health_tracker/health_app_pyqt/resource/images/icon/chronometer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_10.setIcon(icon1)
        self.IconWidget_10.setObjectName("IconWidget_10")
        self.horizontalLayout_22.addWidget(self.IconWidget_10)
        self.verticalLayout_23.addLayout(self.horizontalLayout_22)
        self.SubtitleLabel_11 = SubtitleLabel(self.ElevatedCardWidget_3)
        self.SubtitleLabel_11.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel_11.setObjectName("SubtitleLabel_11")
        self.verticalLayout_23.addWidget(self.SubtitleLabel_11)
        self.BodyLabel_8 = BodyLabel(self.ElevatedCardWidget_3)
        self.BodyLabel_8.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_8.setObjectName("BodyLabel_8")
        self.verticalLayout_23.addWidget(self.BodyLabel_8)
        self.horizontalLayout_20.addLayout(self.verticalLayout_23)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.IconWidget_11 = IconWidget(self.ElevatedCardWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_11.sizePolicy().hasHeightForWidth())
        self.IconWidget_11.setSizePolicy(sizePolicy)
        self.IconWidget_11.setMinimumSize(QtCore.QSize(80, 80))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("health_tracker/health_app_pyqt/resource/images/icon/calories.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_11.setIcon(icon2)
        self.IconWidget_11.setObjectName("IconWidget_11")
        self.horizontalLayout_23.addWidget(self.IconWidget_11)
        self.verticalLayout_24.addLayout(self.horizontalLayout_23)
        self.SubtitleLabel_12 = SubtitleLabel(self.ElevatedCardWidget_3)
        self.SubtitleLabel_12.setAlignment(QtCore.Qt.AlignCenter)
        self.SubtitleLabel_12.setObjectName("SubtitleLabel_12")
        self.verticalLayout_24.addWidget(self.SubtitleLabel_12)
        self.BodyLabel_9 = BodyLabel(self.ElevatedCardWidget_3)
        self.BodyLabel_9.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel_9.setObjectName("BodyLabel_9")
        self.verticalLayout_24.addWidget(self.BodyLabel_9)
        self.horizontalLayout_20.addLayout(self.verticalLayout_24)
        self.verticalLayout_20.addWidget(self.ElevatedCardWidget_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_20)
        self.cardWidget = CardWidget(GroupPage)
        self.cardWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.cardWidget.setObjectName("cardWidget")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.cardWidget)
        self.verticalLayout_25.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.StrongBodyLabel_9 = StrongBodyLabel(self.cardWidget)
        self.StrongBodyLabel_9.setObjectName("StrongBodyLabel_9")
        self.verticalLayout_25.addWidget(self.StrongBodyLabel_9)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.IconWidget_12 = IconWidget(self.cardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget_12.sizePolicy().hasHeightForWidth())
        self.IconWidget_12.setSizePolicy(sizePolicy)
        self.IconWidget_12.setMinimumSize(QtCore.QSize(30, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("health_tracker/health_app_pyqt/resource/images/profile/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_12.setIcon(icon3)
        self.IconWidget_12.setObjectName("IconWidget_12")
        self.verticalLayout_26.addWidget(self.IconWidget_12)
        self.CaptionLabel_3 = CaptionLabel(self.cardWidget)
        self.CaptionLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptionLabel_3.setObjectName("CaptionLabel_3")
        self.verticalLayout_26.addWidget(self.CaptionLabel_3)
        self.horizontalLayout_24.addLayout(self.verticalLayout_26)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem1)
        self.verticalLayout_25.addLayout(self.horizontalLayout_24)
        self.StrongBodyLabel_10 = StrongBodyLabel(self.cardWidget)
        self.StrongBodyLabel_10.setObjectName("StrongBodyLabel_10")
        self.verticalLayout_25.addWidget(self.StrongBodyLabel_10)
        self.groupIDLabel_1 = CaptionLabel(self.cardWidget)
        self.groupIDLabel_1.setObjectName("groupIDLabel_1")
        self.verticalLayout_25.addWidget(self.groupIDLabel_1)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.StrongBodyLabel_11 = StrongBodyLabel(self.cardWidget)
        self.StrongBodyLabel_11.setObjectName("StrongBodyLabel_11")
        self.horizontalLayout_25.addWidget(self.StrongBodyLabel_11)
        self.qrcodeButton_0 = ToolButton(self.cardWidget)
        self.qrcodeButton_0.setObjectName("qrcodeButton_0")
        self.horizontalLayout_25.addWidget(self.qrcodeButton_0)
        self.verticalLayout_25.addLayout(self.horizontalLayout_25)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.cardWidget)
        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(GroupPage)
        QtCore.QMetaObject.connectSlotsByName(GroupPage)

    def retranslateUi(self, GroupPage):
        _translate = QtCore.QCoreApplication.translate
        GroupPage.setWindowTitle(_translate("GroupPage", "Form"))
        self.nameLabel_0.setText(_translate("GroupPage", "Group Name"))
        self.SubtitleLabel_10.setText(_translate("GroupPage", "📢 Announcement"))
        self.announcementLabel_0.setText(_translate("GroupPage", "The group owner is too lazy, didn\'t write anything"))
        self.SubtitleLabel_3.setText(_translate("GroupPage", "1"))
        self.BodyLabel_3.setText(_translate("GroupPage", "Step Rank"))
        self.SubtitleLabel_11.setText(_translate("GroupPage", "1"))
        self.BodyLabel_8.setText(_translate("GroupPage", "Time Rank"))
        self.SubtitleLabel_12.setText(_translate("GroupPage", "1"))
        self.BodyLabel_9.setText(_translate("GroupPage", "Calories Rank"))
        self.StrongBodyLabel_9.setText(_translate("GroupPage", "Group Members"))
        self.CaptionLabel_3.setText(_translate("GroupPage", "You"))
        self.StrongBodyLabel_10.setText(_translate("GroupPage", "Group ID"))
        self.groupIDLabel_1.setText(_translate("GroupPage", "20001"))
        self.StrongBodyLabel_11.setText(_translate("GroupPage", "Group QRCode"))
from qfluentwidgets import BodyLabel, CaptionLabel, CardWidget, ElevatedCardWidget, IconWidget, SimpleCardWidget, StrongBodyLabel, SubtitleLabel, TitleLabel, ToolButton
