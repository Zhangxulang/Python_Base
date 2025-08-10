# 作者: 大数据 浪哥
# 2025年07月11日17时15分37秒
# 1054074422@qq.com

# 集合（set）是由一组无序且唯一的元素组成的集合。
# 使用场景是去重
#用哈希实现
# 集合的元素可以是任何类型，包括数字、字符串、元组、列表等。
def use_set():
    """
    使用集合
    :return:
    """
    set1 = {1, 2, 3, 4, 5}      #和字典一样，{}表示空字典，set()表示空集合；和字典区别是没有冒号
    print(type(set1))
    print(len(set1))
    set2={}                     #定义一个空字典
    print(type(set2))
    print(len(set2))
    set3 = set()                #定义一个空集合
    print(type(set3))
    print(len(set3))
    #print（set[1]）是错误的，因为集合没有索引（无序的） 不支持随机访问


def use_set_operation():
    """
    集合的操作
    :return:
    """
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # 1.求并集
    set3=set1.union(set2)
    print(set3)
    set4=set2.union(set1)    #求并集
    print(set4)
    print(set1.union(set2))     #求并集不改变原集合
    print('-'*50)

    # 2.求交集
    print(set1.intersection(set2))
    print(set1&set2)
    print(set1.isdisjoint(set2))  # 判断set1和set2是否有交集 如果没有返回True，否则返回 False。
    print('-' * 50)

    # 3.求差集
    print(set1.difference(set2))
    print(set1-set2)
    print('-' * 50)

    # 4.求对称差集    即两个集合中各自特有的的元素
    print(set1.symmetric_difference(set2))
    print(set1^set2)#异或操作
    print('-' * 50)

    # 5.判断子集和超集
    print(set1.issubset(set2))    #判断set1是否是set2的子集
    print(set2.issuperset(set1))    #判断set2是否是set1的超集 超集即是指一个集合包含另一个集合的全部元素
    print('-' * 50)

    # 6.更新集合
    print(set1)
    print(set2)
    set1.update(set2)    #更新set1，将set2的元素添加到set1中
    print(set1)
    set1.intersection_update(set2)    #更新set1，将set1和set2的交集更新到set1中
    print(set1)
    set1.difference_update(set2)    #更新set1，将set1和set2的差集更新到set1中
    print(set1)
    set1.symmetric_difference_update(set2)    #更新set1，将set1和set2的对称差集更新到set1中
    print(set1)
    print('-' * 50)

    # 7.其他操作
    print(set1)
    print(set2)
    set1.add(9)    #添加元素到set1中
    print(set1)
    set1.remove(9)    #从set1中删除元素
    print(set1)
    set1.discard(10)    #删除元素，如果元素不存在，不报错
    print(set1)
    set1.pop()    #随机删除一个元素，并返回该元素
    print(set1)
    set1.clear()    #清空set1
    print(set1)
    set1.copy()    #复制set1
    print(set1)
    set1.update([1, 2, 3, 4, 5])    #更新set1，将列表的元素添加到set1中
    print(set1)
    set1.intersection_update([4, 5, 6, 7, 8])    #更新set1，将set1和列表的交集更新到set1中
    print(set1)
    set1.difference_update([4, 5, 6, 7, 8])    #更新set1，将set1和列表的差集更新到set1中
    print(set1)
    set1.symmetric_difference_update([4, 5, 6, 7, 8])    #更新set1，将set1和列表的对称差集更新到set1中
    print(set1)
    print('-'*50)



def use_generator():
    """
    集合的生成器
    :return:
    """
    set1 = {i for i in range(1, 10)}#集合生成式
    print(type(set1))
    print(set1)

    my_tuple = tuple(i for i in range(1, 10))  #元组生成式
    print(type(my_tuple))
    print((my_tuple))#为什么生成元组的元素不能修改，因为元组是不可变的

    set1 = set(my_tuple)
    print(type(set1))
    print(set1)

    set2 = {i**2 for i in range(1, 10)}#i**2表示i的平方
    print(type(set2))
    print(set2)

    my_set={x for x in 'hello world'}
    print(type(my_set))
    print(my_set)

    my_set={x for x in 'hello world' if x not in 'ld'}#去除'ld'中的元素
    print(my_set)

def use_set_query():
    """
    集合的查询
    :return:
    """
    basket = {'apple', 'orange', 'apple', 'pear', 'orange',
              'banana'}
    print(basket)
    print(len(basket))
    print('orange' in basket)#判断元素是否在集合中 是则返回True，否则返回False

    basket.add('grape')
    print(basket)
    x=basket.copy()
    print(x)
    print(id(x))
    print(id(basket))

def use_operators():
    """
    集合的运算符重写
    :return:
    """
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(set1 | set2)  # 并集
    print(set1 & set2)  # 交集
    print(set1 - set2)  # 差集
    print(set1 ^ set2)  # 对称差集   即两个集合中各自特有的的元素  不同时存在于两个集合中的元素  即两个集合的并集中去掉两个集合的交集的部分
    print('-'*50)

def copy_set():
    """
    复制集合
    :return:
    """
    set1 = {1, 2, 3, 4, 5}
    set2 = set1.copy()
    print(set1)
    print(set2)
    set1.add(6)
    print(set1)
    print(set2)  # 复制后的集合与原集合互不影响,表明集合是可变的。
if __name__ == '__main__':
    #use_set()
    #use_set_operation()
    #use_generator()
    #use_set_query()
    # use_operators()
    copy_set()