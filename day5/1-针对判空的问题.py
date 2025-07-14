# 作者: 大数据 浪哥
# 2025年07月12日12时11分13秒
# 1054074422@qq.com

#空的容器和None是不同的，None表示空值，而空的容器则是容器里面没有任何元素。
#判空的标准是：容器是否为空，而不是容器里面是否有元素。
#判空的常用方法有：
#1.使用len()函数判断容器的长度是否为0
#2.使用if语句判断容器是否为None
#3.使用bool()函数判断容器是否为True
#4.使用try-except语句捕获IndexError异常

def test():
    if []:#容器是空就是假，不可以用==False对应，因为[]也是False

        print("[] is not empty")
    else:
        print("[] is empty")

    if None:
        print("None is not empty")
    else:
        print("None is empty")

    if{}:
        print("{} is not empty")
    else:
        print("{} is empty")

    if 0:#0是空的容器 0 == False
        print("0 is not empty")
    else:
        print("0 is empty")




def test_empty_container():
    #1.使用len()函数判断容器的长度是否为0
    lst = [1, 2, 3]
    if len(lst) == 0:
        print("lst is empty")
    else:
        print("lst is not empty")

    #2.使用if语句判断容器是否为None
    lst = [1, 2, 3]
    if lst is None:
        print("lst is None")
    else:
        print("lst is not None")

    #3.使用bool()函数判断容器是否为True
    lst = [1, 2, 3]
    if bool(lst):
        print("lst is True")
    else:
        print("lst is False")

    #4.使用try-except语句捕获IndexError异常
    lst = [1, 2, 3]
    try:
        lst[3]
    except IndexError:
        print("lst is empty")
    else:
        print("lst is not empty")

if __name__ == '__main__':
    test()
    test_empty_container()

    #总结：
    #1.判空的标准是：容器是否为空，而不是容器里面是否有元素。
    #2.判空的常用方法有：len()函数、if语句、bool()函数、try-except语句。