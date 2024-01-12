# page1_ui.py
from PyQt5.QtWidgets import QWidget
from . group_stack_group_list_page_ui import Ui_GroupStackGroupListPage


class GroupStackGroupListPage(QWidget, Ui_GroupStackGroupListPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 添加其他页面1的逻辑
