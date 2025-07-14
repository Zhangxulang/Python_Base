# #数字类型
# z=pow(2,3)
# print(z)
# print(pow(2,3))
# print(pow(2,pow(2,3)))

# z=3+2j    #复试类型
# print(z.imag)
# print(z.real)

# ##e3.1DayDayUp365.py
# import math
# dayup = math.pow((1.0 + 0.001),365) # 每天提高0.001
# daydown = math.pow((1.0 - 0.001), 365) # 每天荒废0.001
# print("向上: %.2f, 向下: %.2f."%(dayup, daydown))

# #e3.2DayDayUp365.py
# import math
# dayup = math.pow((1.0 + 0.005), 365) # 每天提高0.005
# daydown = math.pow((1.0 - 0.005), 365) # 每天荒废0.005
# print("向上: %.2f, 向下: %.2f."%(dayup, daydown))

# #e3.3DayDayUp365.py
# import math
# dayfactor = 0.01
# dayup = math.pow((1.0 + dayfactor), 365) # 提高dayfactor
# daydown = math.pow((1.0 - dayfactor), 365) # 放任dayfactor
# print("向上: {:.2f}, 向下: {:.2f}.".format(dayup, daydown))

# #e3.4DayDayUp365.py
# dayup, dayfactor = 1.0, 0.01
# for i in range(365):
#     if i % 7 not in [6, 0]:
#         dayup = dayup * (1 + dayfactor)
#     else:
#         dayup = dayup * (1 - dayfactor)
# print("向上5 天向下2 天的力量: {:.2f}.".format(dayup))

# #e3.5DayDayUp365.py
# def dayUP(df):
#     dayup = 1.0
#     for i in range(365):
#         if i % 7 in [6, 0]:
#             dayup = dayup * (1 - 0.01)
#         else:
#             dayup = dayup * (1 + df)
#     return dayup
# dayfactor = 0.01
# while (dayUP(dayfactor)<37.78):
#     dayfactor += 0.001
# print("每天的努力参数是: %.3f."%dayfactor)

#●3-6 获取星期字符串
# weekstr = "星期一星期二星期三星期四星期五星期六星期日"
# weekid = eval(input("请输入星期数字(1-7): "))
# pos = (weekid - 1)*3
# print(weekstr[pos: pos+3])

#●3-7 凯撒密码
# plaincode = input("请输入明文: ")
# for p in plaincode:
#     if ord("a") <= ord(p) <= ord("z"):
#         print(chr(ord("a") + (ord(p) - ord("a") + 3)%26),end='')
#     else:
#         print(p, end='')

#●3-8 基本的多行文本进度条
#e4.1TextProgress Bar.py
# import time
# scale = 20
# print("------执行开始------")
# for i in range(scale+1):
#     a, b = '**' * i,'..' * (scale - i)
#     c = (i/scale)*100
#     print("%{:^3.0f}[{}->{}]" .format (c, a, b))
#     time.sleep(0.1)
# print("------执行结束------")

#e4.2TextProgressBar.py
# import time
# for i in range(101):
#     print("\r{:2}%".format(i), end="")
#     time.sleep(0.05)

