# 作者: 大数据 浪哥
# 2025年07月12日16时42分59秒
# 1054074422@qq.com


class Person:
    """人类"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s 体重 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        """跑步"""
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        """吃东西"""
        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1


if __name__ == '__main__':
    xiaoming = Person("大象", 75)
    xiaoming.run()
    xiaoming.eat()
    print(xiaoming)
    print("-" * 50)
    lazy = Person("懒狗", 50)
    lazy.run()
    lazy.eat()
    print(lazy)
