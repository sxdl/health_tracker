# codeing = utf-8
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget

from qfluentwidgets import FluentIcon as FIF, toggleTheme
from .profile_interface_ui import Ui_ProfileInterface

from ..config import *
from ...tracker import User

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

        # 设置显示用户信息
        # TODO: 此处数据接口较混乱，暂时没看懂，不清楚如何调取用户的性别年龄等，先给出名字和UID示例，其余信息设置方法类似
        self.nameLabel.setText(self.user.name)
        self.UIDLabel.setText(self.user.user_id)
        self.genderLabel.setText(self.profile.gender)
        self.ageLabel.setText(self.profile.birth)


        # TODO: 设置显示历史数据



