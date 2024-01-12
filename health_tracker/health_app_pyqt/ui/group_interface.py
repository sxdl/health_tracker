import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget, QAction, QStackedWidget

from qfluentwidgets import FluentIcon as FIF, RoundMenu, toggleTheme
from .group_interface_ui import Ui_GroupInterface

from ..config import *
from ...tracker import User

from .group_stack_default_page import GroupStackDefaultPage
from .group_stack_group_list_page import GroupStackGroupListPage


class GroupInterface(QWidget, Ui_GroupInterface):
    def __init__(self, user: User, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.groupThemeButton.setIcon(FIF.CONSTRACT)
        self.groupThemeButton.setToolTip("Change Theme")
        self.groupThemeButton.clicked.connect(lambda: toggleTheme(True))

        self.GitHubButton.setIcon(FIF.GITHUB)
        self.GitHubButton.setToolTip("GitHub")
        self.GitHubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(GITHUB)))

        # stacked pages
        # self.defaultPage = GroupStackDefaultPage()
        # self.groupListPage = GroupStackGroupListPage()
        #
        # self.stackedWidget = QStackedWidget()
        # self.verticalLayout.addWidget(self.stackedWidget)
        #
        # self.stackedWidget.addWidget(self.defaultPage)
        # self.stackedWidget.addWidget(self.groupListPage)

        self.stackedWidget.setCurrentIndex(0)

    def switch_2_default_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_2_group_list_page(self):
        self.stackedWidget.setCurrentIndex(1)
