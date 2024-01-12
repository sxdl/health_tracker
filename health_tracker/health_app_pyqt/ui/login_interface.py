# codeing = utf-8
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget, QApplication


from qfluentwidgets import FluentIcon as FIF, toggleTheme, SplitTitleBar, setTheme, Theme
from qframelesswindow import AcrylicWindow
from .login_interface_ui import Ui_LoginInterface

from .main_window_interface import MainWindow
from ..config import *
from ...tracker import User

class LoginInterface(AcrylicWindow, Ui_LoginInterface):
    """
    登录界面
    """
    login_signal = pyqtSignal(User)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        setTheme(Theme.LIGHT)

        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.setWindowIcon(QIcon(r'health_tracker\health_app_pyqt\resource\images\icon\icon.png'))
        self.setWindowTitle('Health Tracker')

        self.windowEffect.setMicaEffect(self.winId(), False)
        self.setStyleSheet("LoginWindow{background: rgba(242, 242, 242, 0.8)}")
        self.titleBar.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px
            }
        """)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        self.genderComboBox.setPlaceholderText("Select your gender")
        self.genderComboBox.addItems(["Male", "Female", "Other"])
        self.genderComboBox.setCurrentIndex(-1)

        self.guestButton.clicked.connect(self.on_guest)
        self.loginButton.clicked.connect(self.on_login)


    def on_guest(self):
        # self.login_signal.emit(User("0", "游客"))
        w = MainWindow(User("0", "游客"))
        # 关闭登录界面
        self.close()
        w.show()
        print("Login as guest")

    def on_login(self):
        """
        登录按钮的槽函数
        """
        user_name = self.nameEdit.text()
        user_height = self.heightEdit.text()
        user_weight = self.weightEdit.text()
        # TODO: 此处性别信息未被使用
        user_gender = self.genderComboBox.currentText()
        user_birth = self.birthdayCalendarPicker.getDate().toString("yyyy-MM-dd")
        user_id = "0"

        # 创建用户并启动应用程序
        user = User(user_id, user_name, user_birth, user_height, user_weight)
        w = MainWindow(user)
        # 关闭登录界面
        self.close()
        w.show()

