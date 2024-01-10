"""这个模块包含了所有的健康数据的类"""
import json
from abc import ABC, abstractmethod
from collections import namedtuple, defaultdict
from datetime import date as dt_date
import os
from datetime import datetime
from enum import Enum
import time
from .consts import *
from .decorators import print_run_time

__all__ = [
    "ActivityDataFileHandler",
    "ActivityDataStatistics",
    "StepCount",
    "Distance",
    "FlightsClimbed",
    "ActiveEnergyBurned",
    "Profile",
    "Distance",
    "FlightsClimbed",
    "ActiveEnergyBurned",
    "ACTIVITY_DATA_TYPES",
    "STATIC_DATA_TYPES",
    "DATA_TYPES"
]


class ACTIVITY_DATA_TYPES(Enum):
    """活动数据类型枚举类"""
    STEP_COUNT = 'step_count'
    DISTANCE = 'distance'
    FLIGHTS_CLIMBED = 'flights_climbed'
    ACTIVE_ENERGY_BURNED = 'active_energy_burned'
    EXERCISE_MINUTES = 'exercise_minutes'
    ACTIVE_HOURS = 'active_hours'


class STATIC_DATA_TYPES(Enum):
    """静态数据类型枚举类"""
    PROFILE = 'profile'


class DATA_TYPES(Enum):
    """数据类型枚举类"""
    PROFILE = 'profile'
    STEP_COUNT = 'step_count'
    DISTANCE = 'distance'
    FLIGHTS_CLIMBED = 'flights_climbed'
    ACTIVE_ENERGY_BURNED = 'active_energy_burned'
    EXERCISE_MINUTES = 'exercise_minutes'
    ACTIVE_HOURS = 'active_hours'


# from .util import UserLocalFileStorage as LocalFileStorage
from .file_handler import user_file_handler_factory, UserMultiFieldFileHandler, UserSingleFieldFileHandler


class BaseData(ABC):
    """数据基类"""

    # @abstractmethod
    # def calculate_statistics(self):
    #     pass
    #
    # @abstractmethod
    # def display_statistics(self):
    #     pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    # @abstractmethod
    # def get_data(self):
    #     """提供数据请求接口"""
    #     pass


class BaseActivityData(BaseData):
    """(弃用)活动数据基类"""

    @abstractmethod
    def get_data_by_date(self, date: dt_date):
        """
        获取指定日期的所有数据
        :param date:
        :return:
        """
        pass

    @abstractmethod
    def get_daily_total(self, date: dt_date):
        """
        获取指定日期的数据总和
        :param date:
        :return:
        """
        pass

    @abstractmethod
    def get_all_daily_total(self):
        pass

    @abstractmethod
    def get_all_dates(self):
        pass

    @abstractmethod
    def get_latest_daily_total(self):
        pass


