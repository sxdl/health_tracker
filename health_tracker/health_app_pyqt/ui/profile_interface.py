# codeing = utf-8
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget

from qfluentwidgets import FluentIcon as FIF, toggleTheme, MessageBoxBase, SubtitleLabel, LineEdit, BodyLabel, ComboBox, CalendarPicker
from .profile_interface_ui import Ui_ProfileInterface

from ..config import *
from ...tracker import User

class CustomMessageBox(MessageBoxBase):
    """ Custom message box """
    user_info_updated = pyqtSignal(User, str, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel('Edit profile', self)

        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.BodyLabel = BodyLabel(self)
        self.BodyLabel.setObjectName("BodyLabel")
        self.viewLayout.addWidget(self.BodyLabel)
        self.nameEdit = LineEdit(self)
        self.nameEdit.setText("")
        self.nameEdit.setFrame(True)
        self.nameEdit.setPlaceholderText("")
        self.nameEdit.setProperty("transparent", True)
        self.nameEdit.setObjectName("nameEdit")
        self.viewLayout.addWidget(self.nameEdit)
        self.BodyLabel_2 = BodyLabel(self)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.viewLayout.addWidget(self.BodyLabel_2)
        self.heightEdit = LineEdit(self)
        self.heightEdit.setObjectName("heightEdit")
        self.viewLayout.addWidget(self.heightEdit)
        self.BodyLabel_3 = BodyLabel(self)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.viewLayout.addWidget(self.BodyLabel_3)
        self.weightEdit = LineEdit(self)
        self.weightEdit.setObjectName("weightEdit")
        self.viewLayout.addWidget(self.weightEdit)
        self.BodyLabel_5 = BodyLabel(self)
        self.BodyLabel_5.setObjectName("BodyLabel_5")
        self.viewLayout.addWidget(self.BodyLabel_5)
        self.genderComboBox = ComboBox(self)
        self.genderComboBox.setText("")
        self.genderComboBox.setObjectName("genderComboBox")
        self.viewLayout.addWidget(self.genderComboBox)
        self.BodyLabel_4 = BodyLabel(self)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.viewLayout.addWidget(self.BodyLabel_4)
        self.birthdayCalendarPicker = CalendarPicker(self)
        self.birthdayCalendarPicker.setObjectName("birthdayCalendarPicker")
        self.viewLayout.addWidget(self.birthdayCalendarPicker)

        # set lable text
        self.BodyLabel.setText('Name')
        self.BodyLabel_2.setText('Height')
        self.BodyLabel_3.setText('Weight')
        self.BodyLabel_5.setText('Gender')
        self.BodyLabel_4.setText('Birthday')

        # set genderComboBox
        self.genderComboBox.setPlaceholderText("Select your gender")
        self.genderComboBox.addItems(["Male", "Female", "Other"])
        self.genderComboBox.setCurrentIndex(-1)

        # change the text of button
        self.yesButton.setText('Save')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        # when save button is clicked
        self.yesButton.clicked.connect(self.on_save)

    def on_save(self):
        """
        save button click event
        """
        user_name = self.nameEdit.text()
        user_height = self.heightEdit.text()
        user_weight = self.weightEdit.text()
        user_gender = self.genderComboBox.currentText()
        user_birth = self.birthdayCalendarPicker.getDate().toString("yyyy-MM-dd")
        user_id = "0"

        updated_user = User(user_id, user_name, user_birth, user_height, user_weight)
        self.user_info_updated.emit(updated_user, user_gender, user_birth)  # 发射信号



class ProfileInterface(QWidget, Ui_ProfileInterface):
    def __init__(self, user: User, parent = None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.user = user
        self.profile = self.user.get_profile()

        self.themeButton.setIcon(FIF.CONSTRACT)
        self.themeButton.setToolTip("Change Theme")
        self.themeButton.clicked.connect(lambda: toggleTheme(True))

        self.GitHubButton.setIcon(FIF.GITHUB)
        self.GitHubButton.setToolTip("GitHub")
        self.GitHubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(GITHUB)))

        self.editButton.setIcon(FIF.EDIT)
        self.editButton.setToolTip("Edit Profile")
        self.editButton.clicked.connect(self.on_edit)

        # 设置显示用户信息
        # TODO: 此处数据接口较混乱，暂时没看懂，不清楚如何调取用户的性别年龄等，先给出名字和UID示例，其余信息设置方法类似
        self.nameLabel.setText(self.user.name)
        self.UIDLabel.setText(self.user.user_id)
        self.heightLabel.setText(self.profile.height)
        self.weightLabel.setText(self.profile.weight)
        self.genderLabel.setText(self.profile.gender)
        self.ageLabel.setText(self.profile.birth)


    def on_edit(self):
        print("edit profile")
        msg = CustomMessageBox(self)
        msg.user_info_updated.connect(self.update_user_info)  # 连接信号到槽函数
        msg.show()
        msg.exec_()
    
    
    def update_user_info(self, updated_user, updated_gender, updated_birth):
        self.user = updated_user

        self.user.profile.update_data_by_field("gender", updated_gender)
        self.user.profile.update_data_by_field("birth", updated_birth)  # 修改这行
        self.user.profile.update_data_by_field("height", self.user.height)
        self.user.profile.update_data_by_field("weight", self.user.weight)

        self.nameLabel.setText(self.user.name)
        self.UIDLabel.setText(self.user.user_id)
        self.heightLabel.setText(self.user.height)
        self.weightLabel.setText(self.user.weight)
        self.genderLabel.setText(updated_gender)
        self.ageLabel.setText(updated_birth)



