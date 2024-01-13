import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget, QAction, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView

from qfluentwidgets import FluentIcon as FIF, RoundMenu, toggleTheme
from .data_interface_ui import Ui_DataInterface

from ..config import *
from ...tracker import User
from ...tracker.file_handler import HTMLFileHandler


class DataInterface(QWidget, Ui_DataInterface):
    def __init__(self, user: User, parent=None):
            """
            Initializes the DataInterface class.

            Args:
                user (User): The user object.
                parent (QWidget, optional): The parent widget. Defaults to None.
            """
            super().__init__(parent=parent)
            self.setupUi(self)

            # 设置调整主题颜色按钮
            self.themeButton.setIcon(FIF.CONSTRACT)
            self.themeButton.setToolTip("Change Theme")
            self.themeButton.clicked.connect(lambda: toggleTheme(True))

            # 设置跳转GitHub按钮
            self.GitHubButton.setIcon(FIF.GITHUB)
            self.GitHubButton.setToolTip("GitHub")
            self.GitHubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(GITHUB)))

            # 引入QWebEngineView控件，配合ECharts，用于显示图表
            """ 
            TODO: 此处只给出了一个示例，且数据是静态的，
            需要写JS或用其他接口方法把本地数据读入HTML进行渲染，
            且后续要仿照该示例添加其他图表
            """
            self.HTML_CURRENT_DIR = "health_tracker/health_app_pyqt/resource/html"
            last_week_data = user.activity_data.get_last_week_daily_total()

            # Calories
            self.caloriesHtmlFileName = "calories-daily-area-stack-gradient.html"
            self.caloriesHtmlFileHandler = HTMLFileHandler(f"{self.HTML_CURRENT_DIR}/{self.caloriesHtmlFileName}")

            calories_data = last_week_data["active_energy_burned"]
            calories_run_data_str = f"    data: [{','.join([str(int(i*0.02)) for i in calories_data])}],"
            calories_walk_data_str = f"    data: [{','.join([str(int(i*0.90)) for i in calories_data])}],"
            calories_bike_data_str = f"    data: [{','.join([str(int(i*0.01)) for i in calories_data])}],"
            calories_floor_data_str = f"    data: [{','.join([str(int(i*0.05)) for i in calories_data])}],"
            calories_other_data_str = f"    data: [{','.join([str(int(i*0.02)) for i in calories_data])}],"

            self.caloriesHtmlFileHandler.modify_line(108, calories_run_data_str)
            self.caloriesHtmlFileHandler.modify_line(135, calories_walk_data_str)
            self.caloriesHtmlFileHandler.modify_line(162, calories_bike_data_str)
            self.caloriesHtmlFileHandler.modify_line(189, calories_floor_data_str)
            self.caloriesHtmlFileHandler.modify_line(220, calories_other_data_str)

            self.webview = QWebEngineView()
            self.webview.load(self.renderLocalHtmlURL(self.caloriesHtmlFileName))
            self.verticalLayout_1_1.addWidget(self.webview)

            # Floor
            self.floorHtmlFileName = "floor-bar-stack-borderRadius.html"
            self.floorHtmlFileHandler = HTMLFileHandler(f"{self.HTML_CURRENT_DIR}/{self.floorHtmlFileName}")

            floor_data = last_week_data["flights_climbed"]
            # 将floor_data的每一个元素转换成int，然后再拼接成如下形式：    data: [120, 200, 150, 80, 70, 110, 130],
            floor_data_str = f"    data: [{','.join([str(int(i)) for i in floor_data])}],"
            self.floorHtmlFileHandler.modify_line(45, floor_data_str)

            self.webview = QWebEngineView()
            self.webview.load(self.renderLocalHtmlURL(self.floorHtmlFileName))
            self.verticalLayout_2_1.addWidget(self.webview)

            # Distance
            self.distanceHtmlFileName = "distance-daily-area-stack-gradient.html"
            self.distanceHtmlFileHandler = HTMLFileHandler(f"{self.HTML_CURRENT_DIR}/{self.distanceHtmlFileName}")

            distance_data = last_week_data["distance"]
            distance_run_data_str = f"    data: [{','.join([str(i*0.15) for i in distance_data])}],"
            distance_walk_data_str = f"    data: [{','.join([str(i*0.60) for i in distance_data])}],"
            distance_floor_data_str = f"    data: [{','.join([str(i*0.12) for i in distance_data])}],"
            distance_other_data_str = f"    data: [{','.join([str(i*0.13) for i in distance_data])}],"

            self.distanceHtmlFileHandler.modify_line(108, distance_run_data_str)
            self.distanceHtmlFileHandler.modify_line(135, distance_walk_data_str)
            self.distanceHtmlFileHandler.modify_line(162, distance_floor_data_str)
            self.distanceHtmlFileHandler.modify_line(193, distance_other_data_str)

            self.webview = QWebEngineView()
            self.webview.load(self.renderLocalHtmlURL(self.distanceHtmlFileName))
            self.verticalLayout_3_1.addWidget(self.webview)

            # Steps
            self.stepHtmlFileName = "step-bar-stack-borderRadius.html"
            self.stepHtmlFileHandler = HTMLFileHandler(f"{self.HTML_CURRENT_DIR}/{self.stepHtmlFileName}")

            step_data = last_week_data["steps"]
            step_data_str = f"    data: [{','.join([str(int(i)) for i in step_data])}],"
            self.stepHtmlFileHandler.modify_line(45, step_data_str)

            self.webview = QWebEngineView()
            self.webview.load(self.renderLocalHtmlURL(self.stepHtmlFileName))
            self.verticalLayout_4_1.addWidget(self.webview)

            # 累计和日均label
            self.accumulated_data = user.activity_data.get_last_week_total()

            self.caloriesAccumulatedLabel.setText(f"{self.accumulated_data['active_energy_burned']:.2f} kcal")
            self.caloriesDailyLabel.setText(f"{self.accumulated_data['active_energy_burned']/7:.2f} kcal")

            self.floorAccumulatedLabel.setText(f"{self.accumulated_data['flights_climbed']:.2f} meters")
            self.floorDailyLabel.setText(f"{self.accumulated_data['flights_climbed']/7:.2f} meters")

            self.distanceAccumulatedLabel.setText(f"{self.accumulated_data['distance']:.2f} meters")
            self.distanceDailyLabel.setText(f"{self.accumulated_data['distance']/7:.2f} meters")

            self.stepsAccumulatedLabel.setText(f"{self.accumulated_data['steps']:.2f} steps")
            self.stepsDailyLabel.setText(f"{self.accumulated_data['steps']/7:.2f} steps")

            # 添加菜单，用于切换图表
            self.pivot.addItem(
                routeKey="calories",
                text="Calories",
                onClick=lambda: self.stackedWidget.setCurrentWidget(self.caloriesPage),
            )

            self.pivot.addItem(
                routeKey="floor",
                text="Floor",
                onClick=lambda: self.stackedWidget.setCurrentWidget(self.floorPage),
            )

            self.pivot.addItem(
                routeKey="distance",
                text="Distance",
                onClick=lambda: self.stackedWidget.setCurrentWidget(self.distancePage),
            )

            self.pivot.addItem(
                routeKey="steps",
                text="Steps",
                onClick=lambda: self.stackedWidget.setCurrentWidget(self.stepPage),
            )

    # 用于加载本地HTML文件路径
    def renderLocalHtmlURL(self, HTML_file_name: str):
        file_path = os.path.abspath(os.path.join(CURRENT_DIR, 'resource', 'html', HTML_file_name))
        return QUrl.fromLocalFile(file_path)
        



        