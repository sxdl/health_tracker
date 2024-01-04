"""用于编辑个人资料的窗口"""
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

__all__ = ["EditProfileWindow"]


class EditProfileWindow:
    def __init__(self, root, previous, user):
        self.user = user
        self.root = root
        self.previous = previous
        self.root.title("修改个人资料")

        self.gender, self.birth, self.height, self.weight = user.get_profile()
        self.GENDER = {"男": 0, "女": 1, "未知": 2}

        # 创建标签和输入框
        ttk.Label(root, text="性别:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.gender_combobox = ttk.Combobox(root, width=17, state="readonly")
        self.gender_combobox["values"] = ("男", "女", "未知")
        self.gender_combobox.current(self.GENDER[self.gender])
        self.gender_combobox.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        # 创建标签和日期选择器
        ttk.Label(root, text="出生日期:").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.current_date_label = ttk.Label(root, text=self.birth)
        self.current_date_label.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        self.select_date_button = ttk.Button(root, text="选择日期", command=self.select_date)
        self.select_date_button.grid(row=1, column=2, pady=10, padx=10, sticky="w")

        ttk.Label(root, text="身高:").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.height_entry = ttk.Entry(root)
        self.height_entry.insert(0, self.height)
        self.height_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")
        self.height_unit_label = ttk.Label(root, text="cm")
        self.height_unit_label.grid(row=2, column=2, pady=10, padx=10, sticky="w")

        ttk.Label(root, text="体重:").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.weight_entry = ttk.Entry(root)
        self.weight_entry.insert(0, self.weight)
        self.weight_entry.grid(row=3, column=1, pady=10, padx=10, sticky="w")
        self.weight_unit_label = ttk.Label(root, text="kg")
        self.weight_unit_label.grid(row=3, column=2, pady=10, padx=10, sticky="w")

        # 创建保存按钮
        save_button = ttk.Button(root, text="保存", command=self.save_profile)
        save_button.grid(row=4, column=1, pady=10, padx=10, sticky="e")

    def refresh_date(self, cal, select_date):
        """刷新日期选择器中的日期"""
        self.current_date_label["text"] = select_date
        # self.birth = select_date
        # 关闭窗口
        cal.destroy()

    def select_date(self):
        """在新窗口中显示日历，供用户选择日期"""
        # 创建新窗口
        select_date_window = tk.Toplevel(self.root)
        select_date_window.title("选择出生日期")

        # 创建日历
        calendar = Calendar(select_date_window, selectmode="day", date_pattern="y-mm-dd", year=2003, month=1, day=1)
        calendar.pack(pady=20, padx=20)

        # 创建确认按钮
        confirm_button = ttk.Button(select_date_window, text="确认", command=lambda: self.refresh_date(select_date_window, calendar.get_date()))
        confirm_button.pack(pady=20, padx=20)

    def save_profile(self):
        # 保存用户输入的个人资料
        self.gender = self.gender_combobox.get()
        self.birth = self.current_date_label["text"]
        self.birth = None
        self.height = self.height_entry.get()
        self.weight = self.weight_entry.get()

        # TODO: 这里可以添加将修改后的资料保存到文件或数据库的功能
        # self.user.profile.save_data()
        self.user.profile.update_data_by_field("gender", self.gender)
        self.user.profile.update_data_by_field("height", self.height)
        self.user.profile.update_data_by_field("weight", self.weight)

        # 关闭窗口
        self.root.destroy()
        self.previous.refresh_profile()


# def run_edit_profile_window():
#     profile_window = tk.Toplevel()
#     user_profile = {"gender": "男", "birthdate": "1990-01-01", "height": "170", "weight": "65"}
#     edit_profile = EditProfileWindow(profile_window, user_profile)