class ActivityDataStatistics:
    """活动数据统计类"""

    def __init__(self, user_id):
        # self.steps = StepCount(user_id)
        # self.distance = Distance(user_id)
        # self.flights_climbed = FlightsClimbed(user_id)
        # self.active_energy_burned = ActiveEnergyBurned(user_id)
        # self.exercise_minutes = ExerciseMinutes(user_id)
        # self.active_hours = ActiveHours(user_id)

        self.activity_datas = {
            'steps': ActivityDataFileHandler(user_id, 'step_count'),
            'distance': ActivityDataFileHandler(user_id, 'distance'),
            'flights_climbed': ActivityDataFileHandler(user_id, 'flights_climbed'),
            'active_energy_burned': ActivityDataFileHandler(user_id, 'active_energy_burned'),
            'exercise_minutes': ActivityDataFileHandler(user_id, 'exercise_minutes'),
            'active_hours': ActivityDataFileHandler(user_id, 'active_hours')
        }

        # self.steps = ActivityDataFileHandler(user_id, 'step_count')
        # self.distance = ActivityDataFileHandler(user_id, 'distance')
        # self.flights_climbed = ActivityDataFileHandler(user_id, 'flights_climbed')
        # self.active_energy_burned = ActivityDataFileHandler(user_id, 'active_energy_burned')
        # self.exercise_minutes = ActivityDataFileHandler(user_id, 'exercise_minutes')
        # self.active_hours = ActivityDataFileHandler(user_id, 'active_hours')

    def get_all_daily_total(self) -> dict:
        """
        获取所有历史数据总和，返回一个字典
        :return:
        """
        return {key: value.get_all_daily_total() for key, value in self.activity_datas.items()}

    def get_daily_total(self, data_type, date):
        """
        获取指定日期的数据总和，返回一个字典
        :param data_type: 数据类型，如 'steps', 'distance', 等
        :param date: 日期对象
        :return: 数据总和
        """
        if data_type in self.activity_datas:
            return self.activity_datas[data_type].get_daily_total(date)
        else:
            return 0

    # def get_all_daily_total(self):
    #     """
    #     获取所有日期的数据总和，返回一个字典
    #     :return:
    #     """
    #     return {
    #         'steps': self.steps.get_all_daily_total(),
    #         'distance': self.distance.get_all_daily_total(),
    #         'flights_climbed': self.flights_climbed.get_all_daily_total(),
    #         'active_energy_burned': self.active_energy_burned.get_all_daily_total(),
    #         'exercise_minutes': self.exercise_minutes.get_all_daily_total(),
    #         'active_hours': self.active_hours.get_all_daily_total()
    #     }

    def get_latest_daily_total(self) -> dict:
        """
        获取最近一天的数据总和，返回一个字典
        :return: {'steps', 'distance', 'flights_climbed', 'active_energy_burned, 'exercise_minutes', 'active_hours'}
        """
        return {key: value.get_latest_daily_total() for key, value in self.activity_datas.items()}

    def get_daily_data(self, date):
        """
        获取指定日期的数据，返回一个字典
        :param date: 日期对象
        :return: {'steps', 'distance', 'flights_climbed', 'active_energy_burned, 'exercise_minutes', 'active_hours'}
        """
        daily_data = {}
        for key, value in self.activity_datas.items():
            daily_data[key] = value.get_daily_data(date)
        return daily_data

    # def get_latest_daily_total(self) -> dict:
    #     """
    #     获取最近一天的数据总和，返回一个字典
    #     :return: {'steps', 'distance', 'flights_climbed', 'active_energy_burned, 'exercise_minutes', 'active_hours'}
    #     """
    #     return {
    #         'steps': self.steps.get_latest_daily_total(),
    #         'distance': self.distance.get_latest_daily_total(),
    #         'flights_climbed': self.flights_climbed.get_latest_daily_total(),
    #         'active_energy_burned': self.active_energy_burned.get_latest_daily_total(),
    #         'exercise_minutes': self.exercise_minutes.get_latest_daily_total(),
    #         'active_hours': self.active_hours.get_latest_daily_total()
    #     }


class WeightBaseData(BaseData):
    """体重身体测量数据类"""

    def __init__(self):
        self.data = []

    def add_data(self, data_value):
        self.data.append(data_value)


