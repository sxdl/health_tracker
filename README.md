# 健康追踪系统

## 项目结构

```plaintext
- health_tracker
  - health_app_tikinter             应用前端包
  - health_app_pyQt                 应用前端包
  - tracker                         应用后端包
  - local                           用户本地数据，子文件夹为用户id，默认不上传，程序会自动生成
  main.py                           主程序入口
  requirements.txt                  依赖包列表
  README.md                         项目说明
```

## 模块介绍
### main.py

主程序入口，用于启动应用，提供命令行参数解析功能。输入`main.py -h`查看帮助。

常用命令：

```bash
# 启动应用
python mian,py run -h           # 查看帮助
python main.py run tkinter      # 使用tkinter框架启动
python main.py run pyQt         # 使用pyQt启动

# 生成用户数据
python main.py stimulator -h    # 查看帮助
python main.py stimulator -a 0  # 生成用户id为0的所有用户数据
python main.py stimulator -s 0  # 生成用户id为0的步数数据
python main.py stimulator -a    # 默认用户id为0
```

### tracker

这个包里面是应用的后端，包含了应用的所有逻辑。下面目前有这几个文件：

- `__init__.py`：包的初始化文件，用于导入包内的模块
- `user.py`：用户类，前端和后端的交互都是通过用户类来进行的
- `data.py`：数据类，用于存储用户的数据
- `util.py`：工具类，用于存储一些工具函数，包括数据生成函数、数据读取函数、数据写入函数等

### health_app_tkinter

这个包里面是应用的前端，仅供调试使用，正式上线使用pyQt重写，使用tkinter框架实现。

### health_app_pyQt

这个包里面是应用的前端，使用pyQt框架实现。

### local

这个文件夹用于存储用户的本地数据，每个用户的数据都会存储在一个单独的文件夹中，文件夹的名字为用户的id。

## TODO

### 新增随机文件读取功能

先设计一个基类，用于随机文件的基本读写，然后再设计几个继承自基类的子类，子类中实现对不同数据类型的文件读取功能。可以看情况调整类的结构。

至少提供如下功能，使得其他模块可以通过这个类来读取随机文件：

- 读取文件中的指定行
- 查找文件中的匹配行
- 对指定行的数据进行修改
- 对文件中的数据进行追加
- 对文件中的数据进行删除

### 完善pyQt前端

使用pyQt框架重写前端，实现app的所有功能。界面设计复刻手机上的健康app。

### 提供用户每日手动输入数据的功能

因为实际使用中，用户的数据不可能都是通过手环或者其他设备自动采集的，所以需要提供一个手动输入数据的功能，用户可以在app中手动输入数据，然后保存到本地。

就是在app中提供一个手动输入数据的界面，用户可以在这个界面中输入各种数据，然后保存到本地。

先随便使用一个框架快速实现功能，然后再使用pyQt框架完善美化。

注意，不同的用户因为数据类型不同，所以需要提供不同的手动输入界面。
