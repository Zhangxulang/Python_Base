# 作者: 大数据 浪哥
# 2025年06月12日02时12分08秒
# 1054074422@qq.com
# 代码说明：字典的基本操作

# 1.创建字典
# 语法：{key1:value1, key2:value2, key3:value3}
# 示例：
my_dict = {'apple': 2, 'banana': 3, 'orange': 4}
print(my_dict)

# 2.访问字典元素
# 语法：my_dict[key]
# 示例：
print(my_dict['apple'])  # 输出2

# 3.修改字典元素
# 语法：my_dict[key] = value
# 示例：
my_dict['apple'] = 5
print(my_dict)  # 输出{'apple': 5, 'banana': 3, 'orange': 4}

# 4.添加字典元素
# 语法：my_dict[key] = value
# 示例：
my_dict['grape'] = 6
print(my_dict)  # 输出{'apple': 5, 'banana': 3, 'orange': 4, 'grape': 6}

# 5.删除字典元素
# 语法：del my_dict[key]
# 示例：
del my_dict['banana']
print(my_dict)  # 输出{'apple': 5, 'orange': 4, 'grape': 6}

# 6.判断字典是否为空
# 语法：bool(my_dict)
# 示例：
my_dict = {}
print(bool(my_dict))  # 输出False
#为什么输出False呢？因为空字典是False，非空字典是True。详细介绍请看下面的内容。

# 7.判断字典是否包含某个键
# 语法：key in my_dict
# 示例：
print('grape' in my_dict)  # 输出False

# 9.获取字典长度
# 语法：len(my_dict)
# 示例：
print(len(my_dict))  # 输出0