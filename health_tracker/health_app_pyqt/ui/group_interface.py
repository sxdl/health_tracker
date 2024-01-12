import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget, QAction, QListWidgetItem, QPushButton

from qfluentwidgets import FluentIcon as FIF, RoundMenu, toggleTheme, MessageBoxBase, SubtitleLabel, LineEdit, BodyLabel, TextEdit, FlyoutView, PushButton, Flyout
from .group_interface_ui import Ui_GroupInterface

from ..config import *
from ...tracker import User


class AnnouncementMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel('Edit announcement', self)

        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.announEdit = TextEdit(self)
        self.announEdit.setText(self.parent().announcementLabel.text())
        self.announEdit.setPlaceholderText("")
        self.announEdit.setProperty("transparent", True)
        self.announEdit.setObjectName("nameEdit")
        self.viewLayout.addWidget(self.announEdit)
        
        # change the text of button
        self.yesButton.setText('Save')
        self.cancelButton.setText('Cancel')

        self.widget.setMinimumWidth(350)

        # when save button is clicked
        self.yesButton.clicked.connect(self.on_save)

    def on_save(self):
        """
        save button click event
        """
        self.parent().announcementLabel.setText(self.announEdit.toPlainText())

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
        self.parent().listWidget.addItem(QListWidgetItem("👥" + self.groupNameEdit.text()))
        self.parent().listWidget.setCurrentRow(-1)
        self.parent().stackedWidget.setCurrentIndex(0)

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

        self.groupThemeButton.setIcon(FIF.CONSTRACT)
        self.groupThemeButton.setToolTip("Change Theme")
        self.groupThemeButton.clicked.connect(lambda: toggleTheme(True))

        self.GitHubButton.setIcon(FIF.GITHUB)
        self.GitHubButton.setToolTip("GitHub")
        self.GitHubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(GITHUB)))

        self.createButton.setIcon(FIF.ADD_TO)
        self.createButton.setToolTip("Create Group")
        self.createButton.clicked.connect(self.on_turn_to_create)
        
        groups = [
            "👥 Group 1",
            "👥 Group 2",
            "👥 Group 3",
            "👥 Group 4"
        ]
        for group in groups:
            item = QListWidgetItem(group)
            self.listWidget.addItem(item)
        
        self.listWidget.currentItemChanged.connect(self.on_current_item_changed)
        self.listWidget.setCurrentRow(-1)
        self.stackedWidget.setCurrentIndex(0)

        self.announEditButton.setIcon(FIF.EDIT)
        self.announEditButton.setToolTip("Edit Annnouncement")
        self.announEditButton.clicked.connect(self.on_announ_edit)

        self.qrcodeButton.setIcon(FIF.QRCODE)
        self.qrcodeButton.setToolTip("Show QRCode")
        self.qrcodeButton.clicked.connect(self.showQRCodeFlyout)

        self.createGroupButton.clicked.connect(self.on_create_group)
        self.joinByCodeButton.clicked.connect(self.on_join_by_code)


    def showQRCodeFlyout(self):
        view = FlyoutView(
            title='杰洛·齐贝林',
            content="触网而起的网球会落到哪一侧，谁也无法知晓。\n如果那种时刻到来，我希望「女神」是存在的。\n这样的话，不管网球落到哪一边，我都会坦然接受的吧。",
            image='health_tracker/health_app_pyqt/resource/images/icon\icon.png',
            isClosable=True
            # image='resource/yiku.gif',
        )

        # add button to view
        button = PushButton('Action')
        button.setFixedWidth(120)
        view.addWidget(button, align=Qt.AlignRight)

        # adjust layout (optional)
        view.widgetLayout.insertSpacing(1, 5)
        view.widgetLayout.addSpacing(5)

        # show view
        w = Flyout.make(view, self.qrcodeButton, self)
        view.closed.connect(w.close)

    def on_current_item_changed(self, current):
        index = self.listWidget.row(current) + 1
        self.stackedWidget.setCurrentIndex(index)

    def on_turn_to_create(self):
        """ create group """
        self.listWidget.setCurrentRow(-1)
        self.stackedWidget.setCurrentIndex(0)

    def on_announ_edit(self):
        """ edit announcement """
        self.messageBox = AnnouncementMessageBox(self)
        self.messageBox.exec_()

    def on_create_group(self):
        """ create group """
        self.messageBox = CreateGroupMessageBox(self)
        self.messageBox.exec_()

    def on_join_by_code(self):
        """ join group by code """
        self.messageBox = JoinByCodeMessageBox(self)
        self.messageBox.exec_()