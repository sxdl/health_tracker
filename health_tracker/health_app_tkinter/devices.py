import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from abc import ABC, abstractmethod

from ..tracker.util import *


class AbstractInputWindow(ABC):
    def __init__(self, root, user_id: str, filename: str):
        self.root = root
        self.user_id = user_id
        self.filename = filename

        # 创建输入框
        self.entry = ttk.Entry(root)
        self.entry.grid(row=0, column=0, pady=10, padx=10)

        # 创建提交按钮
        submit_button = ttk.Button(root, text="提交", command=self.submit_data)
        submit_button.grid(row=1, column=0, pady=10, padx=10)

    @abstractmethod
    def submit_data(self):
        pass

class NutrientIntakeWindow(AbstractInputWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日摄入营养素")

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", "一日摄入营养素已记录。")

class CalorieIntakeOutputWindow(AbstractInputWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日卡路里摄入与消耗量")

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", "一日卡路里摄入与消耗量已记录。")

class DeviceUsageWindow(AbstractInputWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日电子设备使用时间")

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", "一日电子设备使用时间已记录。")


class DailyWaterIntakeWindow(NutrientIntakeWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日饮水量")

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", "一日饮水量已记录。")

class FiberIntakeWindow(NutrientIntakeWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日膳食纤维摄入量")

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", "一日膳食纤维摄入量已记录。")

class ProteinIntakeWindow(NutrientIntakeWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日蛋白质摄入量")

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", "一日蛋白质摄入量已记录。")

class FatIntakeWindow(NutrientIntakeWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日脂肪摄入量")

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", "一日脂肪摄入量已记录。")

class MealCalorieIntakeWindow(CalorieIntakeOutputWindow):
    def __init__(self, root, user_id: str, filename: str, meal_type: str):
        super().__init__(root, user_id, filename)
        self.root.title(f"{meal_type}的卡路里摄入量")
        self.meal_type = meal_type

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, f"{self.filename}_{self.meal_type}", data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", f"{self.meal_type}的卡路里摄入量已记录。")

    @classmethod
    def create_meal_windows(cls, root, user_id: str, filename: str):
        meal_types = ["早餐", "中餐", "晚餐"]
        return [cls(root, user_id, filename, meal_type) for meal_type in meal_types]

class FruitCalorieIntakeWindow(CalorieIntakeOutputWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日水果卡路里摄入量")

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", "一日水果卡路里摄入量已记录。")

class BeverageCalorieIntakeWindow(CalorieIntakeOutputWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日饮品卡路里摄入量")

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", "一日饮品卡路里摄入量已记录。")

class FitnessFoodCalorieIntakeWindow(CalorieIntakeOutputWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日健身食品卡路里摄入量")

    def submit_data(self):
        data = self.entry.get()
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        messagebox.showinfo("信息", "一日健身食品卡路里摄入量已记录。")

class ExerciseCalorieOutputWindow(CalorieIntakeOutputWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("一日体育活动卡路里消耗量")

        # 创建活动名称输入框
        self.activity_label = tk.Label(root, text="请输入体育活动名称：")
        self.activity_label.grid(row=1, column=0, pady=10, padx=10)
        self.activity_entry = ttk.Entry(root)
        self.activity_entry.grid(row=1, column=1, pady=10, padx=10)

        # 创建活动时长输入框
        self.duration_label = tk.Label(root, text="请输入活动时长（分钟）：")
        self.duration_label.grid(row=2, column=0, pady=10, padx=10)
        self.duration_entry = ttk.Entry(root)
        self.duration_entry.grid(row=2, column=1, pady=10, padx=10)

        # 卡路里消耗量字典
        self.calorie_dict = {
            "游泳": 175,
            "田径": 450,
            "篮球": 250,
            "自行车": 330,
            "慢跑": 300,
            "散步": 75
        }

        # 用户输入和运动类别的映射
        self.activity_mapping = {
            "游": "游泳",
            "快跑": "田径",
            "一千米":"田径",
            "走": "散步",
            "球": "篮球",
            "车": "自行车",
        }

    def submit_data(self):
        user_input = self.activity_entry.get()
        duration = float(self.duration_entry.get())
        # 根据用户输入获取运动类别
        activity = self.activity_mapping.get(user_input, "")
        # 根据运动类别获取每半小时消耗的卡路里
        calorie_per_half_hour = self.calorie_dict.get(activity, 0)
        # 计算消耗的卡路里
        calories = duration / 30 * calorie_per_half_hour
        data = {"activity": activity, "duration": duration, "calories": calories}
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        self.activity_entry.delete(0, 'end')
        self.duration_entry.delete(0, 'end')
        messagebox.showinfo("信息", f"一日体育活动卡路里消耗量已记录。消耗的卡路里为：{calories} 卡")

class PhoneUsageWindow(DeviceUsageWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("手机日使用时长")

        # 创建手机日使用时间
        duration_label = tk.Label(root, text=f"请输入手机的日使用时长（分钟）：     ")
        duration_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry = ttk.Entry(self.root)
        self.entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")


        # 创建娱乐、学习、工作、生活各方面的使用时间输入框
        self.usage_categories = ["Amusement", "Study", "Work", "Life"]
        self.category_entries = {}
        for i, category in enumerate(self.usage_categories):
            label = tk.Label(root, text=f"请输入手机在{category}方面的使用时长（分钟）：")
            label.grid(row=i+1, column=0, pady=10, padx=10)
            entry = ttk.Entry(root)
            entry.grid(row=i+1, column=1, pady=10, padx=10)
            # 创建上限时间标签
            self.limit_time = tk.StringVar()
            limit_label = ttk.Label(self.root, textvariable=self.limit_time)
            limit_label.grid(row=0, column=2, pady=10, padx=10, sticky="w")
            self.category_entries[category] = entry
        # # 创建“绘制饼图”按钮
        # pie_chart_button = ttk.Button(self.root, text="绘制饼图", command=self.submit_data)
        # pie_chart_button.grid(row=0, column=4, pady=10, padx=10, sticky="w")

    def submit_data(self):
        total_duration = float(self.entry.get())
        self.limit_time.set(f"/{total_duration}")  # 更新上限时间标签
        category_durations = {category: float(entry.get()) for category, entry in self.category_entries.items()}
        category_ratios = {category: duration / total_duration for category, duration in category_durations.items()}
        data = {"device": "手机", "total_duration": total_duration, "category_durations": category_durations, "category_ratios": category_ratios}
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        for entry in self.category_entries.values():
            entry.delete(0, 'end')
        messagebox.showinfo("信息", "手机日使用时长已记录。")

        # # 绘制饼图
        # plt.figure(figsize=(6,6))
        # plt.pie(category_ratios.values(), labels=category_ratios.keys(), autopct='%1.1f%%')
        # plt.title("Proportion of Mobile Phone usage time")
        # plt.show()

class EarphoneUsageWindow(DeviceUsageWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("无线耳机日使用时长")

        # 创建无线耳机日使用时间
        duration_label = tk.Label(root, text=f"请输入无线耳机的日使用时长（分钟）：     ")
        duration_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry = ttk.Entry(self.root)
        self.entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        # 创建娱乐、学习、工作、生活各方面的使用时间输入框
        self.usage_categories = ["Amusement", "Study", "Work", "Life"]
        self.category_entries = {}
        for i, category in enumerate(self.usage_categories):
            label = tk.Label(root, text=f"请输入无线耳机在{category}方面的使用时长（分钟）：")
            label.grid(row=i + 1, column=0, pady=10, padx=10)
            entry = ttk.Entry(root)
            entry.grid(row=i + 1, column=1, pady=10, padx=10)
            # 创建上限时间标签
            self.limit_time = tk.StringVar()
            limit_label = ttk.Label(self.root, textvariable=self.limit_time)
            limit_label.grid(row=0, column=2, pady=10, padx=10, sticky="w")
            self.category_entries[category] = entry
        # # 创建“绘制饼图”按钮
        # pie_chart_button = ttk.Button(self.root, text="绘制饼图", command=self.submit_data)
        # pie_chart_button.grid(row=0, column=4, pady=10, padx=10, sticky="w")

    def submit_data(self):
        total_duration = float(self.entry.get())
        self.limit_time.set(f"/{total_duration}")  # 更新上限时间标签
        category_durations = {category: float(entry.get()) for category, entry in self.category_entries.items()}
        category_ratios = {category: duration / total_duration for category, duration in category_durations.items()}
        data = {"device": "无线耳机", "total_duration": total_duration, "category_durations": category_durations,
                "category_ratios": category_ratios}
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        for entry in self.category_entries.values():
            entry.delete(0, 'end')
        messagebox.showinfo("信息", "无线耳机日使用时长已记录。")

        # # 绘制饼图
        # plt.figure(figsize=(6, 6))
        # plt.pie(category_ratios.values(), labels=category_ratios.keys(), autopct='%1.1f%%')
        # plt.title("Proportion of Earphone usage time")
        # plt.show()

class ComputerUsageWindow(DeviceUsageWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("电脑日使用时长")

        # 创建电脑日使用时间
        duration_label = tk.Label(root, text=f"请输入电脑的日使用时长（分钟）：     ")
        duration_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry = ttk.Entry(self.root)
        self.entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        # 创建娱乐、学习、工作、生活各方面的使用时间输入框
        self.usage_categories = ["Amusement", "Study", "Work", "Life"]
        self.category_entries = {}
        for i, category in enumerate(self.usage_categories):
            label = tk.Label(root, text=f"请输入电脑在{category}方面的使用时长（分钟）：")
            label.grid(row=i + 1, column=0, pady=10, padx=10)
            entry = ttk.Entry(root)
            entry.grid(row=i + 1, column=1, pady=10, padx=10)
            # 创建上限时间标签
            self.limit_time = tk.StringVar()
            limit_label = ttk.Label(self.root, textvariable=self.limit_time)
            limit_label.grid(row=0, column=2, pady=10, padx=10, sticky="w")
            self.category_entries[category] = entry
        # # 创建“绘制饼图”按钮
        # pie_chart_button = ttk.Button(self.root, text="绘制饼图", command=self.submit_data)
        # pie_chart_button.grid(row=0, column=4, pady=10, padx=10, sticky="w")

    def submit_data(self):
        total_duration = float(self.entry.get())
        self.limit_time.set(f"/{total_duration}")  # 更新上限时间标签
        category_durations = {category: float(entry.get()) for category, entry in self.category_entries.items()}
        category_ratios = {category: duration / total_duration for category, duration in category_durations.items()}
        data = {"device": "电脑", "total_duration": total_duration, "category_durations": category_durations,
                "category_ratios": category_ratios}
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        for entry in self.category_entries.values():
            entry.delete(0, 'end')
        messagebox.showinfo("信息", "电脑日使用时长已记录。")

        # # 绘制饼图
        # plt.figure(figsize=(6, 6))
        # plt.pie(category_ratios.values(), labels=category_ratios.keys(), autopct='%1.1f%%')
        # plt.title("Proportion of Computer usage time")
        # plt.show()

class PadUsageWindow(DeviceUsageWindow):
    def __init__(self, root, user_id: str, filename: str):
        super().__init__(root, user_id, filename)
        self.root.title("Pad日使用时长")

        # 创建手机日使用时间
        duration_label = tk.Label(root, text=f"请输入Pad的日使用时长（分钟）：     ")
        duration_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.entry = ttk.Entry(self.root)
        self.entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        # 创建娱乐、学习、工作、生活各方面的使用时间输入框
        self.usage_categories = ["Amusement", "Study", "Work", "Life"]
        self.category_entries = {}
        for i, category in enumerate(self.usage_categories):
            label = tk.Label(root, text=f"请输入Pad在{category}方面的使用时长（分钟）：")
            label.grid(row=i + 1, column=0, pady=10, padx=10)
            entry = ttk.Entry(root)
            entry.grid(row=i + 1, column=1, pady=10, padx=10)
            # 创建上限时间标签
            self.limit_time = tk.StringVar()
            limit_label = ttk.Label(self.root, textvariable=self.limit_time)
            limit_label.grid(row=0, column=2, pady=10, padx=10, sticky="w")
            self.category_entries[category] = entry
        # # 创建“绘制饼图”按钮
        # pie_chart_button = ttk.Button(self.root, text="绘制饼图", command=self.submit_data)
        # pie_chart_button.grid(row=0, column=4, pady=10, padx=10, sticky="w")

    def submit_data(self):
        total_duration = float(self.entry.get())
        self.limit_time.set(f"/{total_duration}")  # 更新上限时间标签
        category_durations = {category: float(entry.get()) for category, entry in self.category_entries.items()}
        category_ratios = {category: duration / total_duration for category, duration in category_durations.items()}
        data = {"device": "Pad", "total_duration": total_duration, "category_durations": category_durations,
                "category_ratios": category_ratios}
        UserLocalFileStorage.write_data(self.user_id, self.filename, data)
        self.entry.delete(0, 'end')
        for entry in self.category_entries.values():
            entry.delete(0, 'end')
        messagebox.showinfo("信息", "Pad日使用时长已记录。")

        # # 绘制饼图
        # plt.figure(figsize=(6, 6))
        # plt.pie(category_ratios.values(), labels=category_ratios.keys(), autopct='%1.1f%%')
        # plt.title("Proportion of Pad usage time")
        # plt.show()