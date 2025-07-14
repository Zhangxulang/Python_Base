# 作者: 大数据 浪哥
# 2025年07月13日18时15分45秒
# 1054074422@qq.com


class Women:
    """
    私有属性和私有方法只能在类的内部访问
    """

    def __init__(self, name):
        self.name = name
        # 不要问女生的年龄
        self.__age = 18  # __表示私有属性

    def __secret(self):  # __表示私有方法
        print(f'我叫{self.name}, 我的年龄是{self.__age}')

    def boy_friend(self):
        self.__secret()  # 调用私有方法


xiaofang = Women("小芳")
# 私有属性，外部不能直接访问
# print(xiaofang.age)
# 私有方法，外部不能直接调用
# xiaofang.secret()
xiaofang.boy_friend()
#print(xiaofang._Women__age)  不要使用这种方式，访问对象的 私有属性 或 私有方法
#xiaofang._Women__secret()     不要使用这种方式，访问对象的 私有属性 或 私有方法