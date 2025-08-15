# 作者: 大数据 浪哥
# 2025年08月16日04时18分49秒
# 1054074422@qq.com

# 断言（assert）是一种在程序运行时进行检查的机制，用于判断一个表达式或变量的值是否符合预期。
# 如果表达式或变量的值不符合预期，assert语句将抛出一个AssertionError异常，并中断程序的执行。
# 因此，在开发过程中，我们可以用assert语句来验证程序的运行结果是否符合预期，从而发现和修复程序中的错误。

def calculate_area(radius):
    # 确保半径是正数
    assert radius > 0, "半径必须为正数"     #用于检查传入函数的参数是否符合预期（如类型、范围、非空性等），确保函数在合法的输入下运行
    return 3.14 * radius **2

def divide(a, b):
    # 假设 b 不为 0（如果违反会立即报错）
    assert b != 0, "除数不能为 0"   #用断言明确表达代码中的隐含假设，比注释更严格（会实际执行检查）
    return a / b

def some_calculation(x, y):
    return x + y
def complex_operation(x, y):
    result = some_calculation(x, y)  #在排查 bug 时，用断言在关键位置验证变量值或逻辑分支，快速缩小问题范围
    # 验证中间结果是否在合理范围内
    assert 0 <= result <= 100, f"计算结果 {result} 超出预期范围"
    return result


def add(x, y):
    return x + y
def test_add():  #在单元测试中，用断言验证函数返回值是否符合预期结果
    assert add(2, 3) == 6, "加法运算错误"

if __name__ == '__main__':
    print(calculate_area(5))  # 78.53981633974483
    # print(calculate_area(-5))  # AssertionError: 半径必须为正数
    print('-'*50)
    print(divide(10, 2))  # 5.0
    # print(divide(10, 0))  # AssertionError: 除数不能为 0
    print('-'*50)
    print(complex_operation(5, 3))  # 8
    # print(complex_operation(101, 3))  # AssertionError: 计算结果 104 超出预期范围
    test_add()