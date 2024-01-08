"""实现文件的随机读写，提供多种增删改查方式"""
import fileinput
import io
import os
import sys
import json
from abc import ABC, abstractmethod
from .data import ACTIVITY_DATA_TYPES, STATIC_DATA_TYPES
from .decorators import print_run_time

__all__ = ["user_file_handler_factory", "UserMultiFieldFileHandler", "UserSingleFieldFileHandler"]  # 对外提供的接口类名


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')


class JsonFileHandler:
    """json文件读写类"""

    @staticmethod
    def to_json(data) -> str:
        """将数据转换为json字符串"""
        return json.dumps(data)

    @staticmethod
    def from_json(data: str):
        """将json字符串转换为数据"""
        return json.loads(data)


class RandomFileHandler:
    """文件随机读写基类"""

    @staticmethod
    def get_lines(fp, line_numbers):
        """
        从文件指针读取多行数据，返回生成器
        https://pynative.com/python-read-specific-lines-from-a-file/
        :param fp:
        :param line_numbers:
        :return:
        """
        # return (x for i, x in enumerate(fp) if i in line_numbers)
        return (JsonFileHandler.from_json(x) for i, x in enumerate(fp) if i in line_numbers)

    @staticmethod
    def read_lines(filepath: str, line_numbers: list) -> list:
        """
        读取多行数据
        :param filepath:
        :param line_numbers: 行号列表
        :return:
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = RandomFileHandler.get_lines(file, line_numbers)
            data = [line for line in lines]
        return data

    @staticmethod
    def read_line(filepath: str, pos: int) -> [str, None]:
        """
        读取指定位置的一行数据
        :param filepath:
        :param pos:
        :return:
        """
        data = RandomFileHandler.read_lines(filepath, [pos])
        if len(data) == 0:
            return None
        else:
            return data[0]

    @staticmethod
    def append_line(data: str, filepath: str):
        """
        在文件末尾添加一行数据
        :param data:
        :param filepath:
        :return:
        """
        with open(filepath, 'a+', encoding='utf-8') as file:
            file.write(JsonFileHandler.to_json(data) + '\n')

    @staticmethod
    def insert_line(data: str, filepath: str, pos: int):
        """
        在指定位置插入一行数据
        :param data:
        :param filepath:
        :param pos:
        :return:
        """
        with fileinput.FileInput(filepath, inplace=True, backup='.bak') as file:
            for i, line in enumerate(file):
                if i == pos:
                    print(JsonFileHandler.to_json(data), end='')
                print(line, end='')

    @staticmethod
    def delete_line(filepath: str, pos: int):
        """
        删除指定位置的一行数据
        :param filepath:
        :param pos:
        :return:
        """
        with fileinput.FileInput(filepath, inplace=True, backup='.bak') as file:
            for i, line in enumerate(file):
                if i != pos:
                    print(line, end='')

    @staticmethod
    def modify_line(filepath: str, pos: int, data: str):
        """
        修改指定位置的一行数据
        :param filepath:
        :param pos:
        :param data:
        :return:
        """
        with fileinput.FileInput(filepath, inplace=True, backup='.bak') as file:
            for i, line in enumerate(file):
                if i != pos:
                    print(line, end='')
                else:
                    print(JsonFileHandler.to_json(data), end='\n')

    @staticmethod
    def search_line(filepath: str, data: str) -> int:
        """
        查找匹配数据的行号
        :param filepath:
        :param data:
        :return: 行号，未找到返回-1
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                if data in line:
                    return i
        return -1

    @staticmethod
    def check_file(filepath: str):
        """
        检查文件以及路径是否存在
        :param filepath:
        :return:
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as _:
                return True
        except FileNotFoundError:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as _:
                return False

    @staticmethod
    def get_file_length(filepath: str) -> int:
        """
        获取文件长度
        :param filepath:
        :return:
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            length = len(lines)
        return length

    @staticmethod
    def delete_file(filepath: str):
        """
        删除文件
        :param filepath:
        :return:
        """
        os.remove(filepath)


class MultiFieldDataFileHandlerInterface(ABC):
    """多字段数据文件读写接口类"""

    @staticmethod
    @abstractmethod
    def format_data(data) -> str:
        """将数据格式化为字符串"""
        pass

    @staticmethod
    @abstractmethod
    def parse_data(data: str) -> tuple:
        """将字符串解析为数据"""
        pass

    @staticmethod
    @abstractmethod
    def search_by_field(filepath: str, field: int, value) -> int:
        """
        根据字段查找匹配数据的行号
        :param filepath:
        :param field: 字段号，从0开始
        :param value: 字段值
        :return: 行号，未找到返回-1
        """
        pass


