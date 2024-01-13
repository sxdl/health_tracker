# codeing = utf-8
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl, QPoint
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget

from qfluentwidgets import FluentIcon as FIF, toggleTheme, MessageBoxBase, SubtitleLabel, TextEdit, LineEdit, InfoBarManager, InfoBar, InfoBarPosition
from .health_interface_ui import Ui_HealthInterface

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


class CaloriesTargetSettingMessageBox(MessageBoxBase):
    """ Custom message box for calories target setting """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel('Calories Target Setting', self)

        # Add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.caloriesEdit = LineEdit(self)
        self.caloriesEdit.setText(str(self.parent().caloriesTarget))
        self.caloriesEdit.setPlaceholderText("")
        self.caloriesEdit.setProperty("transparent", True)
        self.caloriesEdit.setObjectName("caloriesEdit")
        self.viewLayout.addWidget(self.caloriesEdit)
        
        # Change the text of buttons
        self.yesButton.setText('Save')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        # When save button is clicked
        self.yesButton.clicked.connect(self.on_save)

    def on_save(self):
        """
        Save button click event
        """
        self.parent().caloriesTarget = int(self.caloriesEdit.text())
        self.parent().createSuccessInfoBar()

class StepsTargetSettingMessageBox(MessageBoxBase):
    """ Custom message box for steps target setting """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel('Steps Target Setting', self)

        # Add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.stepsEdit = LineEdit(self)
        self.stepsEdit.setText(str(self.parent().stepsTarget))
        self.stepsEdit.setPlaceholderText("")
        self.stepsEdit.setProperty("transparent", True)
        self.stepsEdit.setObjectName("stepsEdit")
        self.viewLayout.addWidget(self.stepsEdit)
        
        # Change the text of buttons
        self.yesButton.setText('Save')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        # When save button is clicked
        self.yesButton.clicked.connect(self.on_save)

    def on_save(self):
        """
        Save button click event
        """
        self.parent().stepsTarget = int(self.stepsEdit.text())

class DistanceTargetSettingMessageBox(MessageBoxBase):
    """ Custom message box for distance target setting """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel('Distance Target Setting', self)

        # Add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.distanceEdit = LineEdit(self)
        self.distanceEdit.setText(str(self.parent().distanceTarget))
        self.distanceEdit.setPlaceholderText("")
        self.distanceEdit.setProperty("transparent", True)
        self.distanceEdit.setObjectName("distanceEdit")
        self.viewLayout.addWidget(self.distanceEdit)
        
        # Change the text of buttons
        self.yesButton.setText('Save')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        # When save button is clicked
        self.yesButton.clicked.connect(self.on_save)

    def on_save(self):
        """
        Save button click event
        """
        self.parent().distanceTarget = int(self.distanceEdit.text())

class TimeTargetSettingMessageBox(MessageBoxBase):
    """ Custom message box for time target setting """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel('Time Target Setting', self)

        # Add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.timeEdit = LineEdit(self)
        self.timeEdit.setText(str(self.parent().timeTarget))
        self.timeEdit.setPlaceholderText("")
        self.timeEdit.setProperty("transparent", True)
        self.timeEdit.setObjectName("timeEdit")
        self.viewLayout.addWidget(self.timeEdit)
        
        # Change the text of buttons
        self.yesButton.setText('Save')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        # When save button is clicked
        self.yesButton.clicked.connect(self.on_save)

    def on_save(self):
        """
        Save button click event
        """
        self.parent().timeTarget = int(self.timeEdit.text())

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
        self.caloriesTarget = 27000
        self.caloriesButton1.setIcon(FIF.MORE)
        self.caloriesButton1.setToolTip("Calories Target Setting")
        self.caloriesButton1.clicked.connect(self.on_calories_target_setting)
        self.caloriesNum.setText(str(int(self.active_energy_burned)))
        self.caloriesProgressBar.setValue(min(int(self.active_energy_burned / self.caloriesTarget * 100), 100))
        
        # 时间显示
        self.timeButton1.setIcon(FIF.MORE)
        self.timeTarget = 12
        self.timeButton1.setToolTip("Time Target Setting")
        self.timeButton1.clicked.connect(self.on_time_target_setting)
        self.timeNum.setText(f"{int(self.active_hours)}")
        self.timeProgressBar.setValue(min(int(self.active_hours / self.timeTarget * 100), 100))

        # 步数显示
        self.stepsButton1.setIcon(FIF.MORE)
        self.stepsTarget = 30000
        self.stepsNum.setText(str(int(self.steps)))
        self.stepsButton1.setToolTip("Steps Target Setting")
        self.stepsButton1.clicked.connect(self.on_steps_target_setting)
        self.stepsProgressBar.setValue(min(int(self.steps / self.stepsTarget * 100), 100))

        # 距离显示
        self.distanceTarget = 60
        self.distanceButton1.setIcon(FIF.MORE)
        self.distanceNum.setText(str(int(self.distance)))
        self.distanceButton1.setToolTip("Distance Target Setting")
        self.distanceButton1.clicked.connect(self.on_distance_target_setting)
        self.distanceProgressBar.setValue(min(int(self.distance / self.distanceTarget * 100), 100))

        self.themeButton.setIcon(FIF.CONSTRACT)
        self.themeButton.setToolTip("Change Theme")
        self.themeButton.clicked.connect(lambda: toggleTheme(True))

        self.GitHubButton.setIcon(FIF.GITHUB)
        self.GitHubButton.setToolTip("GitHub")
        self.GitHubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(GITHUB)))

    
    def on_calories_target_setting(self):
        """ calories target setting """
        self.messageBox = CaloriesTargetSettingMessageBox(self)
        self.messageBox.exec_()
        self.caloriesProgressBar.setValue(min(int(self.active_energy_burned / self.caloriesTarget * 100), 100))
        self.caloriesNum.setText(str(int(self.active_energy_burned)))

    def on_steps_target_setting(self):
        """ steps target setting """
        self.messageBox = StepsTargetSettingMessageBox(self)
        self.messageBox.exec_()
        self.stepsProgressBar.setValue(min(int(self.steps / self.stepsTarget * 100), 100))
        self.stepsNum.setText(str(int(self.steps)))

    def on_distance_target_setting(self):
        """ distance target setting """
        self.messageBox = DistanceTargetSettingMessageBox(self)
        self.messageBox.exec_()
        self.distanceProgressBar.setValue(min(int(self.distance / self.distanceTarget * 100), 100))
        self.distanceNum.setText(str(int(self.distance)))

    def on_time_target_setting(self):
        """ time target setting """
        self.messageBox = TimeTargetSettingMessageBox(self)
        self.messageBox.exec_()
        self.timeProgressBar.setValue(min(int(self.active_hours / self.timeTarget * 100), 100))
        self.timeNum.setText(f"{int(self.active_hours)}")

    def createSuccessInfoBar(self):
        # convenient class mothod
        InfoBar.success(
            title='Target Setting Successful',
            content='Your target has been set successfully.',
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )

