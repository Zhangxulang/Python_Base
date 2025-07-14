# 作者: 大数据 浪哥
# 2025年07月12日01时35分56秒
# 1054074422@qq.com

def list_set_slice():
    """
    列表的切片操作和集合的切片操作是一样的，都是[start:end:step]，其中start是开始索引，end是结束索引，step是步长。
    切片操作的结果是一个新的列表或集合。
    :return:
    """
    test_list=[1,2,3,4,5,6]
    test_list[3:3]=['x','y','z']   #[1, 2, 3, 'x', 'y', 'z', 4, 5, 6]往列表中插入一个列表
    print(test_list)

def list_compare():
    """
    列表的比较操作是通过元素的位置来比较的，如果两个列表的元素位置相同，则认为它们相等。
    集合的比较操作是通过元素的哈希值来比较的，如果两个集合的元素哈希值相同，则认为它们相等。
    :return:
    """
    a =[1, 2, 3, 4, 5, 6]#列表是可变数据类型，所以可以修改元素的值
    b =[1, 2, 3, 4, 5, 6]
    print(a==b)   #作用是判断两个列表是否有相同的元素，返回True或False
    print(set(a)==set(b))   #作用是判断两个列表是否有相同的元素，返回True或False
    print(a is b)   #is判断两个变量是否指向同一个对象，是则返回True，否则返回False

def use_method():
    """
    列表和集合都有很多共同的操作方法，比如append()、extend()、insert()、remove()、pop()等。
    这些方法的用法基本相同，这里就不一一列举了。
    :return:
    """
    a = (1, 2, 3)
    b = ('a', 'b', 'c')
    print(list(zip(a, b)))
    # 如何使用 enumerate
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list2 = list(enumerate(seasons))#enumerate的作用是将列表中的元素和索引组成一个元组，组成一个新的列表
    print(list2)
    my_dict=dict(list2)
    print(my_dict)
    print({v:k for k,v in my_dict.items()})#字典生成式，作用是将元组列表转换为字典


if __name__ == '__main__':
    #list_set_slice()
    #list_compare()
    use_method()