# 作者: 大数据 浪哥
# 2025年07月15日23时45分53秒
# 1054074422@qq.com

# 1.判断类型
# Python中有多种方式来判断变量的类型。

# 1.1 使用type()函数
# type()函数可以返回一个变量的类型。

# 示例1：
a = 10
print(type(a))  # <class 'int'>

# 示例2：
b = "hello"
print(type(b))  # <class'str'>

c=None
print(type(c))  # <class 'NoneType'> NoneType 是 None 值的类型，表示“什么也没有”的一种数据类型
print(a is None)         # True
print(isinstance(a, type(None)))  # True
# 1.2 使用isinstance()函数
# isinstance()函数可以判断一个变量是否是某种类型或其子类。

# 示例1：
a = 10
print(isinstance(a, int))  # True

# 示例2：
b = "hello"
print(isinstance(b, str))  # True

#想了解某个方法干什么，可以配合 help() 使用
help(str.upper)
help(type)

