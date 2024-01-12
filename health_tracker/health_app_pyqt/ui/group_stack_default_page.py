# page1_ui.py
from PyQt5.QtWidgets import QWidget
from . group_stack_default_page_ui import Ui_GroupStackDefaultPage


class GroupStackDefaultPage(QWidget, Ui_GroupStackDefaultPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 添加其他页面1的逻辑
