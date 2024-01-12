import json
from abc import ABC, abstractmethod
import os
from collections import namedtuple, defaultdict
from datetime import timedelta, datetime, date
import random
from .data import ActivityDataFileHandler
from .file_handler import *

__all__ = ["UserLocalFileStorage", "DataStimulator"]


class LocalFileStorage:
    @staticmethod
    def write_data(data, filepath: str):
        with open(filepath, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def append_data(data, filepath: str):
        with open(filepath, 'a') as file:
            json.dump(data, file)
            file.write('\n')

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
        filepath = f'local/{user_id}/{filename}.txt'
        LocalFileStorage.write_data(data, filepath)

    @staticmethod
    def append_data(user_id: str, filename: str, data):
        filepath = f'local/{user_id}/{filename}.txt'
        LocalFileStorage.append_data(data, filepath)

    @staticmethod
    def read_data(user_id: str, filename: str):
        filepath = f'local/{user_id}/{filename}.txt'
        return LocalFileStorage.read_data(filepath)

    @staticmethod
    def check_file(user_id: str, filename: str):
        filepath = f'local/{user_id}/{filename}.txt'
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
        start_date = date.today() - timedelta(days=10)

        file_handler = ActivityDataFileHandler(user_id, 'step_count')
        file_handler.check_file()
        file_handler.delete_file()

        accumulated_data_file_handler = UserSingleFieldFileHandler(user_id, 'step_count_accumulated')
        accumulated_data_file_handler.check_file()
        accumulated_data_file_handler.delete_file()

        accumulated_data = 0

        for i in range(10 * 48):
            dt = (start_date + timedelta(days=i // 48)).strftime('%Y-%m-%d')
            # 从0点开始，每半小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(minutes=30 * (i % 48))).strftime('%H:%M')
            value = random.randint(0, 1000)
            # steps.append(step_count(dt, time, value))
            data = step_count(dt, time, value)
            accumulated_data += value
            file_handler.append_line(data)
        accumulated_data_file_handler.append_line(str(accumulated_data))

        # UserLocalFileStorage.write_data(user_id, 'step_count', steps)

    @staticmethod
    def stimulate_distance(user_id: str):
        # 每隔半小时随机记录0-1公里
        distance = namedtuple('distance', ['date', 'time', 'value'])
        distances = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=10)

        file_handler = ActivityDataFileHandler(user_id, 'distance')
        file_handler.check_file()
        file_handler.delete_file()

        accumulated_data_file_handler = UserSingleFieldFileHandler(user_id, 'distance_accumulated')
        accumulated_data_file_handler.check_file()
        accumulated_data_file_handler.delete_file()

        accumulated_data = 0

        for i in range(10 * 48):
            dt = (start_date + timedelta(days=i // 48)).strftime('%Y-%m-%d')
            # 从0点开始，每半小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(minutes=30 * (i % 48))).strftime('%H:%M')
            value = random.randint(0, 1000) / 1000
            # distances.append(distance(dt, time, value))
            data = distance(dt, time, value)
            accumulated_data += value
            file_handler.append_line(data)
        accumulated_data_file_handler.append_line(str(accumulated_data))

        # UserLocalFileStorage.write_data(user_id, 'distance', distances)

    @staticmethod
    def stimulate_flights_climbed(user_id: str):
        # 每隔半小时随机记录0-10米
        flights_climbed = namedtuple('flights_climbed', ['date', 'time', 'value'])
        flights = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=10)

        file_handler = ActivityDataFileHandler(user_id, 'flights_climbed')
        file_handler.check_file()
        file_handler.delete_file()

        accumulated_data_file_handler = UserSingleFieldFileHandler(user_id, 'flights_climbed_accumulated')
        accumulated_data_file_handler.check_file()
        accumulated_data_file_handler.delete_file()

        accumulated_data = 0

        for i in range(10 * 48):
            dt = (start_date + timedelta(days=i // 48)).strftime('%Y-%m-%d')
            # 从0点开始，每半小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(minutes=30 * (i % 48))).strftime('%H:%M')
            value = random.randint(0, 10)
            # flights.append(flights_climbed(dt, time, value))
            data = flights_climbed(dt, time, value)
            accumulated_data += value
            file_handler.append_line(data)
        accumulated_data_file_handler.append_line(str(accumulated_data))

        # UserLocalFileStorage.write_data(user_id, 'flights_climbed', flights)

    @staticmethod
    def stimulate_active_energy_burned(user_id: str):
        # 每隔半小时随机记录0-300千卡
        active_energy_burned = namedtuple('active_energy_burned', ['date', 'time', 'value'])
        energies = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=10)

        file_handler = ActivityDataFileHandler(user_id, 'active_energy_burned')
        file_handler.check_file()
        file_handler.delete_file()

        accumulated_data_file_handler = UserSingleFieldFileHandler(user_id, 'active_energy_burned_accumulated')
        accumulated_data_file_handler.check_file()
        accumulated_data_file_handler.delete_file()

        accumulated_data = 0

        for i in range(10 * 48):
            dt = (start_date + timedelta(days=i // 48)).strftime('%Y-%m-%d')
            # 从0点开始，每半小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(minutes=30 * (i % 48))).strftime('%H:%M')
            value = random.randint(0, 300)
            # energies.append(active_energy_burned(dt, time, value))
            data = active_energy_burned(dt, time, value)
            accumulated_data += value
            file_handler.append_line(data)
        accumulated_data_file_handler.append_line(str(accumulated_data))

        # UserLocalFileStorage.write_data(user_id, 'active_energy_burned', energies)

    @staticmethod
    def stimulate_exercise_minutes(user_id: str):
        # 每隔半小时随机记录0-5分钟
        exercise_time = namedtuple('exercise_minutes', ['date', 'time', 'value'])
        times = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=10)

        file_handler = ActivityDataFileHandler(user_id, 'exercise_minutes')
        file_handler.check_file()
        file_handler.delete_file()

        accumulated_data_file_handler = UserSingleFieldFileHandler(user_id, 'exercise_minutes_accumulated')
        accumulated_data_file_handler.check_file()
        accumulated_data_file_handler.delete_file()

        accumulated_data = 0

        for i in range(10 * 48):
            dt = (start_date + timedelta(days=i // 48)).strftime('%Y-%m-%d')
            # 从0点开始，每半小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(minutes=30 * (i % 48))).strftime('%H:%M')
            value = random.randint(0, 5)
            # times.append(exercise_time(dt, time, value))
            data = exercise_time(dt, time, value)
            accumulated_data += value

            file_handler.append_line(data)
        accumulated_data_file_handler.append_line(str(accumulated_data))

        # UserLocalFileStorage.write_data(user_id, 'exercise_minutes', times)

    @staticmethod
    def stimulate_active_hours(user_id: str):
        # 每隔一小时随机记录0-1小时
        active_hours = namedtuple('active_hours', ['date', 'time', 'value'])
        hours = []
        # 从三年前开始记录
        start_date = date.today() - timedelta(days=10)

        file_handler = ActivityDataFileHandler(user_id, 'active_hours')
        file_handler.check_file()
        file_handler.delete_file()

        accumulated_data_file_handler = UserSingleFieldFileHandler(user_id, 'active_hours_accumulated')
        accumulated_data_file_handler.check_file()
        accumulated_data_file_handler.delete_file()

        accumulated_data = 0

        for i in range(10 * 24):
            dt = (start_date + timedelta(days=i // 24)).strftime('%Y-%m-%d')
            # 从0点开始，每小时记录一次
            time = (datetime.strptime(dt, '%Y-%m-%d') + timedelta(hours=i % 24)).strftime('%H:%M')
            value = random.randint(0, 1)
            # hours.append(active_hours(dt, time, value))
            data = active_hours(dt, time, value)
            accumulated_data += value

            file_handler.append_line(data)
        accumulated_data_file_handler.append_line(str(accumulated_data))

        # UserLocalFileStorage.write_data(user_id, 'active_hours', hours)


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
