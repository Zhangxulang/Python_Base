# 作者: 大数据 浪哥
# 2025年07月14日01时56分21秒
# 1054074422@qq.com

#多态：同一条指令，不同的对象，产生的行为不同。
#多态的好处：
#1. 代码的复用性提高，相同的操作只需要定义一次，就可以在不同的类中使用。
#2. 增加了程序的灵活性，当需求改变时，只需要修改具体的类即可。
#3. 降低了代码的耦合度，提高了代码的可维护性。

# 以下是代码实现：
class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name


    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
        # 让狗玩耍
        dog.game()  #多态调用


# 1. 创建一个狗对象
# waining = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")
# 2. 创建一个大象对象
xiaoming = Person("大象")
# 3. 让大象调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
