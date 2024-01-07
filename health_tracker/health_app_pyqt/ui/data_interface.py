import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QAction

from qfluentwidgets import FluentIcon as FIF, RoundMenu
from .data_interface_ui import Ui_DataInterface

from ...tracker import User

class DataInterface(QWidget, Ui_DataInterface):
    def __init__(self, user: User, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


        