class Profile(BaseData):
    """个人资料类， 是静态数据类"""

    def __init__(self, user_id):
        self._datatype = DATA_TYPES.PROFILE.value
        self._user_id = user_id
        self._FIELD_LIST = 'gender', 'birth', 'height', 'weight'
        self._profile = namedtuple('Profile', self._FIELD_LIST)
        self._data_handler: UserSingleFieldFileHandler = user_file_handler_factory(self._user_id, self._datatype)

        if not self.check_data():
            self.init_data()

    def load_data(self):
        """
        弃用
        :return:
        """
        # if LocalFileStorage.check_file(self._user_id, self._datatype):
        #     self.data = self._profile(*LocalFileStorage.read_data(self._user_id, self._datatype))
        # else:
        #     self.data = self._profile('未知', '未知', '未知', '未知')
        #     self.save_data()

    def save_data(self):
        """
        弃用
        :return:
        """
        # LocalFileStorage.write_data(self._user_id, self._datatype, self.data)

    def update_data(self, data_value: list):
        """
        弃用
        :param data_value:
        :return:
        """
        self.data = self._profile(*data_value)
        self.save_data()

    def init_data(self):
        """
        初始化数据为默认值“未知”
        :return:
        """
        self._data_handler.delete_file()
        for i in range(len(self._FIELD_LIST)):
            self._data_handler.append_line('未知')

    def check_data(self) -> bool:
        """
        检查文件是否存在，并检查文件中的数据行数是否完整
        :return:
        """
        return (self._data_handler.check_file()
                and self._data_handler.get_file_length() == len(self._FIELD_LIST))

    def update_data_by_field(self, field: str, data_value):
        """
        更新指定字段的数据
        :param field: ['gender', 'birth', 'height', 'weight']
        :param data_value:
        :return:
        """
        self._data_handler.modify_line(self._FIELD_LIST.index(field), data_value)

    def get_dict_data(self) -> dict:
        """返回用户的个人资料"""
        # return self.data._asdict()

        return {field: self._data_handler.read_line(i) for i, field in enumerate(self._FIELD_LIST)}

    def get_namedtuple_data(self) -> namedtuple:
        return self._profile(*(self._data_handler.read_line(i) for i, _ in enumerate(self._FIELD_LIST)))

    def __repr__(self):
        # return f'Profile({self.data})'
        return f'Profile({self.get_dict_data()})'

    def save_profile_to_file(self):
        """将用户的个人信息保存到本地文件中"""
        profile_data = {
            'gender': self.gender,
            'birth': self.birth,
            'height': self.height,
            'weight': self.weight
        }

        local_directory = 'local'
        os.makedirs(local_directory, exist_ok=True)

        file_path = f'local/{self._user_id}_profile.json'

        with open(file_path, 'w') as f:
            json.dump(profile_data, f)

    def save_profile(self):
        """保存用户输入的个人资料"""
        self.gender = self.gender_combobox.get()
        self.birth = self.current_date_label["text"]
        self.height = self.height_entry.get()
        self.weight = self.weight_entry.get()

        # 将修改后的资料保存到文件中
        self.save_profile_to_file()

        # 更新用户的个人资料
        self.user.profile.update_data_by_field("gender", self.gender)
        self.user.profile.update_data_by_field("height", self.height)
        self.user.profile.update_data_by_field("weight", self.weight)

        # 关闭窗口
        self.root.destroy()
        self.previous.refresh_profile()


class ManualUpdateInterface(ABC):
    """手动更新接口"""

    @abstractmethod
    def manual_update(self):
        pass


class AutoUpdateInterface(ABC):
    """自动更新接口"""

    @abstractmethod
    def auto_update(self):
        pass


class UpdateFromDevice(AutoUpdateInterface):
    """从设备更新接口"""

    @staticmethod
    def isAvailable():
        """检查设备是否连接"""
        pass

    @abstractmethod
    def auto_update(self):
        pass


class UpdateFromPhone(UpdateFromDevice):
    """从手机更新接口"""

    @staticmethod
    def isAvailable():
        return False

    def auto_update(self):
        pass


class UpdateFromWatch(UpdateFromDevice):
    """从手表更新接口"""

    @staticmethod
    def isAvailable():
        return False

    def auto_update(self):
        pass


class UpdateFromFile:
    """从文件更新接口"""

    # def __init__(self, user_id, data_type, data_value, date: dt_date):
    #     self._user_id = user_id
    #     self._data_type = data_type
    #     self._data_value = data_value
    #     self._date = date

    @staticmethod
    def isAvailable():
        return True

    @staticmethod
    def auto_update(user_id, data_type):
        # if LocalFileStorage.check_file(user_id, data_type):
        #     data = LocalFileStorage.read_data(user_id, data_type)
        # else:
        #     raise FileNotFoundError(f'用户 {user_id} 的 {data_type} 数据文件不存在')
        #     # data = None
        # return data
        pass


class AutoUpdateFromMultipleWays(UpdateFromPhone, UpdateFromWatch, UpdateFromFile):
    """（弃用）支持多种方式自动更新的数据，统一管理获取数据的方法"""

    def __init__(self, available_ways: list):
        self._available_ways = available_ways

    def auto_update(self):
        for way in self._available_ways:
            if way.isAvailable():
                # way.auto_update()
                return way.auto_update


# class AutoUpdateFromMultipleWays:
#     """（new）支持多种方式自动更新的数据，统一管理获取数据的方法"""
#
#     @staticmethod
#     def auto_update(available_ways: list):
#         """
#         从多种方式中选择一种可用的方式来自动更新数据
#         :param available_ways:
#         :return:
#         """
#         for way in available_ways:
#             if way.isAvailable():
#                 # way.auto_update()
#                 return way.auto_update


