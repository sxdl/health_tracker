# codeing = utf-8
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget

from qfluentwidgets import FluentIcon as FIF
from .profile_interface_ui import Ui_ProfileInterface

from ...tracker import User

class ProfileInterface(QWidget, Ui_ProfileInterface):
    def __init__(self, user: User, parent = None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.user = user

