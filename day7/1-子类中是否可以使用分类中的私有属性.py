# 作者: 大数据 浪哥
# 2025年07月14日16时15分16秒
# 1054074422@qq.com

class Parent:
    __private_attr = "This is a private attribute"

    def __init__(self):
        self.public_attr = "This is a public attribute"

    def get_private_attr(self):
        return self.__pri       # 这里的__pri是私有属性，不能直接访问，需要通过get_private_attr
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attr = "This is a child attribute"

    def get_private_attr(self):
        return self.__private_attr  # 这里的__private_attr是父类中的私有属性，可以直接访问

p = Parent()
print(p.public_attr)
print(p.get_private_attr())  # 这里会报错，因为p是Parent类的实例，不能访问私有属性

c = Child()
print(c.public_attr)
print(c.child_attr)
print(c.get_private_attr())  # 这里可以正常访问私有属性