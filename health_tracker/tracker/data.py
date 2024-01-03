"""这个模块包含了所有的健康数据的类"""

from abc import ABC, abstractmethod
from collections import namedtuple, defaultdict
from datetime import date as dt_date
from .util import UserLocalFileStorage as LocalFileStorage
from enum import Enum

__all__ = ["ActivityDataStatistics", "StepCount", "Distance", "FlightsClimbed", "ActiveEnergyBurned", "Profile",
           "Distance", "FlightsClimbed", "ActiveEnergyBurned"]


class ACTIVITY_DATA_TYPES(Enum):
    """活动数据类型枚举类"""
    STEP_COUNT = 'step_count'
    DISTANCE = 'distance'
    FLIGHTS_CLIMBED = 'flights_climbed'
    ACTIVE_ENERGY_BURNED = 'active_energy_burned'
    EXERCISE_MINUTES = 'exercise_minutes'
    ACTIVE_HOURS = 'active_hours'


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
        self.steps = StepCount(user_id)
        self.distance = Distance(user_id)
        self.flights_climbed = FlightsClimbed(user_id)
        self.active_energy_burned = ActiveEnergyBurned(user_id)
        self.exercise_minutes = ExerciseMinutes(user_id)
        self.active_hours = ActiveHours(user_id)

        # self.data = defaultdict(list, {
        #     'steps': [],
        #     'distance': [],
        #     'flights_climbed': [],
        #     'active_energy_burned': []
        # })

    def get_all_daily_total(self):
        return {
            'steps': self.steps.get_all_daily_total(),
            'distance': self.distance.get_all_daily_total(),
            'flights_climbed': self.flights_climbed.get_all_daily_total(),
            'active_energy_burned': self.active_energy_burned.get_all_daily_total(),
            'exercise_minutes': self.exercise_minutes.get_all_daily_total(),
            'active_hours': self.active_hours.get_all_daily_total()
        }

    def get_latest_daily_total(self) -> dict:
        return {
            'steps': self.steps.get_latest_daily_total(),
            'distance': self.distance.get_latest_daily_total(),
            'flights_climbed': self.flights_climbed.get_latest_daily_total(),
            'active_energy_burned': self.active_energy_burned.get_latest_daily_total(),
            'exercise_minutes': self.exercise_minutes.get_latest_daily_total(),
            'active_hours': self.active_hours.get_latest_daily_total()
        }


class WeightBaseData(BaseData):
    """体重身体测量数据类"""

    def __init__(self):
        self.data = []

    def add_data(self, data_value):
        self.data.append(data_value)


class Profile(BaseData):
    """个人资料类"""

    def __init__(self, user_id):
        self._datatype = 'profile'
        self.user_id = user_id
        self._profile = namedtuple(self._datatype, ['gender', 'birth', 'height', 'weight'])
        self.data = None
        self.load_data()

    def load_data(self):
        if LocalFileStorage.check_file(self.user_id, self._datatype):
            self.data = self._profile(*LocalFileStorage.read_data(self.user_id, self._datatype))
        else:
            self.data = self._profile('未知', '未知', '未知', '未知')
            self.save_data()

    def save_data(self):
        LocalFileStorage.write_data(self.user_id, self._datatype, self.data)

    def update_data(self, data_value: list):
        self.data = self._profile(*data_value)
        self.save_data()

    def get_data(self) -> dict:
        """返回用户的个人资料"""
        return self.data._asdict()

    def __repr__(self):
        return f'Profile({self.data})'


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
        if LocalFileStorage.check_file(user_id, data_type):
            data = LocalFileStorage.read_data(user_id, data_type)
        else:
            raise FileNotFoundError(f'用户 {user_id} 的 {data_type} 数据文件不存在')
            # data = None
        return data


# class AutoUpdateFromMultipleWays(UpdateFromPhone, UpdateFromWatch, UpdateFromFile):
#     """支持多种方式自动更新的数据，统一管理获取数据的方法"""
#
#     def __init__(self, available_ways: list):
#         self._available_ways = available_ways
#
#     def auto_update(self):
#         for way in self._available_ways:
#             if way.isAvailable():
#                 # way.auto_update()
#                 return way.auto_update


class AutoUpdateFromMultipleWays:
    """支持多种方式自动更新的数据，统一管理获取数据的方法"""

    @staticmethod
    def auto_update(available_ways: list):
        """
        从多种方式中选择一种可用的方式来自动更新数据
        :param available_ways:
        :return:
        """
        for way in available_ways:
            if way.isAvailable():
                # way.auto_update()
                return way.auto_update


class ActivityData(BaseData, AutoUpdateFromMultipleWays):
    """
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
        self.data = None
        self._update_ways = [UpdateFromWatch, UpdateFromPhone, UpdateFromFile]
        # todo 添加对应的handler，用于随机读写数据文件

        self.load_data()

    def load_data(self):
        self.data = [self._activity_data(*x) for x in
                     self.auto_update(self._update_ways)(self._user_id, self._datatype)]

    def save_data(self):
        pass

    def get_data_by_date(self, date: dt_date):
        return [x for x in self.data if x.date == date]

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
        # super().__init__([UpdateFromWatch, UpdateFromPhone, UpdateFromFile])
        self._update_ways = [UpdateFromWatch, UpdateFromPhone, UpdateFromFile]

        self.load_data()

    def load_data(self):
        self.data = [self._step_count(*x) for x in self.auto_update(self._update_ways)(self.user_id, self._datatype)]

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
