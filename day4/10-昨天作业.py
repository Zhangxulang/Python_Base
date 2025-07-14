# 作者: 大数据 浪哥
# 2025年07月12日10时31分52秒
# 1054074422@qq.com

def homework1():
    """
    作业1：有7个整数，其中有3个数出现了两次，1个数出现了一次，找出出现了一次的那个数。
    :return:
    """
    my_list = [1, 1, 2, 2, 3, 6, 6]
    result = 0
    # 方法一：count()函数统计某个元素在列表中出现的次数
    for i in my_list:
        if my_list.count(i) == 1:
            result = i
            break
    print(result)
    # 方法二：异或操作：不同位上为1，相同位上为0，异或满足交换律，即a^b^b=a^0=a,适用于找出现奇数次的数
    a = 0
    for i in my_list:
        a ^= i  # ^=展开为a=a^i
    print(a)


def homework2():
    """
    作业2：写一个简单的for循环，从1打印到20，横着打为1排。
    :return:
    """


def homework3():
    """
    作业3：写一个say_hello函数打印多次hello并给该函数加备注(具体打印几次依靠传递的参数)，然后调用say_hello，同时学会快速査看函数备注，及如何跳转到函数实现快捷操作(与上课一致)。
    :return:
    """


def homework4():
    """
    #作业4：写一个模块(命名不要用中文)，模块里写3个打印函数，然后另外一个py文件调用该模块，并调用对应模块的函数，同时用一下下面操作
if __name == '__main__':       wd5.print line()#调用函数。
    :return:
    """


def homework5():
    """
    作业5：练习列表基本使用，排序，生成式等各种操作(与上课的代码保持一致)。
    :return:
    """


def homework6():
    """
    作业6：有8个整数，其中有3个数出现了两次，2个数出现了一次，找出出现了一次的那2个数。
    :return:
    """
    my_list = [1, 1, 2, 2, 3, 6, 6, 8]
    # result = []
    # # 方法一：count()函数统计某个元素在列表中出现的次数
    # for i in my_list:
    #     if my_list.count(i) == 1:
    #         result.append(i)
    #         if len(result) == 2:
    #             break
    # print(result)

    # 方法二：把出现了一次的那个两个数分到两堆，对每一堆异或操作，最后得到的结果就是出现了一次的那2个数
    # 0000 0011   3
    # 0000 1000   8
    result=0
    for i in my_list:
        result ^= i  # ^=展开为a=a^i
    print(result)
    #0000 1011
    #1111 0100 +1= 1111 0101
    #0000 1011 & 1111 0101=0000 0001
    split_flag =result& -result   # 找到最低位的1，即分割点result& -result
    list1 = []
    list2 = []
    result1 = 0
    result2 = 0
    for i in my_list:
        if i & split_flag:
            #list1.append(i)    #[1, 1, 3]
            result1 ^= i
        else:
            #list2.append(i)   #[2, 2, 6, 6, 8]
            result2 ^= i
    #print(list1, list2)
    print(result1, result2)


if __name__ == '__main__':
    # homework1()
    homework6()
