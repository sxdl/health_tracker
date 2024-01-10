"""User class"""

from abc import ABC, abstractmethod
from collections import namedtuple, defaultdict
from . data import *

__all__ = ["User"]


DEFAULT_HEALTH_DATA_TYPES = {  # 弃用
    'step_count': StepCount,
    'distance': Distance,
    'flights_climbed': FlightsClimbed,
    'active_energy_burned': ActiveEnergyBurned
}

age_groups = {  # 谨慎使用，可能实际用不到这个年龄分组
    'children': (0, 12),
    'teenagers': (13, 18),
    'youth': (19, 40),
    'middle_aged': (41, 60),
    'old': (61, 100)
}


class HealthData:
    """
    warning: 已弃用，使用data.ActivityDataStatistics替代
    """
    def __init__(self, user_id, health_data_types: dict):
        self._user_id = user_id
        self._health_data_types = health_data_types


class User:
    """
    用户的接口类，与用户数据的所有交互通过调用这个类的方法来实现。
    尽量直接使用User中的方法，而不是简介操作成员对象。
    如果本类中没有提供相关的功能函数，在这个类里新增功能函数，然后在别处调用。
    """

    def __init__(self, user_id: str, name: str, birth=None, height=None, weight=None):
        self.user_id = user_id
        self.name = name
        self.birth = birth
        self.height = height
        self.weight = weight
        self.profile = Profile(user_id)
        self.activity_data = ActivityDataStatistics(user_id)
        # self.health_data = HealthData(user_id, DEFAULT_HEALTH_DATA_TYPES)  # 这个对象应该是用不到，用activity_data
        self.age_group = None  # 可能用不到这个

    def load_profile(self):
        """Load profile"""
        pass

    def get_profile(self) -> namedtuple:
        """获取用户的个人资料:gender, birth, height, weight"""
        return self.profile.get_namedtuple_data()

    def get_birth(self):
        """获取用户的出生日期"""
        return self.birth

    def set_birth(self, birth):
        """设置用户的出生日期"""
        self.birth = birth

    def get_height(self):
        """获取用户的身高"""
        return self.height

    def set_height(self, height):
        """设置用户的身高"""
        self.height = height

    def get_weight(self):
        """获取用户的体重"""
        return self.weight

    def set_weight(self, weight):
        """设置用户的体重"""
        self.weight = weight

    def get_profile(self) -> namedtuple:
        """获取用户的个人资料:gender, birth, height, weight"""
        return self.profile.get_namedtuple_data()

    def add_2_group(self, group_id: str):
        """加入群组"""
        self.groups.add_2_group(group_id)

    def is_in_group(self, group_id: str):
        """检查是否在群组中"""
        return group_id in self.groups
