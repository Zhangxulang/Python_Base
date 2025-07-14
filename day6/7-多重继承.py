# 作者: 大数据 浪哥
# 2025年07月13日19时04分11秒
# 1054074422@qq.com

class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A, B):
    def __init__(self):
        super().__init__()# 调用父类的__init__方法,记住有括号
        print("C")

if __name__ == '__main__':
    c = C() # 输出: A C
    print(C.__mro__) # 查看C的继承顺序
    # 多重继承的顺序是从左到右，即先继承A，再继承B，最后继承C。
    # 由于C继承了A和B，所以先输出A和B，最后输出C。
    # 注意：多重继承时，子类必须在括号中指定所有父类，即不能只继承一个父类。
