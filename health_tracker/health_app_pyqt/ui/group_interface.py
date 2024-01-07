import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QAction

from qfluentwidgets import FluentIcon as FIF, RoundMenu
from .group_interface_ui import Ui_GroupInterface

from ...tracker import User

class GroupInterface(QWidget, Ui_GroupInterface):
    def __init__(self, user: User, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        