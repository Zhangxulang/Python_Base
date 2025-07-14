# 作者: 大数据 浪哥
# 2025年07月12日12时12分04秒
# 1054074422@qq.com
import sys
sys.setrecursionlimit(1000000)  # 设置递归深度，防止栈溢出


# 递归可以实现的，循环也可以实现，递归实现起来更简单，而且效率更高。
# 1、找到递推公式
# 2、确定结束条件
def sum_numbers(num):
    print(num)
    # 递归的出口（结束条件）很重要，否则会出现死循环
    if num == 1:
        return
    sum_numbers(num - 1)


# question: 请用递归函数实现求1到n的和
# 1、找到递推公式：sum = num + sum(num-1)
# 2、确定结束条件：num == 1时，返回num
# 3、实现代码：
def sum_numbers(n):
    if n == 1:
        return n
    else:
        return n + sum_numbers(n - 1)


def step(n):
    if n == 1 or n == 2:
        return n

    return step(n - 1) + step(n - 2)


if __name__ == '__main__':
    # sum_numbers(5)
    # print(sum_numbers(1000))
    for i in range(1,10):#range(1,10)作用是生成1到9的数字，左闭右开
        print(step(i))
