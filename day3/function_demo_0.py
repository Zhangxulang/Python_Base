# 作者: 大数据 浪哥
# 2025年06月12日22时51分57秒
# 1054074422@qq.com
# 函数的定义和调用

# 定义函数
def my_function(x):
    return x * x


# 调用函数
print(my_function(3))  # 输出9


# 函数可以接收多个参数，并返回多个值
def my_function(x, y):
    return x + y, x - y


print(my_function(3, 4))  # 输出(7, -1)


# 函数可以有默认参数
def my_function(x, y=2):
    return x + y


print(my_function(3))  # 输出5
print(my_function(3, 4))  # 输出7


# 函数可以有可变参数
def my_function(*args):
    return sum(args)


print(my_function(1, 2, 3, 4, 5))  # 输出15


# 函数可以有关键字参数
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        my_function(name='大数据', age=25, gender='男')  # 输出name 大数据 age 25 gender 男
        my_function()
        my_function()  # 输出name None age None gender None
