"""
该文件用于记录 学生类, 学生的属性信息为: 姓名, 性别, 年龄, 手机号, 描述信息.
"""


class Student:
    # 定义初始化学生信息
    def __init__(self, name, age, gender, phone, desc):
        """
        魔法方法初始化属性信息
        :param name:姓名
        :param age:年龄
        :param gender:性别
        :param phone:电话
        :param desc:描述
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.desc = desc

    def __str__(self):
        return f'姓名:{self.name}，年龄:{self.age}，性别:{self.gender}，电话:{self.phone}，描述:{self.desc}'


if __name__ == '__main__':
    s = Student('乔峰', '男', 38, '13112345678', '丐帮帮主')
    print(s)
