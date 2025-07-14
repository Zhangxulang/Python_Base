# 作者: 大数据 浪哥
# 2025年07月14日15时21分35秒
# 1054074422@qq.com

def input_password():
    # 1. 提示用户输入密码
    pwd = input("请输入密码：")
    # 2. 判断密码长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3. 如果 < 8 主动抛出异常
    print("主动抛出异常")
    # 1> 创建异常对象 - 可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 2> 主动抛出异常
    raise ex


if __name__ == "__main__":
    #input_password()
    try:
        print(input_password())
    except Exception as result:
        print(result)

#断言异常
    try:
        assert 1 == 0, "你的程序在这里发生了什么什么错误"
    except Exception as e:
        print(e)