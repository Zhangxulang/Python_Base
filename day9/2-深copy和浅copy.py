# 作者: 大数据 浪哥
# 2025年07月15日23时46分27秒
# 1054074422@qq.com
import copy

# 深copy和浅copy的区别
# 深copy: 复制整个对象及其包含的所有子对象，包括列表、字典、集合等。
# 浅copy: 只复制对象本身，不包含其包含的子对象。

# 例子1：浅copy
# 列表的浅copy
def use_list_shallow_copy():
    """
    列表的浅copy,创建了一个新的列表对象 b；
    把 a 中的每个元素的引用（不是值）复制一份放入 b 中
    单内层列表是同一个列表对象
    :return:
    """
    a = [1, 2, [3, 4]]
    b = a.copy()
    a[2].append(5)
    print(a)  # [1, 2, [3, 4, 5]]
    print(b)  # [1, 2, [3, 4,5]]
    print(id(a), id(b))   # 两个对象地址不同、a 和 b 是不同的对象
# 例子2：深copy

def use_list_deep_copy():
    """
    列表的深copy,创建了一个新的列表对象 b；
    把 a 中的每个元素的引用（不是值）复制一份放入 b 中
    单内层列表是新的列表对象
    :return:
    """
    a = [1, 2, [3, 4]]
    b = copy.deepcopy(a)
    a[2].append(5)
    print(a)  # [1, 2, [3, 4, 5]]
    print(b)  # [1, 2, [3, 4]]
    print(id(a), id(b))   # 两个对象地址不同、a 和 b 是不同的对象

# 例子3：深copy
# 集合的深copy
def use_set_copy():
    """
    在 Python 中，set 是“可变的”，不能作为另一个 set 的元素，因为：
    set 的元素必须是 可哈希（hashable） 的；
    而 set 本身是 不可哈希的（unhashable）；"""
    # a = {1, 2, {3, 4}}
    # b = copy.deepcopy(a)
    # a.add(5)
    # print(a)  # {1, 2, {3, 4}, 5}
    # print(b)  # {1, 2, {3, 4}}

# 例子4：使用copy包中的copy
def use_copy_shallow():
    """
    使用copy包中的copy，浅copy
    :return:
    """
    c = [1, 2, 3]
    d = copy.copy(c)
    d[0] = 10
    print(id(c))
    print(id(d))
    print(c)
    print(d)

# 例子4：使用copy包中的copy
def use_copy_shallow2():
    """
    copy是浅copy，只做第一层copy
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c--{c}')
    print(f'd--{d}')
    print('-' * 50)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))

# 例子5：使用copy包中的deepcopy
def use_deepcopy():
    """
    递归去copy，不管有多少层，都会新做一个空间，把数据拿进来
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c--{c}')
    print(f'd--{d}')
    print('-' * 50)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))

class Hero:
    def __init__(self, name, blood):
        self.name = name  #不可变数据类型
        self.blood = blood  #不可变数据类型
        self.equipment = ['鞋子', '指环']  #可变数据类型


def use_copy_own_obj():
    """
    实际对于自定义对象的练习
    :return:
    """
    old_hero = Hero('蚂蚁', 90)
    new_hero = copy.deepcopy(old_hero)
    new_hero.blood = 80  #新对象修改后，原对象不会受到任何影响
    new_hero.equipment.append('药水')
    print(old_hero.blood)
    print(old_hero.equipment)


if __name__ == '__main__':
     use_list_shallow_copy()
    # use_list_deep_copy()
    # use_set_copy()
    # use_copy_shallow()
    # use_copy_shallow2()
    # use_deepcopy()
    #use_copy_own_obj()



# 总结：深copy和浅copy的区别在于是否复制对象包含的子对象。
# 深copy会复制整个对象及其包含的所有子对象，包括列表、字典、集合等。
# 浅copy只复制对象本身，不包含其包含的子对象。
# 建议使用深copy，以确保数据的完整性和一致性。

# 浅拷贝：外层分开，内层共用；
# 深拷贝：彻底分家，互不影响
