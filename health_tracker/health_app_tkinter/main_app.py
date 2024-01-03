import tkinter as tk
from tkinter import ttk
from . show_profile import ShowProfileWindow
from .my_statistics import MyStatisticsWindow
from ..tracker.user import User
from health_tracker.tracker import util

from ttkbootstrap import Style

__all__ = ["run_app"]


class HealthTrackingApp:
    def __init__(self, root, user=None):
        self.root = root
        # self.root.overrideredirect(True)  # 设置窗口为无边框
        self.root.geometry('800x450')  # 设置窗口大小为800x450
        self.center_window(self.root)
        self.root.title("健康追踪应用")

        self.user = user if user else User("0", "游客")
        self.today_data = self.user.activity_data.get_latest_daily_total()

        # 创建导航栏
        self.nav_bar = ttk.Notebook(root)

        # “健康”页面
        self.health_frame = ttk.Frame(self.nav_bar)
        self.create_health_page()

        # “设备”页面
        self.device_frame = ttk.Frame(self.nav_bar)
        self.create_device_page()
        self.device_list = []  # 创建一个空的设备列表
        self.device_label = None  # 初始化设备标签

        # “我的”页面
        self.my_frame = ttk.Frame(self.nav_bar)
        self.create_my_page()

        # 将页面添加到导航栏
        self.nav_bar.add(self.health_frame, text="健康")
        self.nav_bar.add(self.device_frame, text="设备")
        self.nav_bar.add(self.my_frame, text="我的")

        # 显示导航栏
        self.nav_bar.pack(expand=1, fill="both")
    def create_device_page(self):
        # 在“设备”页面显示已绑定设备
        # TODO: 实现显示已绑定设备的功能
        self.device_label = ttk.Label(self.device_frame, text="已绑定设备列表: ")
        self.device_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        print(f"After create_device_page: {self.device_label}")  # 打印self.device_label的值

        # 创建“添加设备”按钮
        add_device_button = ttk.Button(self.device_frame, text="添加设备", command=self.add_device)
        add_device_button.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        # 创建设备使用时间按钮并设置为不可见
        self.device_buttons = {
            "手机": ttk.Button(self.device_frame, text="手机日使用时间", command=self.record_phone_usage),
            "无线耳机": ttk.Button(self.device_frame, text="无线耳机日使用时间", command=self.record_earphone_usage),
            "电脑": ttk.Button(self.device_frame, text="电脑日使用时间", command=self.record_computer_usage),
            "Pad": ttk.Button(self.device_frame, text="Pad日使用时间", command=self.record_pad_usage),
        }
        for i, button in enumerate(self.device_buttons.values()):
            button.grid(row=i + 1, column=2, pady=10, padx=10, sticky="w")
            button.grid_remove()  # 设置按钮为不可见


    def add_device(self):
        # TODO: 显示已有设备列表
        # TODO: 实现添加新设备的功能
        self.new_window = tk.Toplevel(self.root)
        for device in self.device_buttons.keys():
            button = ttk.Button(self.new_window, text=device, command=lambda d=device: self.add_device_type(d))
            button.pack()

    def add_device_type(self, device):
        self.device_buttons[device].grid()  # 设置按钮为可见
        self.device_list.append(device)  # 将设备添加到设备列表中
        self.device_label.config(text=f"已绑定设备列表: {', '.join(self.device_list)}")  # 更新设备列表的显示
        self.new_window.destroy()
        print(f"After add_device_type: {self.device_label}")  # 打印self.device_label的值

    def record_phone_usage(self):
        phone_usage_window = tk.Toplevel(self.root)
        phone_usage_page = util.PhoneUsageWindow(phone_usage_window, self.user.user_id, "earphone_usage.txt")
    def record_earphone_usage(self):
        earphone_usage_window = tk.Toplevel(self.root)
        earphone_usage_page = util.EarphoneUsageWindow(earphone_usage_window, self.user.user_id, "earphone_usage.txt")
    def record_computer_usage(self):
        computer_usage_window = tk.Toplevel(self.root)
        computer_usage_page = util.ComputerUsageWindow(computer_usage_window, self.user.user_id, "earphone_usage.txt")
    def record_pad_usage(self):
        pad_usage_window = tk.Toplevel(self.root)
        pad_usage_page = util.PadUsageWindow(pad_usage_window, self.user.user_id, "earphone_usage.txt")

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def create_my_page(self):
        # 在“我的”页面创建姓名标签
        name_label = ttk.Label(self.my_frame, text=f"用户姓名: {self.user.name}")
        name_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # 创建“我的数据”按钮
        my_data_button = ttk.Button(self.my_frame, text="我的数据", command=self.show_my_data)
        my_data_button.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        # 创建“个人资料”按钮
        profile_button = ttk.Button(self.my_frame, text="个人资料", command=self.show_profile)
        profile_button.grid(row=2, column=0, pady=10, padx=10, sticky="w")


    def create_health_page(self):
        # 在“健康”页面显示活动记录
        active_energy_burned_label = ttk.Label(self.health_frame, text=f"活动热量: {self.today_data['active_energy_burned']} /270 千卡")
        active_energy_burned_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        exercise_time_label = ttk.Label(self.health_frame, text=f"锻炼时长: {self.today_data['exercise_minutes']} /25 分钟")
        exercise_time_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        active_hours_label = ttk.Label(self.health_frame, text=f"活动小时数: {self.today_data['active_hours']} /12 小时")
        active_hours_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        steps_label = ttk.Label(self.health_frame, text=f"今日步数: {self.today_data['steps']} /10000 步")
        steps_label.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        # 创建“查看活动记录”按钮
        view_activity_button = ttk.Button(self.health_frame, text="查看历史活动记录", command=self.show_activity_records)
        view_activity_button.grid(row=4, column=0, pady=10, padx=10, sticky="w")

    def show_my_data(self):
        # TODO: 实现进入详细的数据页面的功能
        print("进入我的数据页面")
        my_data_window = tk.Toplevel(self.root)
        self.center_window(my_data_window)
        my_data_page = MyStatisticsWindow(my_data_window, self.user)

    def show_profile(self):
        print("查看和修改个人资料")
        profile_window = tk.Toplevel(self.root)
        self.center_window(profile_window)
        edit_profile = ShowProfileWindow(profile_window, self.user)


    def show_activity_records(self):
        # TODO: 实现查看活动记录的功能
        print("查看活动记录")


def run_app(user_id="0", user_name="游客"):
    # 应用主题
    style = Style(theme="superhero")
    root = style.master

    # root = tk.Tk()
    app = HealthTrackingApp(root, user=User(user_id, user_name))
    root.mainloop()