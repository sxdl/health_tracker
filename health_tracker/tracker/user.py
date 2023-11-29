"""User class"""

from abc import ABC, abstractmethod
from collections import namedtuple, defaultdict
from . data import *

__all__ = ["User"]


DEFAULT_HEALTH_DATA_TYPES = {
    'step_count': StepCount,
    'distance': Distance,
    'flights_climbed': FlightsClimbed,
    'active_energy_burned': ActiveEnergyBurned
}

age_groups = {
    'children': (0, 12),
    'teenagers': (13, 18),
    'youth': (19, 40),
    'middle_aged': (41, 60),
    'old': (61, 100)
}



class HealthData:
    def __init__(self, user_id, health_data_types: dict):
        self._user_id = user_id
        self._health_data_types = health_data_types


class User:
    """User class"""

    def __init__(self, user_id: str, name: str):
        """Constructor"""

        self.user_id = user_id
        self.name = name
        self.profile = Profile(user_id)
        self.activity_data = ActivityDataStatistics(user_id)
        self.health_data = HealthData(user_id, DEFAULT_HEALTH_DATA_TYPES)
        self.age_group = None

    def load_profile(self):
        """Load profile"""
        pass


