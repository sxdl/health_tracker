# coding:utf-8
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

from qfluentwidgets import SplitFluentWindow, FluentIcon, setTheme, Theme

from .ui.health_interface import HealthInterface

__all__ = ["run_app"]


class MainWindow(SplitFluentWindow):

    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(r'health_tracker\health_app_pyqt\resource\images\icon\icon.png'))
        self.setWindowTitle('Health Tracker')

        self.health_interface = HealthInterface(self)

        self.addSubInterface(self.health_interface, FluentIcon.HEART,'Health Interface')


def run_app():
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    setTheme(Theme.DARK)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
    

