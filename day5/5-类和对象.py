# 作者: 大数据 浪哥
# 2025年07月12日13时49分09秒
# 1054074422@qq.com

# 类和对象
# 类是创建对象的蓝图，它定义了对象的属性和方法。对象是类的实例，它是类的具体实现。
# 类定义语法：
# class 类名:
#     类变量
#     def 方法名(self, 参数列表):
#         函数体
# 实例化对象语法：
# 对象名 = 类名()   # 实例化对象
# 类变量：
# 类变量是属于整个类所有对象的变量，它可以被所有实例共享。
# # 方法：
# 方法是属于类的函数，它可以访问类的变量和其他方法。

# # 类和对象之间的关系：
#     1. 类是创建对象的蓝图，它定义了对象的属性和方法。
#     2. 对象是类的实例，它是类的具体实现。
#     3. 类变量是属于整个类所有对象的变量，它可以被所有实例共享。
#     4. 方法是属于类的函数，它可以访问类的变量和其他方法。
#     5. self参数是类的实例变量，它代表了当前对象的实例。

#类的作用是把属性和方法封装在一起，使得每一个方法只能访问属于自己的属性，从而实现了数据隐藏和信息隐藏。
class Person:
    def __init__(self, name, age,height):
        self.name = name
        self.age = age
        self.height = height

    def say_hello(self):
        print("Hello, my name is %s, I am %d years old,my height is %d cm." % (self.name, self.age,self.height))


#实例化一个Person对象：
p = Person("Alice", 25,185)
# 调用say_hello方法：
p.say_hello()
print(dir(Person))    #输出Person类的所有属性和方法,包括继承自基类object的属性和方法
print(dir(p))         #输出p对象的所有属性和方法

