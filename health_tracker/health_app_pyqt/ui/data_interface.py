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
            # Calories
            # TODO: 添加“累计”和“日均”label
            self.webview = QWebEngineView()
            self.webview.load(self.renderLocalHtmlURL("calories-daily-area-stack-gradient.html"))
            self.verticalLayout_1_1.addWidget(self.webview)

            # Floor
            # TODO: 爬楼数据应该要改成柱状图，展示每日的数据；添加“总高度”和“平均高度”label
            self.webview = QWebEngineView()
            self.webview.load(self.renderLocalHtmlURL("floor-bar-stack-borderRadius.html"))
            self.verticalLayout_2_1.addWidget(self.webview)

            # Distance
            # TODO: 添加“总距离”和“平均距离”label
            self.webview = QWebEngineView()
            self.webview.load(self.renderLocalHtmlURL("distance-daily-area-stack-gradient.html"))
            self.verticalLayout_3_1.addWidget(self.webview)

            # Steps
            # TODO: 步数数据应该要改成柱状图，展示每日的数据；添加“总步数”和“平均步数”label
            self.webview = QWebEngineView()
            self.webview.load(self.renderLocalHtmlURL("step-bar-stack-borderRadius.html"))
            self.verticalLayout_4_1.addWidget(self.webview)

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
        



        