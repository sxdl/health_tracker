"""这个模块里存放所有的静态常量和枚举类"""
from enum import Enum


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