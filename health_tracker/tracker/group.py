"""这个类包括了群组的相关内容"""

import time
import qrcode
from .file_handler import GroupFileHandler
import os


__all__ = ["Group"]


class Group:
    def __init__(self, group_id: str, owner_id: str = None, group_name: str = None, file_path=None):
        self.group_id = group_id            # 群组id
        self.name = group_name              # 群名称
        self.members = [owner_id]           # 成员列表
        self.announcement = ""              # 发布的通知,是一个对象
        self.activities = []                # 发布的活动
        self.owner = owner_id               # 群主
        self.QR_cord = qrcode.QRCode(       # 二维码
            version=1,  # 控制二维码的大小，范围为1到40
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # 控制纠错水平，L表示低纠错水平
            box_size=10,  # 控制每个单元格的像素数
            border=4,  # 控制边框的像素数
        )  # 这个变量是用来存储二维码的
        
        # self.administrator = [self.owner]   # 管理员名单
        if file_path is not None:
            self.handler = GroupFileHandler(group_id)

        self.qr_path = f"health_tracker/health_app_pyqt/resource/images/icon/tempqrcode.png"
        # self.save_qr_cord()
        self.generate_qr_cord()

    @staticmethod
    def create_group(owner_id: str, group_name: str):
        group_id = str(time.time_ns())
        group = Group(group_id, owner_id, group_name)
        return group

    def generate_qr_cord(self):
        self.QR_cord.add_data(self.group_id)
        self.QR_cord.make(fit=True)
        # 创建一个PIL图像对象
        img = self.QR_cord.make_image(fill_color="black", back_color="white")
        return img

    def save_qr_cord(self):
        self.QR_cord.make(fit=True)
        img = self.QR_cord.make_image(fill_color="black", back_color="white")
        img.save(self.qr_path)
        return self.qr_path
    
    def check_members(self, uid: str):
        if uid in self.members:
            return True
        else:
            return False
    
    def add_members(self, uid: str):
        self.members.append(uid)
        # 我的想法是，返回的group_id直接传递给uid下的用户，用用户的函数添加这个group_id
        return self.group_id

    def delete_members(self, uid: str):
        if self.check_members(uid):
            self.members.remove(uid)
            return True
        else:
            return False
        
    def leave_group(self, uid: str):
        # 这里要补充UI来写，询问用户是否退出的弹窗，有确认或取消
        # ...
        if uid == self.owner:
            del self
        else:
            self.delete_members(uid)
        # 踢出群聊删除活动中的这个人
        for i in self.activities:
            i.leave_activity(uid)
            
    def add_announcement(self, uid, inf: str):
        """
        发布通知
        """
        message = Announcement(inf, uid)
        self.announcement = message
        return True

    def delete_announcement(self):
        self.announcement = ""
        return True

    def add_activity(self):
        # TODO: 这个活动我还不是很会搞
        pass

    def statistic(self):
        statis = {
            "gender": {
                "man": 0,
                "women": 0},
            "age": {
            }
        }
        for i in self.members:
            # TODO: 由于不熟悉user类到底是什么结构，所以这个for要补充
            pass
        return statis


class Activities:
    """
    这个类是设置活动的我也不知道具体要哪些活动
    """
    def __init__(self, uid: str):
        self.members = [uid]
        self.num = 1            # 参加的人员总数
        self.name = ""          # 活动的名称
        # 可能还有关于内容的成员

    def join_activity(self, uid: str):
        self.members.append(uid)
        self.name += 1

    def leave_activity(self, uid: str):
        self.members.remove(uid)
        self.name -= 1
        self.delete_activity()

    def delete_activity(self):
        if self.num == 0:
            del self

    def check_member(self, uid):
        if uid in self.members:
            return True
        else:
            return False

    def statistic(self):
        statis = {
            "gender": {
                "man": 0,
                "women": 0
            },
            "age": {}
        }
        for i in self.members:
            # 由于不熟悉user类到底是什么结构，所以这个for要补充，做一个统计
            pass
        return statis


class Announcement:
    def __init__(self, inf: str, uid: str):
        self.inf = inf
        self.time = time.time()
        self.publisher = uid

    def edit_inf(self, new_inf: str, uid: str):
        self.inf = new_inf
        self.time = time.time()
        self.publisher = uid
