# coding:utf-8
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

from qfluentwidgets import SplitFluentWindow, FluentIcon, setTheme, Theme, SplashScreen, NavigationAvatarWidget, FluentIcon as FIF


from .ui.login_interface import LoginInterface
from .ui.main_window_interface import MainWindow

from ..tracker import User
__all__ = ["run_app"]


def run_app(user_id="0", user_name="游客"):
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    setTheme(Theme.DARK)

    loginInterface = LoginInterface()
    loginInterface.show()
    
    sys.exit(app.exec_())
    

