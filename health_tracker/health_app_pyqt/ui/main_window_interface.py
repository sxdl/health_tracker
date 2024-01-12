
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import SplitFluentWindow, FluentIcon

from .health_interface import HealthInterface
from .device_interface import DeviceInterface
from .data_interface import DataInterface
from .group_interface import GroupInterface
from .profile_interface import ProfileInterface

from ...tracker import User

class MainWindow(SplitFluentWindow):

    def __init__(self, user=None):
        super().__init__()

        self.setWindowIcon(QIcon(r'health_tracker\health_app_pyqt\resource\images\icon\icon.png'))
        self.setWindowTitle('Health Tracker')

        # 若开启云母效果，会与 WebEngineView 冲突
        self.updateFrameless()
        self.setMicaEffectEnabled(False)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        # 由于未知原因，原本长宽“除以二”的部分会导致窗口初始化时位置不在正中央，故未除以二
        self.move(w//2 - self.width(), h//2 - self.height())


        self.user = user if user else User("0", "游客")
        self.today_data = self.user.activity_data.get_latest_daily_total()

        # 添加子界面
        self.health_interface = HealthInterface(self.user, self)
        self.device_interface = DeviceInterface(self.user, self)
        self.data_interface = DataInterface(self.user, self)
        self.group_interface = GroupInterface(self.user, self)
        self.profile_interface = ProfileInterface(self.user, self)

        

        self.addSubInterface(self.health_interface, FluentIcon.HEART,'Health Interface')
        self.addSubInterface(self.device_interface, FluentIcon.DICTIONARY_ADD,'Device Interface')
        self.addSubInterface(self.data_interface, FluentIcon.PIE_SINGLE,'Data Interface')
        self.addSubInterface(self.group_interface, FluentIcon.IOT,'Group Interface')
        self.addSubInterface(self.profile_interface, FluentIcon.PEOPLE,'Profile Interface', position=Qt.BottomDockWidgetArea)


        # 添加设置
        self.navigationInterface.addItem(
            routeKey='settings',
            icon=FluentIcon.SETTING,
            text='Settings',
            position=Qt.BottomDockWidgetArea
        )