class ActivityDataFileHandler(UserMultiFieldFileHandler):
    """活动数据文件处理类"""

    def __init__(self, user_id, data_type):
        """
        从ACITIVITY_DATA_TYPES中选择一个数据类型
        数据类型包括：['step_count', 'distance', 'flights_climbed', 'active_energy_burned', 'exercise_minutes', 'active_hours']
        :param user_id:
        :param data_type:
        """
        super().__init__(user_id, data_type)
        self._FIELD_LIST = 'date', 'time', 'value'
        self._activity_data = namedtuple(self._data_type, self._FIELD_LIST)
        self.check_file()

    def read_line(self, pos: int) -> [tuple, None]:
        """
        读取指定行的数据
        :param pos:
        :return:
        """
        data = super().read_line(pos)
        if data is None:
            return None
        return self._activity_data(*data)

    @print_run_time
    def get_data_by_date(self, date: str) -> list:
        """
        读取指定日期的数据
        :param date:
        :return: 返回一个列表，列表中的每个元素是一个namedtuple(date, time, value)
        """
        # date_str = date.strftime('%Y-%m-%d')
        selected_lines = self.search_by_field_all(0, date)
        return [self.read_line(i) for i in selected_lines]

    def get_data_by_date_range(self, start_date: str, end_date: str) -> list:
        """
        读取指定日期范围内的数据
        :param start_date:
        :param end_date:
        :return: 返回一个列表，列表中的每个元素是一个namedtuple(date, time, value)
        """
        # start_date_str = start_date.strftime('%Y-%m-%d')
        # end_date_str = end_date.strftime('%Y-%m-%d')
        selected_lines = self.search_by_field_range(0, (start_date, end_date))
        return [self.read_line(i) for i in selected_lines]

    @print_run_time
    def get_daily_total(self, date: str):
        """
        获取指定日期的数据总和
        :param date:
        :return:
        """
        if date is None:
            return 0
        return sum([float(x.value) for x in self.get_data_by_date(date)])

    def get_daily_total_range(self, start_date: str, end_date: str):
        """
        获取指定日期范围内的数据总和
        :param start_date:
        :param end_date:
        :return:
        """
        return sum([x.value for x in self.get_data_by_date_range(start_date, end_date)])

    def get_start_date(self):
        """
        获取数据中的最早日期
        :return:
        """
        return self.read_line(0).date

    def get_end_date(self):
        """
        获取数据中的最晚日期
        :return:
        """
        data = self.read_line(-1)
        if data is None:
            return None
        return self.read_line(-1).date

    @print_run_time
    def get_latest_daily_total(self):
        """
        获取最近一天的数据总和
        :return:
        """
        return self.get_daily_total(self.get_end_date())

    def get_daily_data(self, date: str) -> [tuple, None]:
        """
        获取指定日期的数据
        :param date: 日期字符串
        :return: 返回一个namedtuple(date, time, value)或None
        """
        selected_lines = self.search_by_field_all(0, date)
        if selected_lines:
            return self.read_line(selected_lines[0])
        return None

    def get_daily_data_latest(self) -> [tuple, None]:
        """
        获取最新一天的数据
        :return: 返回一个namedtuple(date, time, value)或None
        """
        end_date = self.get_end_date()
        if end_date is not None:
            try:
                # 将 end_date 解析为日期对象
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
                # 将日期对象转换为整数
                end_date_pos = int(end_date_obj.timestamp())
                print("end_date:", end_date)  # 添加这行代码
                return self.read_line(end_date_pos)
            except ValueError as e:
                print(f"Error parsing date: {e}")
        return None

    @print_run_time
    def get_latest_daily_total(self):
        """
        获取最近一天的数据总和
        :return:
        """
        latest_data = self.get_daily_data_latest()
        if latest_data is not None:
            # 将 end_date 直接作为字符串传递给 get_daily_total
            end_date = latest_data.date
            return float(self.get_daily_total(end_date))
        return 0

    def get_all_daily_total(self) -> float:
        """
        获取历史数据总和
        :return:
        """
        return sum([x.value for x in self.read_lines([x for x in range(self.get_file_length())])])



