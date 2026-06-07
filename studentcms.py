import ast
from pathlib import Path

from stdent import Student


class StudentCms:
    # 2. 通过魔法方法init, 初始化属性信息.
    # 创建一个空列表, 用于存储学生信息.
    def __init__(self):
        self.stu_list = []

    # 3. 定义函数, 实现打印 管理系统的界面.
    def show_view(self) -> None:
        print('*' * 23)
        print('学生管理系统V2.0版')
        print('\t1.添加学生信息')
        print('\t2.删除学生信息')
        print('\t3.修改学生信息')
        print('\t4.查询单个学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存学生信息')
        print('\t0.退出系统')
        print('*' * 23)

    # 定义函数，添加学生信息
    def add_stu(self):
        name = input('请输入学生姓名:')
        gender = input('请输入学生性别:')
        age = int(input('请输入学生年龄:'))
        phone = input('请输入学生电话:')
        desc = input('请输入学生描述信息:')
        stu = Student(name, gender, age, phone, desc)
        self.stu_list.append(stu)
        print(f'学生{name}信息添加完成')

    def del_stu(self):
        del_name = input('请输入要删除的学生姓名:')
        for stu in self.stu_list:
            if del_name == stu.name:
                self.stu_list.remove(stu)
                print(f'学员 {del_name} 信息删除成功!\n')
                return
        print('查无此人, 请检查后重新删除!\n')

    def update_stu(self):
        update_name = input('请输入要修改的学生姓名:')
        for stu in self.stu_list:
            if update_name == stu.name:
                stu.gender = input('请录入修改后的性别: ')
                stu.age = int(input('请录入修改后的年龄: '))
                stu.phone = input('请录入修改后的电话: ')
                stu.desc = input('请录入修改后的描述信息: ')
                print(f'学员 {update_name} 信息修改成功!\n')
                break
        else:
            print('查无此人, 请检查后更新!\n')

    def search_one_stu(self):
        search_name = input('请输入要查找的学生姓名:')
        for stu in self.stu_list:
            # 7.3 如果当前学生的姓名 和 要查找的学生相同, 就打印该学生信息
            if stu.name == search_name:
                print(stu, end='\n\n')
                break
        else:
            print('查无此人, 请检查后重新操作!\n')

    def search_all_stu(self):
        if len(self.stu_list) == 0:
            print('暂无学生信息, 请添加后查询!')
        for stu in self.stu_list:
            print(stu)

    def save_stu(self):
        path = Path('./data/stu.txt')
        path.parent.mkdir(parents=True, exist_ok=True)
        with open('./data/stu.txt', 'w', encoding='utf-8') as stu:
            # for stud in self.stu_list:
            #     stu.write(str(stud.__dict__) + '\n')
            #保存的时候，对象列表-》字典列表，然后直接把字典列表转化成字符串，写入成一行
            stu_list=[stu.__dict__ for stu in self.stu_list]
            stu.write(str(stu_list))

    def load_stu(self):
        try:
            with open('./data/stu.txt', 'r', encoding='utf-8') as stu:
                stu_r = stu.read()
                #加载的时候，文件是一行表面量的字典列表，通过ast.literal_eval()直接转换成字典列表
                stu_list = ast.literal_eval(stu_r)
                #字典解包实例化传入self.stu_list
                self.stu_list = [Student(**stu) for stu in stu_list]
        except:
            path = Path('./data/stu.txt')
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8'):
                pass


    def start(self):
        while True:
            self.show_view()
            numb = input('请输入您要操作的编号:')
            match numb:
                case '1':
                    self.add_stu()
                case '2':
                    self.del_stu()
                case '3':
                    self.update_stu()
                case '4':
                    self.search_one_stu()
                case '5':
                    self.search_all_stu()
                case '6':
                    self.save_stu()
                case '0':
                    result = input('您确定要退出吗? (Y/N) -> ')
                    if result.lower() == 'y':
                        break
                case _:
                    print('录入有误, 请重新录入!\n')


if __name__ == '__main__':
    c = StudentCms()
    c.start()
