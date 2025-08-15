# 作者: 大数据 浪哥
# 2025年08月16日03时41分24秒
# 1054074422@qq.com


class A:
    """
    类在实例化时，会自动调用__init__方法，该方法可以接收参数，并将参数赋值给实例的属性。
    类在实例化时，会自动调用__new__方法，该方法可以返回一个实例对象。
    类函数可以接收一个参数，该参数可以是实例本身，也可以是实例的属性。
    类在实例化时，会自动把实例本身作为第一个参数（self）传入类函数。
    实例本身作为第一个参数传入类函数
    """

    def f(self, x):  # 类函数，接收一个参数，返回一个元组，包含类实例和参数值，self是类实例，x是参数值
        return self, x


a = A()
obj, val = a.f(10)  # 等价于 A.f(a, 10)
print(obj, val)
assert obj is a and val == 10

class Bad:
    def f():              # 忘了写 self，
        pass


b = Bad()   #实例方法需要一个形参来接收这个自动传入的实例
print(b.f())  #报错TypeError: Bad.f() takes 0 positional arguments but 1 was given