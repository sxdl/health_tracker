"""展示个人资料界面"""
import tkinter as tk
from tkinter import ttk
from . edit_profile import EditProfileWindow
from ..tracker.user import User

__all__ = ["ShowProfileWindow"]


class ShowProfileWindow:
    def __init__(self, root, user: User):
        self.user = user
        self.root = root
        self.root.title("个人资料")

        # self.user_profile = user.profile.data
        self.user_profile = self.user.get_profile()

        # 创建标签显示个人资料
        self.gender_label = ttk.Label(root, text="性别: " + self.user_profile.gender)
        self.gender_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.birth_label = ttk.Label(root, text="出生日期: " + self.user_profile.birth)
        self.birth_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.height_label = ttk.Label(root, text="身高: " + self.user_profile.height)
        self.height_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.weight_label = ttk.Label(root, text="体重: " + self.user_profile.weight)
        self.weight_label.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        # ttk.Label(root, text="出生日期: " + self.user_profile.birth).grid(row=1, column=0, pady=10, padx=10, sticky="w")
        # ttk.Label(root, text="身高: " + self.user_profile.height).grid(row=2, column=0, pady=10, padx=10, sticky="w")
        # ttk.Label(root, text="体重: " + self.user_profile.weight).grid(row=3, column=0, pady=10, padx=10, sticky="w")

        # 创建修改按钮
        edit_button = ttk.Button(root, text="修改", command=self.open_edit_profile_window)
        edit_button.grid(row=4, column=0, pady=10, padx=10, sticky="w")

    def open_edit_profile_window(self):
        # 调用 EditProfileWindow 类显示编辑个人资料窗口
        edit_window = tk.Toplevel(self.root)
        edit_profile = EditProfileWindow(edit_window, self, self.user)
        self.root.wait_window(edit_window)

    def refresh_profile(self):
        """刷新个人资料"""
        print("刷新个人资料")
        self.user_profile = self.user.get_profile()
        # 更新标签
        self.gender_label.config(text="性别: " + self.user_profile.gender)
        self.birth_label.config(text="出生日期: " + self.user_profile.birth)
        self.height_label.config(text="身高: " + self.user_profile.height)
        self.weight_label.config(text="体重: " + self.user_profile.weight)


