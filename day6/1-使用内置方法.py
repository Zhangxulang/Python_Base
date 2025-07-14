# 作者: 大数据 浪哥
# 2025年07月12日16时42分48秒
# 1054074422@qq.com

class Cat:
    def __init__(self, new_name):
        """
        对象初始化时，默认调用的函数
        :param new_name:
        """
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name

    def __del__(self):
        """
        对象被销毁时，默认调用的函数
        :return:
        """
        print(f'{self.name}对象被销毁了')

    def __str__(self):
        """
        打印对象时，默认调用的函数
        :return:
        """
        return f"这是一个{self.name}的实例"

    def eat(self):
        print("%s 爱吃鱼" % self.name)
        # 使用类名()创建对象的时候，会自动调用初始化方法 __init__


tom = Cat("Tom")
print(tom.name)
lazy_cat = Cat("大懒猫")
print(tom is lazy_cat)  # 对象是可变数据类型，所以可以用 is 来判断两个对象是否相同
lazy_cat.eat()
print(lazy_cat)
print('-' * 50)
del lazy_cat
print('程序结束')  # 为什么程序结束后，tom对象会被销毁
#当程序完全结束，所有的对象引用都被释放后，tom对象才会被Python的垃圾回收机制销毁
