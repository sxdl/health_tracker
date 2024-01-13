from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5.QtWidgets import QWidget, QAction, QLabel

from qfluentwidgets import FluentIcon as FIF, RoundMenu, toggleTheme, FlyoutView, PushButton, Flyout, TextEdit, MessageBoxBase, SubtitleLabel

from .group_page_ui import Ui_GroupPage
from ..config import *
from ...tracker import User
from ...tracker.group import Group


class GroupPage(QWidget, Ui_GroupPage):
    def __init__(self, group: Group, parent=None):
        """
        Initializes the GroupPage class.

        Args:
            group (Group): The group object.
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent=parent)
        self.setupUi(self)

        self.announEditButton_0.setIcon(FIF.EDIT)
        self.announEditButton_0.setToolTip("Edit Annnouncement")
        self.announEditButton_0.clicked.connect(self.on_announ_edit)

        self.qrcodeButton_0.setIcon(FIF.QRCODE)
        self.qrcodeButton_0.setToolTip("Show QRCode")
        self.qrcodeButton_0.clicked.connect(self.showQRCodeFlyout)

        self.group = group

    def showQRCodeFlyout(self):
        view = FlyoutView(
            title='杰洛·齐贝林',
            content="触网而起的网球会落到哪一侧，谁也无法知晓。\n如果那种时刻到来，我希望「女神」是存在的。\n这样的话，不管网球落到哪一边，我都会坦然接受的吧。",
            # image='health_tracker/health_app_pyqt/resource/images/icon\icon.png',
            image=self.group.save_qr_cord(),
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
        w = Flyout.make(view, self.qrcodeButton_0, self)
        view.closed.connect(w.close)

    def on_announ_edit(self):
        """ edit announcement """
        self.messageBox = AnnouncementMessageBox(self)
        self.messageBox.exec_()


class AnnouncementMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel('Edit announcement', self)

        # add widget to view layout
        self.viewLayout.addWidget(self.titleLabel)
        self.announEdit = TextEdit(self)
        self.announEdit.setText(self.parent().announcementLabel_0.text())
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
        self.parent().announcementLabel_0.setText(self.announEdit.toPlainText())