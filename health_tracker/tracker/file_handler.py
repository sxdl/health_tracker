"""实现文件的随机读写，提供多种增删改查方式"""
from abc import ABC, abstractmethod  # 可以看情况使用基类继承ABC和使用abstractmethod修饰符

__all__ = []  # 对外提供的接口类名


class RandomFileHandler:
    """文件随机读写基类"""
    pass  # todo 设计 RandomFileHandler 类，实现文件的随机读写。注意需要满足*多态*的要求


class DataFileHandler(RandomFileHandler):
    """数据文件读写类"""
    pass  # todo 设计 DataFileHandler 类，实现数据文件的随机读写。
