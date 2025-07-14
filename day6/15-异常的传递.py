# 作者: 大数据 浪哥
# 2025年07月14日03时51分05秒
# 1054074422@qq.com

# 异常的传递性                  出现异常时，会向上抛出，并被上层调用者捕获。
# 异常的传递性是指当一个函数调用另一个函数，如果该函数发生异常，则会向上抛出，并被上层调用者捕获。
# 异常的传递性可以帮助我们更好地处理异常，避免程序崩溃。

# 举例说明：
def demo1():    # 定义一个函数，输入一个整数
    return int(input("输入整数："))
def demo2():
    return demo1()   # 调用demo1函数，并返回结果

try:
    print(demo2())   # 调用demo2函数，并打印结果
except Exception as result:  # 捕获异常
    print("未知错误 %s" % result)   # 打印异常信息

# 运行结果：
# 输入整数：abc
# 未知错误 invalid literal for int() with base 10: 'abc'     # 捕获到异常，并打印异常信息

# 说明：
# demo2函数调用demo1函数，demo1函数输入整数，输入abc，抛出异常。
# demo2函数捕获到异常，并打印异常信息。