# codeing = utf-8
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget, QAction

from qfluentwidgets import FluentIcon as FIF, toggleTheme, RoundMenu, setThemeColor, setTheme, Theme
from .setting_interface_ui import Ui_SettingInterface

from ..config import *
from ...tracker import User

class SettingInterface(QWidget, Ui_SettingInterface):
    """ Setting interface """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.themeButton.setIcon(FIF.CONSTRACT)
        self.themeButton.setToolTip("Change Theme")
        self.themeButton.clicked.connect(lambda: toggleTheme(True))

        self.GitHubButton.setIcon(FIF.GITHUB)
        self.GitHubButton.setToolTip("GitHub")
        self.GitHubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(GITHUB)))
        
        self.AcrylicIcon.setIcon(FIF.TRANSPARENT)
        self.AcrylicIcon.setToolTip("Acrylic Effect")

        self.themeIcon.setIcon(FIF.CONSTRACT)
        self.themeIcon.setToolTip("Change Theme")

        self.themeComboBox.addItems(["Light", "Dark", "Auto"])
        # 实现下拉框选中一个选项后，自动设置对应的主题
        self.themeComboBox.currentIndexChanged.connect(lambda: setTheme(Theme(self.themeComboBox.currentText())))

        self.colorIcon.setIcon(FIF.PALETTE)
        self.colorIcon.setToolTip("Change Color")
        self.colorButton.clicked.connect(setThemeColor)

        self.feedbackIcon.setIcon(FIF.FEEDBACK)
        self.feedbackIcon.setToolTip("Feedback")
        self.feedbackButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(FEEDBACK_URL)))



        



