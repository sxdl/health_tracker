import tkinter as tk
from tkinter import ttk
from ..tracker import User
from abc import ABC, abstractmethod
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.font_manager import FontProperties





__all__ = ["MyStatisticsWindow"]


class MyStatisticsWindow:
    def __init__(self, root, user: User):
        self.user = user
        self.root = root
        self.root.title("我的数据")

        self.latest_data = self.user.activity_data.get_latest_daily_total()
        self.steps = self.latest_data["steps"]
        self.distance = self.latest_data["distance"]
        self.flights_climbed = self.latest_data["flights_climbed"]
        self.active_energy_burned = self.latest_data["active_energy_burned"]

        # 创建标签显示我的数据概览
        ttk.Label(root, text=f"步数: {self.steps} 步").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        ttk.Label(root, text=f"距离: {self.distance:.2f} 公里").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        ttk.Label(root, text=f"爬楼: {self.flights_climbed} 米").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        ttk.Label(root, text=f"活动热量: {self.active_energy_burned} 千卡").grid(row=3, column=0, pady=10, padx=10,
                                                                             sticky="w")

        # 创建查看详细数据按钮
        ttk.Button(root, text="查看详细数据", command=lambda: self.open_detail_data_page("steps")).grid(row=0, column=1, pady=10,
                                                                                           padx=10, sticky="w")
        ttk.Button(root, text="查看详细数据", command=lambda: self.open_detail_data_page("distance")).grid(row=1, column=1, pady=10,
                                                                                              padx=10, sticky="w")
        ttk.Button(root, text="查看详细数据", command=lambda: self.open_detail_data_page("flights_climbed")).grid(row=2, column=1,
                                                                                                       pady=10, padx=10,
                                                                                                       sticky="w")
        ttk.Button(root, text="查看详细数据", command=lambda: self.open_detail_data_page("active_energy_burned")).grid(row=3,
                                                                                                              column=1, pady=10,
                                                                                                              padx=10,
                                                                                                              sticky="w")

    def open_detail_data_page(self, data_type):
        # 跳转到详细数据页面
        detail_data_window = tk.Toplevel(self.root)

        if data_type == "steps":
            detail_data_page = StepsDetailDataPage(detail_data_window, self.user)
        elif data_type == "distance":
            detail_data_page = DistanceDetailDataPage(detail_data_window, self.user)
        elif data_type == "flights_climbed":
            detail_data_page = FlightsClimbedDetailDataPage(detail_data_window, self.user)
        elif data_type == "active_energy_burned":
            detail_data_page = ActiveEnergyBurnedDetailDataPage(detail_data_window, self.user)
        else:
            detail_data_page = DetailDataPage(detail_data_window, self.user)


class DetailDataPage(ABC):
    def __init__(self, root, user=None):
        self.root = root
        self.user = user
        self.root.title("详细数据页面")
        self.latest_data = self.user.activity_data.get_latest_daily_total() if self.user else None

        # 创建标签显示详细数据
        ttk.Label(root, text=self.get_detail_label_text()).grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # 创建返回按钮
        back_button = ttk.Button(root, text="返回", command=self.close_detail_data_page)
        back_button.grid(row=5, column=0, pady=10, padx=10, sticky="w")

    @abstractmethod
    def get_detail_label_text(self):
        pass

    @abstractmethod
    def close_detail_data_page(self):
        pass

# class DetailDataPage:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("详细数据页面")
#         self.latest_data = self.user.activity_data.get_latest_daily_total()
#         self.steps = self.latest_data["steps"]
#         self.distance = self.latest_data["distance"]
#         self.flights_climbed = self.latest_data["flights_climbed"]
#         self.active_energy_burned = self.latest_data["active_energy_burned"]
#
#         # 创建标签显示详细数据
#         ttk.Label(root, text=f"步数: {self.steps} 步").grid(row=0, column=0, pady=10, padx=10, sticky="w")
#         ttk.Label(root, text=f"距离: {self.distance:.2f} 公里").grid(row=1, column=0, pady=10, padx=10, sticky="w")
#         ttk.Label(root, text=f"爬楼: {self.flights_climbed} 米").grid(row=2, column=0, pady=10, padx=10, sticky="w")
#         ttk.Label(root, text=f"活动热量: {self.active_energy_burned} 千卡").grid(row=3, column=0, pady=10, padx=10,
#                                                                                  sticky="w")
#
#         # 创建返回按钮
#         back_button = ttk.Button(root, text="返回", command=self.close_detail_data_page)
#         back_button.grid(row=5, column=0, pady=10, padx=10, sticky="w")
#
#     def close_detail_data_page(self):
#         # 关闭详细数据页面
#         self.root.destroy()


class StepsDetailDataPage(DetailDataPage):
    def __init__(self, root, user):
        super().__init__(root, user)

        # 添加一个画布用于显示图表
        self.canvas = FigureCanvasTkAgg(self.plot_steps_over_time(), master=root)
        self.canvas.get_tk_widget().grid(row=1, column=0, pady=10, padx=10, sticky="w")

    def get_detail_label_text(self):
        return f"步数: {self.latest_data['steps']} 步"

    def close_detail_data_page(self):
        self.root.destroy()

    def plot_steps_over_time(self):
        # 获取一周内的步数数据
        start_date = datetime.now() - timedelta(days=6)
        dates = [start_date + timedelta(days=i) for i in range(7)]
        steps_data = [self.user.activity_data.get_daily_total("steps", date) for date in dates]

        # 设置字体为支持多语言字符的字体（比如Arial Unicode MS）
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

        # 绘制折线图
        fig, ax = plt.subplots()
        ax.plot(dates, steps_data, marker='o', linestyle='-')

        # 重新设置字体为黑体（SimHei）
        plt.rcParams['font.sans-serif'] = ['SimHei']

        ax.set(xlabel='日期', ylabel='步数', title='步数随时间变化')
        ax.grid()

        return fig


class DistanceDetailDataPage(DetailDataPage):
    def __init__(self, root, user):
        super().__init__(root, user)

        # 添加一个画布用于显示图表
        self.canvas = FigureCanvasTkAgg(self.plot_distance_over_time(), master=root)
        self.canvas.get_tk_widget().grid(row=1, column=0, pady=10, padx=10, sticky="w")

    def get_detail_label_text(self):
        return f"距离: {self.latest_data['distance']:.2f} 公里"

    def close_detail_data_page(self):
        self.root.destroy()

    def plot_distance_over_time(self):
        # 获取一周内的距离数据
        start_date = datetime.now() - timedelta(days=6)
        dates = [start_date + timedelta(days=i) for i in range(7)]
        distance_data = [self.user.activity_data.get_daily_total("distance", date) for date in dates]
        # 绘制折线图
        fig, ax = plt.subplots()

        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 使用支持多语言字符的字体
        ax.plot(dates, distance_data, marker='o', linestyle='-')

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
        ax.set(xlabel='日期', ylabel='距离 (公里)', title='距离随时间变化')
        ax.grid()

        return fig



class FlightsClimbedDetailDataPage(DetailDataPage):
    def __init__(self, root, user):
        super().__init__(root, user)

        # 添加一个画布用于显示图表
        self.canvas = FigureCanvasTkAgg(self.plot_flights_climbed_over_time(), master=root)
        self.canvas.get_tk_widget().grid(row=1, column=0, pady=10, padx=10, sticky="w")

    def get_detail_label_text(self):
        return f"爬楼: {self.latest_data['flights_climbed']} 米"

    def close_detail_data_page(self):
        self.root.destroy()

    def plot_flights_climbed_over_time(self):
        # 获取一周内的爬楼数据
        start_date = datetime.now() - timedelta(days=6)
        dates = [start_date + timedelta(days=i) for i in range(7)]
        flights_climbed_data = [self.user.activity_data.get_daily_total("flights_climbed", date) for date in dates]

        # 绘制折线图
        fig, ax = plt.subplots()
        ax.plot(dates, flights_climbed_data, marker='o', linestyle='-')
        ax.set(xlabel='日期', ylabel='爬楼高度 (米)', title='爬楼高度随时间变化')
        ax.grid()

        return fig



class ActiveEnergyBurnedDetailDataPage(DetailDataPage):
    def __init__(self, root, user):
        super().__init__(root, user)

        # 添加一个画布用于显示图表
        self.canvas = FigureCanvasTkAgg(self.plot_active_energy_burned_over_time(), master=root)
        self.canvas.get_tk_widget().grid(row=1, column=0, pady=10, padx=10, sticky="w")

    def get_detail_label_text(self):
        return f"活动热量: {self.latest_data['active_energy_burned']} 千卡"

    def close_detail_data_page(self):
        self.root.destroy()

    def plot_active_energy_burned_over_time(self):
        # 获取一周内的活动热量数据
        start_date = datetime.now() - timedelta(days=6)
        dates = [start_date + timedelta(days=i) for i in range(7)]
        active_energy_burned_data = [self.user.activity_data.get_daily_total("active_energy_burned", date) for date in dates]
        # 绘制折线图
        fig, ax = plt.subplots()
        ax.plot(dates, active_energy_burned_data, marker='o', linestyle='-')
        ax.set(xlabel='日期', ylabel='活动热量 (千卡)', title='活动热量随时间变化')
        ax.grid()

        return fig



