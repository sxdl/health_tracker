import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl, QPoint
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget, QAction, QListWidgetItem, QPushButton, QHBoxLayout, QMessageBox

from qfluentwidgets import FluentIcon as FIF, RoundMenu, toggleTheme, MessageBoxBase, SubtitleLabel, LineEdit, InfoBarManager, InfoBar, InfoBarPosition
from .group_interface_ui import Ui_GroupInterface
from .group_page import GroupPage

from ..config import *
from ...tracker import User
from ...tracker.group import Group


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


class CreateGroupMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel('Create group', self)

        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.groupNameEdit = LineEdit(self)
        self.groupNameEdit.setText("")
        self.groupNameEdit.setFrame(True)
        self.groupNameEdit.setPlaceholderText("")
        self.groupNameEdit.setProperty("transparent", True)
        self.groupNameEdit.setObjectName("nameEdit")
        self.viewLayout.addWidget(self.groupNameEdit)
        
        # change the text of button
        self.yesButton.setText('Create')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        # when save button is clicked
        self.yesButton.clicked.connect(self.on_create)

    def on_create(self):
        """
        save button click event
        """
        self.parent().listWidget.addItem(QListWidgetItem("👥 " + self.groupNameEdit.text()))
        # 设置当前行为新建的群组
        self.parent().listWidget.setCurrentRow(self.parent().listWidget.count() - 1)


class JoinByCodeMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel('Join group by code', self)

        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.groupCodeEdit = LineEdit(self)
        self.groupCodeEdit.setText("")
        self.groupCodeEdit.setFrame(True)
        self.groupCodeEdit.setPlaceholderText("")
        self.groupCodeEdit.setProperty("transparent", True)
        self.groupCodeEdit.setObjectName("nameEdit")
        self.viewLayout.addWidget(self.groupCodeEdit)
        
        # change the text of button
        self.yesButton.setText('Join')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        # when save button is clicked
        self.yesButton.clicked.connect(self.on_join)

    def on_join(self):
        """
        save button click event
        """
        pass


class GroupInterface(QWidget, Ui_GroupInterface):
    def __init__(self, user: User, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.user = user

        self.groupThemeButton.setIcon(FIF.CONSTRACT)
        self.groupThemeButton.setToolTip("Change Theme")
        self.groupThemeButton.clicked.connect(lambda: toggleTheme(True))

        self.GitHubButton.setIcon(FIF.GITHUB)
        self.GitHubButton.setToolTip("GitHub")
        self.GitHubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(GITHUB)))

        self.createButton.setIcon(FIF.ADD_TO)
        self.createButton.setToolTip("Create Group")
        self.createButton.clicked.connect(self.on_turn_to_create)
        
        groups_id = Group.load_existing_groups()
        for group_id in groups_id:
            # item = QListWidgetItem(group)
            group = Group(group_id)
            item = QListWidgetItem("👥 " + group.name)
            self.listWidget.addItem(item)

            group_page = GroupPage(group, self)  # 创建一个新的 GroupPage 实例
            group_page.nameLabel_0.setText(group.name)
            group_page.announcementLabel_0.setText(group.announcement)
            group_page.groupIDLabel_1.setText(group.group_id)
            self.stackedWidget.addWidget(group_page)  # 将 GroupPage 实例添加到 stackedWidget 中

        self.listWidget.currentItemChanged.connect(self.on_current_item_changed)
        self.listWidget.setCurrentRow(-1)
        self.stackedWidget.setCurrentIndex(0)

        self.createGroupButton.clicked.connect(self.on_create_group)
        self.joinByCodeButton.clicked.connect(self.on_join_by_code)

    def on_current_item_changed(self, current):
        index = self.listWidget.row(current) + 1
        self.stackedWidget.setCurrentIndex(index)

    def on_turn_to_create(self):
        """ create group """
        self.listWidget.setCurrentRow(-1)
        self.stackedWidget.setCurrentIndex(0)

    def on_create_group(self):
        """ create group """
        self.messageBox = CreateGroupMessageBox(self)
        if self.messageBox.exec_() == QMessageBox.Accepted:
            group = Group.create_group(self.user.user_id, self.messageBox.groupNameEdit.text())  # 创建Group对象
            group_page = GroupPage(group, self)  # 创建一个新的 GroupPage 实例
            group_page.nameLabel_0.setText(self.messageBox.groupNameEdit.text())
            group_page.groupIDLabel_1.setText(group.group_id)
            self.stackedWidget.addWidget(group_page)  # 将 GroupPage 实例添加到 stackedWidget 中
            self.stackedWidget.setCurrentIndex(self.listWidget.count()) 
            self.createSuccessInfoBar()

    def on_join_by_code(self):
        """ join group by code """
        self.messageBox = JoinByCodeMessageBox(self)
        self.messageBox.exec_()

    def createSuccessInfoBar(self):
        # convenient class mothod
        InfoBar.success(
            title='Creation Successful',
            content=f"The group {self.messageBox.groupNameEdit.text()} has been created successfully.",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )
