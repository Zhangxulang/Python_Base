# 作者: 大数据 浪哥
# 2025年07月14日03时50分30秒
# 1054074422@qq.com

def exception_demo1():  # 循环读取直到输入正确的数据类型
    while True:
        try:
            num = int(input("请输入一个数字: "))
            print("你输入的数字是: ", num)
            break
        except ValueError:  # 捕获ValueError异常
            print("输入的不是数字, 请重新输入!")


def exception_demo2():
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("除 0 错误")
    except Exception as e:  # 捕获所有异常 e代表异常对象的别名
        print("未知错误 %s" % e)

#异常捕获完整语法
# def exception_demo3():
#     try:
#         # 尝试执行的代码
#         pass
#     except 错误类型 1:
#         # 针对错误类型 1，对应的代码处理
#         pass
#     except 错误类型 2:
#         # 针对错误类型 2，对应的代码处理
#         pass
#     except (错误类型 3, 错误类型 4):
#         # 针对错误类型 3 和 4，对应的代码处理
#         pass
#     except Exception as result:
#         # 打印错误信息
#         print(result)
#     else:
#         # 没有异常才会执行的代码
#         pass
#     finally:
#         # 无论是否有异常，都会执行的代码（不受 return 影响）
#         print("无论是否有异常，都会执行的代码")

def exception_demo4():
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("除 0 错误")
    except Exception as result:
        print("未知错误 %s" % result)
    else:
        print("正常执行")
    finally:
        print("执行完成，但是不保证正确")

if __name__ == '__main__':
    # exception_demo1()
    exception_demo2()