class MultiFieldDataFileHandler(RandomFileHandler, MultiFieldDataFileHandlerInterface):
    """多字段数据文件读写类"""

    @staticmethod
    def format_data(data) -> str:
        """将数据格式化为字符串"""
        data = [str(x) for x in data]
        d = ";".join(data)
        return d

    @staticmethod
    def parse_data(data: str) -> tuple:
        """将字符串解析为数据"""
        data = data.split(";")
        return tuple(data)

    @staticmethod
    def append_line(data: tuple, filepath: str):
        data = MultiFieldDataFileHandler.format_data(data)
        RandomFileHandler.append_line(data, filepath)

    @staticmethod
    def insert_line(data: tuple, filepath: str, pos: int):
        data = MultiFieldDataFileHandler.format_data(data)
        RandomFileHandler.insert_line(data, filepath, pos)

    @staticmethod
    def modify_line(filepath: str, pos: int, data: tuple):
        data = MultiFieldDataFileHandler.format_data(data)
        RandomFileHandler.modify_line(filepath, pos, data)

    @staticmethod
    def read_line(filepath: str, pos: int) -> [tuple, None]:
        if pos < 0:
            pos = RandomFileHandler.get_file_length(filepath) + pos
        data = RandomFileHandler.read_line(filepath, pos)
        if data is None:
            return None
        data = MultiFieldDataFileHandler.parse_data(data)
        return data

    @staticmethod
    def read_lines(filepath: str, line_numbers: list) -> list:
        data = RandomFileHandler.read_lines(filepath, line_numbers)
        data = [MultiFieldDataFileHandler.parse_data(line) for line in data]
        return data

    @staticmethod
    def search_by_field(filepath: str, field: int, value) -> int:
        """
        根据字段查找第一个匹配数据的行号
        :param filepath:
        :param field: 字段号，从0开始
        :param value: 字段值
        :return: 行号，未找到返回-1
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                data = MultiFieldDataFileHandler.parse_data(JsonFileHandler.from_json(line))
                if data[field] == value:
                    return i
        return -1

    @staticmethod
    def search_by_field_all(filepath: str, field: int, value) -> list:
        """
        根据字段查找所有匹配数据的行号
        :param filepath:
        :param field: 字段号，从0开始
        :param value: 字段值
        :return: 行号，未找到返回-1
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            line_numbers = []
            for i, line in enumerate(file):
                data = MultiFieldDataFileHandler.parse_data(JsonFileHandler.from_json(line))
                if data[field] == value:
                    line_numbers.append(i)
        return line_numbers

    @staticmethod
    def search_by_filed_range(filepath: str, field: int, value_range: tuple) -> list:
        """
        根据字段范围查找所有匹配数据的行号
        :param filepath:
        :param field: 字段号，从0开始
        :param value_range: 字段值范围
        :return: 行号，未找到返回-1
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            line_numbers = []
            for i, line in enumerate(file):
                data = MultiFieldDataFileHandler.parse_data(JsonFileHandler.from_json(line))
                if value_range[0] <= data[field] <= value_range[1]:
                    line_numbers.append(i)
        return line_numbers

class BaseUserFileHandler(ABC):
    """用户文件读写基类"""
    def __init__(self, user_id: str, data_type: str):
        self._user_id = user_id
        self._data_type = data_type
        self._filepath = f'local/{user_id}/{data_type}.txt'

        # self.check_file()


class UserSingleFieldFileHandler(BaseUserFileHandler, RandomFileHandler):
    """用户单字段数据文件读写类"""

    def __init__(self, user_id: str, data_type: str):
        super().__init__(user_id, data_type)
        # self._user_id = user_id
        # self._data_type = data_type
        # self._filepath = f'local/{user_id}/{data_type}.txt'
        #
        # # self.check_file()

    def check_file(self):
        return RandomFileHandler.check_file(self._filepath)

    def append_line(self, data: str):
        RandomFileHandler.append_line(data, self._filepath)

    def insert_line(self, data: str, pos: int):
        RandomFileHandler.insert_line(data, self._filepath, pos)

    def delete_line(self, pos: int):
        RandomFileHandler.delete_line(self._filepath, pos)

    def modify_line(self, pos: int, data: str):
        RandomFileHandler.modify_line(self._filepath, pos, data)

    def search_line(self, data: str) -> int:
        return RandomFileHandler.search_line(self._filepath, data)

    def read_line(self, pos: int) -> str:
        return RandomFileHandler.read_line(self._filepath, pos)

    def read_lines(self, line_numbers: list) -> list:
        return RandomFileHandler.read_lines(self._filepath, line_numbers)

    def get_file_length(self) -> int:
        return RandomFileHandler.get_file_length(self._filepath)

    def delete_file(self):
        RandomFileHandler.delete_file(self._filepath)


class UserMultiFieldFileHandler(BaseUserFileHandler, MultiFieldDataFileHandler):
    """用户多字段数据文件读写类"""

    def __init__(self, user_id: str, data_type: str):
        super().__init__(user_id, data_type)
        # self._user_id = user_id
        # self._data_type = data_type
        # self._filepath = f'local/{user_id}/{data_type}.txt'
        #
        # self.check_file()

    def check_file(self):
        return RandomFileHandler.check_file(self._filepath)

    def append_line(self, data: tuple):
        MultiFieldDataFileHandler.append_line(data, self._filepath)

    def insert_line(self, data: tuple, pos: int):
        MultiFieldDataFileHandler.insert_line(data, self._filepath, pos)

    def delete_line(self, pos: int):
        MultiFieldDataFileHandler.delete_line(self._filepath, pos)

    def modify_line(self, pos: int, data: tuple):
        MultiFieldDataFileHandler.modify_line(self._filepath, pos, data)

    def search_by_field(self, field: int, value) -> int:
        return MultiFieldDataFileHandler.search_by_field(self._filepath, field, value)

    @print_run_time
    def search_by_field_all(self, field: int, value) -> [list, None]:
        return MultiFieldDataFileHandler.search_by_field_all(self._filepath, field, value)

    def search_by_field_range(self, field: int, value_range: tuple) -> list:
        return MultiFieldDataFileHandler.search_by_filed_range(self._filepath, field, value_range)

    def read_line(self, pos: int) -> tuple:
        return MultiFieldDataFileHandler.read_line(self._filepath, pos)

    def read_lines(self, line_numbers: list) -> list:
        return MultiFieldDataFileHandler.read_lines(self._filepath, line_numbers)

    def get_file_length(self) -> int:
        return RandomFileHandler.get_file_length(self._filepath)

    def delete_file(self):
        RandomFileHandler.delete_file(self._filepath)


def user_file_handler_factory(user_id: str, data_type: str):
    """
    用户文件读写类工厂函数
    :param user_id:
    :param data_type: data.DATA_TYPES中的数据类型
    :return:
    """
    activity_data_types_values = [x.value for x in ACTIVITY_DATA_TYPES]
    static_data_types_values = [x.value for x in STATIC_DATA_TYPES]

    if data_type in activity_data_types_values:
        return UserMultiFieldFileHandler(user_id, data_type)
    elif data_type in static_data_types_values:
        return UserSingleFieldFileHandler(user_id, data_type)
    else:
        raise ValueError(f"Invalid data type: {data_type}")


# class DataFileHandler:
#     """数据文件读写类"""
#
#
#     @staticmethod
#     def __change_the_form_of_data(data: list):
#         data = [str(x) for x in data]
#         d = ";".join(data)
#         return d
#
#     @staticmethod
#     def write_line(data: list, filepath: str):
#         """
#         传入一条信息，以列表的形式传入
#         这个函数的作用就相当于append
#         """
#         data = DataFileHandler.__change_the_form_of_data(data)
#         with open(filepath, 'a+') as file:
#             file.write(data)
#
#     @staticmethod
#     def read_line(filepath: str, pos: int):
#         with open(filepath, 'r+') as file:
#             file.seek(0)
#             for _ in range(pos):
#                 file.readline()
#             data = file.readline()
#             data = data.split(";")
#         return data
#
#     @staticmethod
#     def delete_line(filepath: str, pos: int):
#         with fileinput.FileInput(filepath, inplace=True, backup='.bak') as file:
#             for i, line in enumerate(file):
#                 if i != pos:
#                     print(line, end='')
#
#     @staticmethod
#     def modify_line(filepath: str, pos: int, data: list):
#         """
#         只是在某一行更改一条信息
#         """
#         data = DataFileHandler.__change_the_form_of_data(data)
#         with fileinput.FileInput(filepath, inplace=True, backup='.bak') as file:
#             for i, line in enumerate(file):
#                 if i != pos:
#                     print(line, end='')
#                 if i == pos:
#                     print(data)
#
#     @staticmethod
#     def find_pos(filepath:str, inf):
#         """
#         找到关于某个信息的位置
#         """
#         inf = str(inf)
#         i = 1
#         while i:
#             data = DataFileHandler.read_line(filepath, i-1)
#             if inf not in data:
#                 i += 1
#             elif not data:# 判断是否已经到达文件末尾
#                 print("No such information")
#                 return -1
#             else:
#                 return i-1



#
# class UserFileHandler(DataFileHandler):
#     @staticmethod
#     def write_data(user_id: str, filename: str, data: str):
#         filepath = f'local/{user_id}/{filename}.txt'
#         DataFileHandler.write_line(data, filepath)
#
#     @staticmethod
#     def read_data(user_id: str, filename: str, inf):
#         filepath = f'local/{user_id}/{filename}.txt'
#         pos = DataFileHandler.find_pos(filepath, inf)
#         return DataFileHandler.read_line(filepath, pos)
#
#     @staticmethod
#     def check_file(user_id: str, filename: str):
#         filepath = f'local/{user_id}/{filename}.txt'
#         try:
#             with open(filepath, 'r') as _:
#                 return True
#         except FileNotFoundError:
#             os.makedirs(os.path.dirname(filepath), exist_ok=True)
#             return False
#
#     @staticmethod
#     def modify_data(user_id: str, filename: str, inf, data: list):
#         filepath = f'local/{user_id}/{filename}.txt'
#         pos = DataFileHandler.find_pos(filepath, inf)
#         return DataFileHandler.modify_line(filepath, pos, data)