class ActivityData(BaseData):
    """
    弃用，使用ActivityDataFileHandler代替
    活动数据类, 数据格式为：(date, time, value)
    """

    def __init__(self, user_id, data_type):
        """
        从ACITIVITY_DATA_TYPES中选择一个数据类型
        数据类型包括：['step_count', 'distance', 'flights_climbed', 'active_energy_burned', 'exercise_minutes', 'active_hours']
        :param user_id:
        :param data_type: ACITIVITY_DATA_TYPES中的一个
        """
        self._datatype = data_type.value  # 数据类型
        self._user_id = user_id
        self._activity_data = namedtuple(self._datatype, ['date', 'time', 'value'])
        # self.data = None
        self._update_ways = [UpdateFromWatch, UpdateFromPhone, UpdateFromFile]  # TODO: 优化更新方式的选择
        self._data_handler: UserMultiFieldFileHandler = user_file_handler_factory(self._user_id, self._datatype)

        # self.load_data()

    def load_data(self):
        """
        弃用
        :return:
        """
        self.data = [self._activity_data(*x) for x in
                     self.auto_update(self._update_ways)(self._user_id, self._datatype)]

    def save_data(self):
        """
        弃用
        :return:
        """
        pass

    def get_data_by_date(self, date: dt_date) -> list:
        """
        获取指定日期的所有数据
        :param date:
        :return: 返回一个列表，列表中的每个元素是一个namedtuple(date, time, value)
        """
        # return [x for x in self.data if x.date == date]
        return [self._activity_data(*x) for x in self._data_handler.read_data_by_date(date)]

    def get_daily_total(self, date: dt_date):
        return sum([x.value for x in self.get_data_by_date(date)])

    def get_all_daily_total(self):
        return {x: self.get_daily_total(x) for x in self.get_all_dates()}

    def get_all_dates(self):
        return list(set([x.date for x in self.data]))

    def get_latest_daily_total(self):
        return self.get_daily_total(max(self.get_all_dates()))


class StepCount(BaseActivityData, AutoUpdateFromMultipleWays):
    """步数类"""

    def __init__(self, user_id):
        self._datatype = 'step_count'
        self.user_id = user_id
        self._step_count = namedtuple(self._datatype, ['date', 'time', 'steps'])
        self.data = None
        self.daily_total_data = None
        super().__init__([UpdateFromWatch, UpdateFromPhone, UpdateFromFile])
        self._update_ways = [UpdateFromWatch, UpdateFromPhone, UpdateFromFile]

        self.load_data()

    def load_data(self):
        self.data = [self._step_count(*x) for x in self.auto_update()(self.user_id, self._datatype)]

    def save_data(self):
        pass

    def get_data_by_date(self, date: dt_date):
        return [x for x in self.data if x.date == date]

    def get_daily_total(self, date: dt_date):
        return sum([x.steps for x in self.get_data_by_date(date)])

    def get_all_daily_total(self):
        return {x: self.get_daily_total(x) for x in self.get_all_dates()}

    def get_all_dates(self):
        return list(set([x.date for x in self.data]))

    def get_latest_daily_total(self):
        return self.get_daily_total(max(self.get_all_dates()))


class Distance(AutoUpdateFromMultipleWays, BaseActivityData):
    """距离类"""

    def __init__(self, user_id):
        self._datatype = 'distance'
        self.user_id = user_id
        self._distance = namedtuple(self._datatype, ['date', 'time', 'distance'])
        self.data = None
        super().__init__([UpdateFromWatch, UpdateFromPhone, UpdateFromFile])

        self.load_data()

    def load_data(self):
        self.data = [self._distance(*x) for x in self.auto_update()(self.user_id, self._datatype)]

    def save_data(self):
        pass

    def get_data_by_date(self, date: dt_date):
        return [x for x in self.data if x.date == date]

    def get_daily_total(self, date: dt_date):
        return sum([x.distance for x in self.get_data_by_date(date)])

    def get_all_daily_total(self):
        return {x: self.get_daily_total(x) for x in self.get_all_dates()}

    def get_all_dates(self):
        return list(set([x.date for x in self.data]))

    def get_latest_daily_total(self):
        return self.get_daily_total(max(self.get_all_dates()))


