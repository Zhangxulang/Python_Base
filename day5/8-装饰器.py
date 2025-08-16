# 作者: 大数据 浪哥
# 2025年08月16日16时36分21秒
# 1054074422@qq.com

"""
装饰器是Python中的一种高级功能，它允许你动态地修改函数或类的行为。
装饰器本质上是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。
"""
# 定义一个装饰器用于日志打印
def log_decorator(original_function):
    def wrapper(*args, **kwargs):
        # 记录函数调用前的信息
        print(f"----- 调用函数: {original_function.__name__} ----")
        # 处理位置参数
        if args:
            print("位置参数:")
            for i, arg in enumerate(args):
                print(f"  第{i + 1}个参数: {arg} (类型: {type(arg).__name__})")
        else:
            print("位置参数: 无")

        # 处理关键字参数
        if kwargs:
            print("关键字参数:")
            for key, value in kwargs.items():
                print(f"  {key}: {value} (类型: {type(value).__name__})")
        else:
            print("关键字参数: 无")
        # 调用原始函数
        result = original_function(*args, **kwargs)
        # 记录函数调用后的信息
        print(f"函数返回值: {result} (类型: {type(result).__name__})")
        print(f"----- 函数 {original_function.__name__} 调用结束 -----")
        return result

    return wrapper
# 使用装饰器
@log_decorator  #这里使用@符号将装饰器应用到calculate函数上，相当于calculate = log_decorator(calculate)，当调用calculate函数时，会自动调用log_decorator函数，并将原始函数calculate作为参数传入。
def calculate(a, b, operation='add'):
    """执行简单的数学运算"""
    if operation == 'add':
        return a + b
    elif operation == 'multiply':
        return a * b
    elif operation == 'subtract':
        return a - b
    else:
        return f"不支持的操作: {operation}"


# 测试不同参数组合
calculate(10, 5)  # 仅位置参数
calculate(20, 3, 'multiply')  # 位置参数包含操作
calculate(100, 30, operation='subtract')  # 混合参数
calculate(a=5, b=8, operation='add')  # 仅关键字参数
calculate(10, 5, 'division')  # 非法操作