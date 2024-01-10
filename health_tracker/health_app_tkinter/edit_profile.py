"""用于编辑个人资料的窗口"""
import tkinter as tk
from tkinter import ttk

__all__ = ["EditProfileWindow"]


class EditProfileWindow:
    def __init__(self, root, previous, user):
        self.user = user
        self.root = root
        self.previous = previous
        self.root.title("修改个人资料")

        self.nickname, self.gender, self.birth, self.height, self.weight = ("默认昵称",) + user.get_profile()
        self.GENDER = {"男": 0, "女": 1, "未知": 2}

        # 创建标签和输入框
        ttk.Label(root, text="昵称:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.nickname_entry = ttk.Entry(root)
        self.nickname_entry.insert(0, "请输入昵称")
        self.nickname_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        ttk.Label(root, text="性别:").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.gender_combobox = ttk.Combobox(root, width=17, state="readonly")
        self.gender_combobox["values"] = ("男", "女", "未知")
        self.gender_combobox.current(self.GENDER[self.gender])
        self.gender_combobox.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        # 创建标签和日期选择器
        ttk.Label(root, text="出生日期:").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.current_date_label = ttk.Label(root, text=self.birth)
        self.current_date_label.grid(row=2, column=1, pady=10, padx=10, sticky="w")
        self.select_date_button = ttk.Button(root, text="选择日期", command=self.select_date)
        self.select_date_button.grid(row=2, column=2, pady=10, padx=10, sticky="w")

        ttk.Label(root, text="身高:").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.height_entry = ttk.Entry(root)
        self.height_entry.insert(0, self.height)
        self.height_entry.grid(row=3, column=1, pady=10, padx=10, sticky="w")
        self.height_unit_label = ttk.Label(root, text="cm")
        self.height_unit_label.grid(row=3, column=2, pady=10, padx=10, sticky="w")

        ttk.Label(root, text="体重:").grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.weight_entry = ttk.Entry(root)
        self.weight_entry.insert(0, self.weight)
        self.weight_entry.grid(row=4, column=1, pady=10, padx=10, sticky="w")
        self.weight_unit_label = ttk.Label(root, text="kg")
        self.weight_unit_label.grid(row=4, column=2, pady=10, padx=10, sticky="w")

        # 创建保存按钮
        save_button = ttk.Button(root, text="保存", command=self.save_profile)
        save_button.grid(row=5, column=1, pady=10, padx=10, sticky="e")

    def select_date(self):
        """在新窗口中显示手动选择日期的界面"""
        # 创建新窗口
        select_date_window = tk.Toplevel(self.root)
        select_date_window.title("选择出生日期")

        # 创建标签和输入框，手动输入年、月、日
        ttk.Label(select_date_window, text="年:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        year_spinbox = ttk.Spinbox(select_date_window, from_=1900, to=2100)
        year_spinbox.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        ttk.Label(select_date_window, text="月:").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        month_spinbox = ttk.Spinbox(select_date_window, from_=1, to=12)
        month_spinbox.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        ttk.Label(select_date_window, text="日:").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        day_spinbox = ttk.Spinbox(select_date_window, from_=1, to=31)
        day_spinbox.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        # 创建确认按钮
        confirm_button = ttk.Button(select_date_window, text="确认", command=lambda: self.refresh_date_manual(select_date_window, year_spinbox.get(), month_spinbox.get(), day_spinbox.get()))
        confirm_button.grid(row=3, column=1, pady=20, padx=20, sticky="w")

    def refresh_date_manual(self, cal, year, month, day):
        """刷新手动选择日期的界面"""
        selected_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        self.current_date_label["text"] = selected_date
        cal.destroy()

    def save_profile(self):
        # 保存用户输入的个人资料
        self.gender = self.gender_combobox.get()
        self.birth = self.current_date_label["text"]
        self.height = self.height_entry.get()
        self.weight = self.weight_entry.get()

        # TODO: 可以添加将修改后的资料保存到文件或数据库的功能
        # 更新用户资料
        self.user.profile.update_data_by_field("gender", self.gender)
        self.user.profile.update_data_by_field("birth", self.birth)  # 修改这行
        self.user.profile.update_data_by_field("height", self.height)
        self.user.profile.update_data_by_field("weight", self.weight)


        # 关闭窗口
        self.root.destroy()
        self.previous.refresh_profile()



# def run_edit_profile_window():
#     profile_window = tk.Toplevel()
#     user_profile = {"gender": "男", "birthdate": "1990-01-01", "height": "170", "weight": "65"}
#     edit_profile = EditProfileWindow(profile_window, user_profile)