class FlightsClimbed(AutoUpdateFromMultipleWays, BaseActivityData):
    """爬楼类"""

    def __init__(self, user_id):
        self._datatype = 'flights_climbed'
        self.user_id = user_id
        self._flights_climbed = namedtuple(self._datatype, ['date', 'time', 'flights_climbed'])
        self.data = None
        super().__init__([UpdateFromWatch, UpdateFromPhone, UpdateFromFile])

        self.load_data()

    def load_data(self):
        self.data = [self._flights_climbed(*x) for x in self.auto_update()(self.user_id, self._datatype)]

    def save_data(self):
        pass

    def get_data_by_date(self, date: dt_date):
        return [x for x in self.data if x.date == date]

    def get_daily_total(self, date: dt_date):
        return sum([x.flights_climbed for x in self.get_data_by_date(date)])

    def get_all_daily_total(self):
        return {x: self.get_daily_total(x) for x in self.get_all_dates()}

    def get_all_dates(self):
        return list(set([x.date for x in self.data]))

    def get_latest_daily_total(self):
        return self.get_daily_total(max(self.get_all_dates()))


class ActiveEnergyBurned(AutoUpdateFromMultipleWays, BaseActivityData):
    """活动能量类"""

    def __init__(self, user_id):
        self._datatype = 'active_energy_burned'
        self.user_id = user_id
        self._active_energy_burned = namedtuple(self._datatype, ['date', 'time', 'active_energy_burned'])
        self.data = None
        super().__init__([UpdateFromWatch, UpdateFromPhone, UpdateFromFile])

        self.load_data()

    def load_data(self):
        self.data = [self._active_energy_burned(*x) for x in self.auto_update()(self.user_id, self._datatype)]

    def save_data(self):
        pass

    def get_data_by_date(self, date: dt_date):
        return [x for x in self.data if x.date == date]

    def get_daily_total(self, date: dt_date):
        return sum([x.active_energy_burned for x in self.get_data_by_date(date)])

    def get_all_daily_total(self):
        return {x: self.get_daily_total(x) for x in self.get_all_dates()}

    def get_all_dates(self):
        return list(set([x.date for x in self.data]))

    def get_latest_daily_total(self):
        return self.get_daily_total(max(self.get_all_dates()))


class ExerciseMinutes(AutoUpdateFromMultipleWays, BaseActivityData):
    """锻炼时长"""

    def __init__(self, user_id):
        self._datatype = 'exercise_minutes'
        self.user_id = user_id
        self._exercise_minutes = namedtuple(self._datatype, ['date', 'time', 'exercise_minutes'])
        self.data = None
        super().__init__([UpdateFromWatch, UpdateFromPhone, UpdateFromFile])

        self.load_data()

    def load_data(self):
        self.data = [self._exercise_minutes(*x) for x in self.auto_update()(self.user_id, self._datatype)]

    def save_data(self):
        pass

    def get_data_by_date(self, date: dt_date):
        return [x for x in self.data if x.date == date]

    def get_daily_total(self, date: dt_date):
        return sum([x.exercise_minutes for x in self.get_data_by_date(date)])

    def get_all_daily_total(self):
        return {x: self.get_daily_total(x) for x in self.get_all_dates()}

    def get_all_dates(self):
        return list(set([x.date for x in self.data]))

    def get_latest_daily_total(self):
        return self.get_daily_total(max(self.get_all_dates()))


class ActiveHours(AutoUpdateFromMultipleWays, BaseActivityData):
    """活动时长"""

    def __init__(self, user_id):
        self._datatype = 'active_hours'
        self.user_id = user_id
        self._active_hours = namedtuple(self._datatype, ['date', 'time', 'active_hours'])
        self.data = None
        super().__init__([UpdateFromWatch, UpdateFromPhone, UpdateFromFile])

        self.load_data()

    def load_data(self):
        self.data = [self._active_hours(*x) for x in self.auto_update()(self.user_id, self._datatype)]

    def save_data(self):
        pass

    def get_data_by_date(self, date: dt_date):
        return [x for x in self.data if x.date == date]

    def get_daily_total(self, date: dt_date):
        return sum([x.active_hours for x in self.get_data_by_date(date)])

    def get_all_daily_total(self):
        return {x: self.get_daily_total(x) for x in self.get_all_dates()}

    def get_all_dates(self):
        return list(set([x.date for x in self.data]))

    def get_latest_daily_total(self):
        return self.get_daily_total(max(self.get_all_dates()))
