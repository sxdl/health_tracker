import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl, QPoint
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget, QAction

from qfluentwidgets import FluentIcon as FIF, RoundMenu, toggleTheme, InfoBarManager, InfoBar, InfoBarPosition
from .device_interface_ui import Ui_DeviceInterface

from ..config import *
from ...tracker import User

@InfoBarManager.register('Custom')
class CustomInfoBarManager(InfoBarManager):
    """ Custom info bar manager """

    def _pos(self, infoBar: InfoBar, parentSize=None):
        p = infoBar.parent()
        parentSize = parentSize or p.size()

        # the position of first info bar
        x = (parentSize.width() - infoBar.width()) // 2
        y = (parentSize.height() - infoBar.height()) // 2 + 200

        # get the position of current info bar
        index = self.infoBars[p].index(infoBar)
        for bar in self.infoBars[p][0:index]:
            y += (bar.height() + self.spacing)

        return QPoint(x, y)

    def _slideStartPos(self, infoBar: InfoBar):
        pos = self._pos(infoBar)
        return QPoint(pos.x(), pos.y() - 16)

class DeviceInterface(QWidget, Ui_DeviceInterface):
    def __init__(self, user: User, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.user = user

        # 获取用户数据
        self.latest_data = self.user.activity_data.get_latest_daily_total()
        self.steps = self.latest_data["steps"]
        self.distance = self.latest_data["distance"]
        self.flights_climbed = self.latest_data["flights_climbed"]
        self.active_energy_burned = self.latest_data["active_energy_burned"]

        # # 设备卡片
        # self.menu = RoundMenu(parent=self)
        # self.menu.addAction(QAction(FIF.REMOVE.icon(), 'Remove'))
        # self.menu.addAction(QAction(FIF.SHARE.icon(), 'Share'))
        #
        # self.deviceButton1.setIcon(FIF.MORE)
        # self.deviceButton2.setIcon(FIF.MORE)
        # self.deviceButton1.setMenu(self.menu)
        # self.deviceButton2.setMenu(self.menu)

        self.addDeviceButton.setIcon(FIF.ADD_TO)

        self.themeButton.setIcon(FIF.CONSTRACT)
        self.themeButton.setToolTip("Change Theme")
        self.themeButton.clicked.connect(lambda: toggleTheme(True))

        self.GitHubButton.setIcon(FIF.GITHUB)
        self.GitHubButton.setToolTip("GitHub")
        self.GitHubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(GITHUB)))

        self.deviceButton1.clicked.connect(self.createSuccessInfoBar)
        self.deviceButton2.clicked.connect(self.createSuccessInfoBar)

    def createSuccessInfoBar(self):
        # convenient class mothod
        InfoBar.success(
            title='Removal Successful',
            content="The device has been removed successfully.",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )


