import tkinter as tk
from tkinter import ttk
from ..tracker import User
from abc import ABC, abstractmethod

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
        ttk.Button(root, text="查看详细数据", command=self.open_detail_data_page).grid(row=0, column=1, pady=10,
                                                                                       padx=10, sticky="w")
        ttk.Button(root, text="查看详细数据", command=self.open_detail_data_page).grid(row=1, column=1, pady=10,
                                                                                       padx=10, sticky="w")
        ttk.Button(root, text="查看详细数据", command=self.open_detail_data_page).grid(row=2, column=1, pady=10,
                                                                                       padx=10, sticky="w")
        ttk.Button(root, text="查看详细数据", command=self.open_detail_data_page).grid(row=3, column=1, pady=10,
                                                                                       padx=10, sticky="w")

    def open_detail_data_page(self):
        # 跳转到详细数据页面
        detail_data_window = tk.Toplevel(self.root)
        detail_data_page = DetailDataPage(detail_data_window)


class DetailDataPage:
    def __init__(self, root):
        # TODO: 显示日周月年的详细数据，生成图表
        self.root = root
        self.root.title("详细数据页面")

        # 创建标签显示详细数据
        ttk.Label(root, text="日期: 2023-01-01").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        ttk.Label(root, text="步数: 10000").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        ttk.Label(root, text="距离: 5 km").grid(row=2, column=0, pady=10, padx=10, sticky="w")
        ttk.Label(root, text="爬楼: 10 层").grid(row=3, column=0, pady=10, padx=10, sticky="w")
        ttk.Label(root, text="活动热量: 200 kcal").grid(row=4, column=0, pady=10, padx=10, sticky="w")

        # 创建返回按钮
        back_button = ttk.Button(root, text="返回", command=self.close_detail_data_page)
        back_button.grid(row=5, column=0, pady=10, padx=10, sticky="w")

    def close_detail_data_page(self):
        # 关闭详细数据页面
        self.root.destroy()


class StepsDetailDataPage(DetailDataPage):
    # TODO: 显示步数的详细数据
    pass


class DistanceDetailDataPage(DetailDataPage):
    # TODO: 显示距离的详细数据
    pass


class FlightsClimbedDetailDataPage(DetailDataPage):
    # TODO: 显示爬楼的详细数据
    pass


class ActiveEnergyBurnedDetailDataPage(DetailDataPage):
    # TODO: 显示活动热量的详细数据
    pass


