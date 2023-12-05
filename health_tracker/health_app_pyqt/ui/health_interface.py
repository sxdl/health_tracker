# codeing = utf-8
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget

from .health_interface_ui import Ui_HealthInterface

class HealthInterface(QWidget, Ui_HealthInterface):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setupUi(self)
