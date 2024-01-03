import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QAction

from qfluentwidgets import FluentIcon as FIF, RoundMenu
from .device_interface_ui import Ui_DeviceInterface

from ...tracker import User

class DeviceInterface(QWidget, Ui_DeviceInterface):
    def __init__(self, user: User, parent = None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.user = user

        # 获取用户数据
        self.latest_data = self.user.activity_data.get_latest_daily_total()
        self.steps = self.latest_data["steps"]
        self.distance = self.latest_data["distance"]
        self.flights_climbed = self.latest_data["flights_climbed"]
        self.active_energy_burned = self.latest_data["active_energy_burned"]

        # 设备卡片
        self.menu = RoundMenu(parent=self)
        self.menu.addAction(QAction(FIF.REMOVE.icon(), 'Remove'))
        self.menu.addAction(QAction(FIF.SHARE.icon(), 'Share'))


        self.deviceButton1.setIcon(FIF.MORE)
        self.deviceButton2.setIcon(FIF.MORE)
        self.deviceButton1.setMenu(self.menu)
        self.deviceButton2.setMenu(self.menu)
        
        self.addDeviceButton.setIcon(FIF.ADD)


