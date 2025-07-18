# 作者: 大数据 浪哥
# 2025年06月12日05时01分54秒
# 1054074422@qq.com
# 练习 1: 定义一个整数变量 age，编写代码判断年龄是否正确
age = 100
# 要求人的年龄在 0-120 之间
if age >= 0 and age <= 120:
    print("年龄正确")
else:
    print("年龄不正确")
print('-'*50)
##########################################
# 练习 2: 定义两个整数变量 python_score、c_score，编写代码判断成绩
python_score = 50
c_score = 50
# 要求只要有一门成绩 > 60 分就算合格
if python_score > 60 or c_score > 60:
    print("考试通过")
else:
    print("再接再厉！")
print('-'*50)
##########################################
# 练习 3: 定义一个布尔型变量 `is_employee`，编写代码判断是否是本公司员工
is_employee = False
# 如果不是提示不允许入内
if not is_employee:#负负得正才会进入if语句
    print("非公勿内")
print('-'*50)
##########################################
# 练习 4: # 定义布尔型变量 has_ticket 表示是否有车票，定义整数型变量 knife_length 表示刀的长度，单位：厘米
# 编写代码，判断是否有车票，如果有，则进行安检，安检时，需要检查刀的长度，判断是否超过 20 厘米，如果超过 20 厘米，提示刀的长度，不允许上车，如果不超过 20 厘米，安检通过，如果没有车票，不允许进门
has_ticket = False
knife_length = 20
# 首先检查是否有车票，如果有，才允许进行 安检
if has_ticket:
    print("有车票，可以开始安检...")
# 安检时，需要检查刀的长度，判断是否超过 20 厘米
# 如果超过 20 厘米，提示刀的长度，不允许上车
    if knife_length >= 20:
        print("不允许携带 %d 厘米长的刀上车" % knife_length)
# 如果不超过 20 厘米，安检通过
    else:
        print("安检通过，祝您旅途愉快……")
# 如果没有车票，不允许进门
else:
    print("大哥，您要先买票啊")
print('-'*50)
##########################################
# 练习 5: 先 假定电脑就只会出石头，完成整体代码功能
# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("请出拳 石头（1）／剪刀（2）／布（3）："))
# 电脑 随机 出拳 - 假定电脑永远出石头
computer = 1
# 比较胜负
# 如果条件判断的内容太长，可以在最外侧的条件增加一对大括号
# 再在每一个条件之间，使用回车，PyCharm 可以自动增加 8 个空格
if ((player == 1 and computer == 2) or(player == 2 and computer == 3) or(player == 3 and computer == 1)):
    print("噢耶！！！电脑弱爆了！！！")
elif player == computer:
    print("心有灵犀，再来一盘！")
else:
    print("不行，我要和你决战到天亮！")