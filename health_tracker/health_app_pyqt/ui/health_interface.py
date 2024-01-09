# codeing = utf-8
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget

from qfluentwidgets import FluentIcon as FIF, toggleTheme
from .health_interface_ui import Ui_HealthInterface

from ..config import *
from ...tracker import User


class HealthInterface(QWidget, Ui_HealthInterface):
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
        self.exercise_minutes = self.latest_data["exercise_minutes"]  # 锻炼时长
        self.active_hours = self.latest_data["active_hours"]  # 活动小时数

        # 卡路里显示
        self.caloriesButton1.setIcon(FIF.MORE)
        self.caloriesNum.setText(str(int(self.active_energy_burned)))
        self.caloriesTarget = 27000
        self.caloriesProgressBar.setValue(min(int(self.active_energy_burned / self.caloriesTarget * 100), 100))
        
        # 时间显示
        self.timeButton1.setIcon(FIF.MORE)
        self.timeTarget = 12
        self.timeNum.setText(f"{int(self.active_hours)}")
        self.timeProgressBar.setValue(min(int(self.active_hours / self.timeTarget * 100), 100))

        # 步数显示
        self.stepsButton1.setIcon(FIF.MORE)
        self.stepsNum.setText(str(int(self.steps)))
        self.stepsTarget = 30000
        self.stepsProgressBar.setValue(min(int(self.steps / self.stepsTarget * 100), 100))

        # 距离显示
        self.distanceButton1.setIcon(FIF.MORE)
        self.distanceNum.setText(str(int(self.distance)))
        self.distanceTarget = 60
        self.distanceProgressBar.setValue(min(int(self.distance / self.distanceTarget * 100), 100))

        self.themeButton.setIcon(FIF.CONSTRACT)
        self.themeButton.setToolTip("Change Theme")
        self.themeButton.clicked.connect(lambda: toggleTheme(True))

        self.GitHubButton.setIcon(FIF.GITHUB)
        self.GitHubButton.setToolTip("GitHub")
        self.GitHubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(GITHUB)))



        