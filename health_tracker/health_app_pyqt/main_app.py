# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

from qfluentwidgets import SplitFluentWindow, FluentIcon, setTheme, Theme

from .ui.health_interface import HealthInterface
from .ui.device_interface import DeviceInterface

from ..tracker import User
__all__ = ["run_app"]


class MainWindow(SplitFluentWindow):

    def __init__(self, user=None):
        super().__init__()

        self.setWindowIcon(QIcon(r'health_tracker\health_app_pyqt\resource\images\icon\icon.png'))
        self.setWindowTitle('Health Tracker')

        self.user = user if user else User("0", "游客")
        self.today_data = self.user.activity_data.get_latest_daily_total()

        # 添加子界面
        self.health_interface = HealthInterface(self.user, self)
        self.device_interface = DeviceInterface(self.user, self)

        self.addSubInterface(self.health_interface, FluentIcon.HEART,'Health Interface')
        self.addSubInterface(self.device_interface, FluentIcon.DICTIONARY_ADD,'Device Interface')


def run_app():
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    setTheme(Theme.DARK)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
    

