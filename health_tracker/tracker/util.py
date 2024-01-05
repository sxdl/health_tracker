import json
from abc import ABC, abstractmethod
import os
from collections import namedtuple, defaultdict
from datetime import timedelta, datetime, date
import random

__all__ = ["UserLocalFileStorage", "DataStimulator"]


class LocalFileStorage:
    @staticmethod
    def write_data(data, filepath: str):
        with open(filepath, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def read_data(filepath: str):
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def check_file(filepath: str):
        try:
            with open(filepath, 'r') as file:
                return True
        except FileNotFoundError:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            return False


class UserLocalFileStorage:
    @staticmethod
    def write_data(user_id: str, filename: str, data):
        filepath = f'local/{user_id}/{filename}.json'
        LocalFileStorage.write_data(data, filepath)

    @staticmethod
    def read_data(user_id: str, filename: str):
        filepath = f'local/{user_id}/{filename}.json'
        return LocalFileStorage.read_data(filepath)

    @staticmethod
    def check_file(user_id: str, filename: str):
        filepath = f'local/{user_id}/{filename}.json'
        return LocalFileStorage.check_file(filepath)


class DataStimulator:
    @staticmethod
    def stimulate_all_data(user_id: str):
        DataStimulator.stimulate_step_count(user_id)
        DataStimulator.stimulate_distance(user_id)
        DataStimulator.stimulate_flights_climbed(user_id)
        DataStimulator.stimulate_active_energy_burned(user_id)
        DataStimulator.stimulate_exercise_minutes(user_id)
        DataStimulator.stimulate_active_hours(user_id)

    @staticmethod
    def stimulate_step_count(user_id: str):
        # 每隔半小时随机记录0-1000步
        step_count = namedtuple('step_count', ['date', 'time', 'value'])
        steps = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=3 * 365)
        for i in range(3 * 365 * 48):
            dt = (start_date + timedelta(days=i // 48)).strftime('%Y-%m-%d')
            # 从0点开始，每半小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(minutes=30 * (i % 48))).strftime('%H:%M')
            value = random.randint(0, 1000)
            steps.append(step_count(dt, time, value))

        UserLocalFileStorage.write_data(user_id, 'step_count', steps)

    @staticmethod
    def stimulate_distance(user_id: str):
        # 每隔半小时随机记录0-1公里
        distance = namedtuple('distance', ['date', 'time', 'value'])
        distances = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=3 * 365)
        for i in range(3 * 365 * 48):
            dt = (start_date + timedelta(days=i // 48)).strftime('%Y-%m-%d')
            # 从0点开始，每半小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(minutes=30 * (i % 48))).strftime('%H:%M')
            value = random.randint(0, 1000) / 1000
            distances.append(distance(dt, time, value))

        UserLocalFileStorage.write_data(user_id, 'distance', distances)

    @staticmethod
    def stimulate_flights_climbed(user_id: str):
        # 每隔半小时随机记录0-10米
        flights_climbed = namedtuple('flights_climbed', ['date', 'time', 'value'])
        flights = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=3 * 365)
        for i in range(3 * 365 * 48):
            dt = (start_date + timedelta(days=i // 48)).strftime('%Y-%m-%d')
            # 从0点开始，每半小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(minutes=30 * (i % 48))).strftime('%H:%M')
            value = random.randint(0, 10)
            flights.append(flights_climbed(dt, time, value))

        UserLocalFileStorage.write_data(user_id, 'flights_climbed', flights)

    @staticmethod
    def stimulate_active_energy_burned(user_id: str):
        # 每隔半小时随机记录0-300千卡
        active_energy_burned = namedtuple('active_energy_burned', ['date', 'time', 'value'])
        energies = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=3 * 365)
        for i in range(3 * 365 * 48):
            dt = (start_date + timedelta(days=i // 48)).strftime('%Y-%m-%d')
            # 从0点开始，每半小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(minutes=30 * (i % 48))).strftime('%H:%M')
            value = random.randint(0, 300)
            energies.append(active_energy_burned(dt, time, value))

        UserLocalFileStorage.write_data(user_id, 'active_energy_burned', energies)

    @staticmethod
    def stimulate_exercise_minutes(user_id: str):
        # 每隔半小时随机记录0-5分钟
        exercise_time = namedtuple('exercise_minutes', ['date', 'time', 'value'])
        times = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=3 * 365)
        for i in range(3 * 365 * 48):
            dt = (start_date + timedelta(days=i // 48)).strftime('%Y-%m-%d')
            # 从0点开始，每半小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(minutes=30 * (i % 48))).strftime('%H:%M')
            value = random.randint(0, 5)
            times.append(exercise_time(dt, time, value))

        UserLocalFileStorage.write_data(user_id, 'exercise_minutes', times)

    @staticmethod
    def stimulate_active_hours(user_id: str):
        # 每隔一小时随机记录0-1小时
        active_hours = namedtuple('active_hours', ['date', 'time', 'value'])
        hours = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=3 * 365)
        for i in range(3 * 365 * 24):
            dt = (start_date + timedelta(days=i // 24)).strftime('%Y-%m-%d')
            # 从0点开始，每小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(hours=i % 24)).strftime('%H:%M')
            value = random.randint(0, 1)
            hours.append(active_hours(dt, time, value))

        UserLocalFileStorage.write_data(user_id, 'active_hours', hours)


class UserInputData:
    @staticmethod
    def input_data(user_id: str, filename: str):
        print(f"请输入要存储在 {filename} 中的数据：")
        data = input()
        UserLocalFileStorage.write_data(user_id, filename, data)

    @staticmethod
    def update_data(user_id: str, filename: str):
        print(f"请输入要更新在 {filename} 中的数据：")
        data = input()
        if UserLocalFileStorage.check_file(user_id, filename):
            old_data = UserLocalFileStorage.read_data(user_id, filename)
            old_data.append(data)
            UserLocalFileStorage.write_data(user_id, filename, old_data)
        else:
            print(f"{filename} 文件不存在。")
