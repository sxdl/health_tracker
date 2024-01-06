"""装饰器函数"""
import time


def print_run_time(func):
    """打印函数运行时间的装饰器"""
    def wrapper(*args, **kwargs):
        local_time = time.time()
        result = func(*args, **kwargs)
        print(f'函数 {func.__name__} 运行时间为：{time.time() - local_time} 秒', file=open('log.txt', 'a'))
        return result

    return wrapper
