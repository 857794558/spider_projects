from 学生 import *


class ManagerSystem(object):
    def __init__(self):
        self.students_list = []

    def run(self):
        # 加载学员信息
        self.load()
        while True:
            # 加载界面
            self.show_info()
            # 选择功能
            num = int(input('请选择您想要的功能:'))
            if num == 1:
                print('1.添加学员信息')
                self.add_students()
            elif num == 2:
                print('2.删除学员信息')
                self.del_students()
            elif num == 3:
                print('3.修改学员信息')
                self.modify_students()
            elif num == 4:
                print('4.查询学员信息')
                self.search_students()
            elif num == 5:
                print('5.显示所有学员信息')
                self.show_list()
            elif num == 6:
                print('6.保存学员信息')
                self.reserve_list()
            elif num == 7:
                print('7.退出系统')
                break
            else:
                print('你的输入有误，请重新输入')

    def show_info(self):
        print('1.添加学员信息')
        print('2.删除学员信息')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        # 打开文件
        # 转化为字典
        # 储存到'信息表'
        print('7.退出系统')

        # 怎么添加信息的？
    def add_students(self):
        name = input('请输入您的姓名')
        gender = input('请输入您的性别')
        tel = input('请输入您的联系方式')
        students = Students(name, gender, tel)
        self.students_list.append(students)
        # print(self.students_list)

    def del_students(self):
        name = input('请输入您的姓名')
        for i in self.students_list:
            if i.name == name:
                self.students_list.remove(i)
                print(self.students_list)
        else:
            print('该学员不存在')

    def modify_students(self):
        name = input('请输入原姓名:')
        for i in self.students_list:
            if i.name == name:
                i.name = input('请输入新姓名:')
                i.gender = input('请输入你的性别:')
                i.tel = input('请输入您的联系方式:')
                print(f'修改后的姓名是{i.name},性别是{i.gender},联系方式是{i.tel}')
                print(self.students_list)

        else:
            print('该学员不存在')

    def search_students(self):
        name = input('请输入原姓名:')
        for i in self.students_list:
            if i.name == name:
                print(i)
        else:
            print('该学员不存在')

    def show_list(self):
        answer = input('are you sure to search all list?')
        if answer == 'sure':
            print('姓名\t性别\t联系电话')
            for i in self.students_list:
                print(f'{i.name}\t{i.gender}\t{i.tel}')
        else:
            print('该学员不存在')

    def reserve_list(self):
        f = open('信息表','w')
        new_list = [i.__dict__ for i in self.students_list]
        f.write(str(new_list))
        f.close()

    def load(self):
        try:
            f = open('信息表', 'r')
        except:
            f = open('信息表', 'w')
        else:
            data = f.read()
            new_list = eval(data)
            self.students_list = [Students(i['name'],i['gender'],i['tel']) for i in new_list]
        finally:
            f.close()

