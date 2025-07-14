#e1.1TempConvert.py
# TempStr = input("请输入带有符号的温度值: ")
# if TempStr[-1] in ["F","f"]:                           #:表示缩进（tab键）
#     C = (eval(TempStr[0:-1]) - 32)/1.8                 #eval()函数作用：将字符串转为python语句（就是去掉“”）然后执行转化后的语句
#     print("转换后的温度是{:.2f}C".format(C))
# elif TempStr[-1] in ['C','c']:
#     F = 1.8*eval(TempStr[0:-1]) + 32
#     print("转换后的温度是{:.2f}F".format(F))
# else:
#     print("输入格式错误")


# #e1.2TempConvert.py
# TempStr = input("请输入带有符号的温度值: ")
# while TempStr[-1] not in ['N','n']:
#     if TempStr[-1] in ['F','f']:
#         C = (eval(TempStr[0:-1]) - 32)/1.8
#         print("转换后的温度是{:.2f}C".format(C))
#     elif TempStr[-1] in ['C','c']:
#         F = 1.8*eval(TempStr[0:-1]) + 32
#         print("转换后的温度是{:.2f}F".format(F))
#     else:
#         print("输入格式错误")
#     TempStr = input("请输入带有符号的温度值: ")


# #e1.3TempConvert.py
# def tempConvert(ValueStr):
#     if ValueStr[-1] in ['F','f']:
#         C = (eval(ValueStr[0:-1]) - 32)/1.8
#         print("转换后的温度是{:.2f}C".format(C))
#     elif ValueStr[-1] in ['C','c']:
#         F = 1.8*eval(ValueStr[0:-1]) + 32
#         print("转换后的温度是{:.2f}F".format(F))
#     else:
#         print("输入格式错误")
# TempStr = input("请输入带有符号的温度值: ")
# tempConvert(TempStr)


#e2.1DrawPython.py
# import turtle
# turtle.setup(650, 350, None, None)        #设置主窗体的大小和位置
# turtle.penup()                          #抬起画笔
# turtle.fd(-250)                         #负号表示画笔朝相反方向前进250个像素点
# turtle.pendown()                        #落下画笔
# turtle.pensize(20)                      #设置画笔尺寸
# turtle.pencolor("purple")               #设置画笔颜色:紫色
# turtle.seth(-40)                        #改变画笔绘制方向：绝对角度
# for i in range(4):                      #遍历循环4次
#     turtle.circle(40, 80)  #radius半径、extend弧长 、
#     turtle.circle(-40, 80)
# turtle.circle(40, 80/2)
# turtle.fd(40)
# turtle.circle(16, 180)
# turtle.fd(40 * 2/3)


# #e2.2DrawPython.py
# from turtle import *
# setup(650, 350, 200, 200)
# penup()
# fd(-250)
# pendown()
# pensize(25)
# pencolor("purple")
# seth(-40)
# for i in range(4):
#     circle(40, 80)
#     circle(-40, 80)
# circle(40, 80/2)
# fd(40)
# circle(16, 180)
# fd(40 * 2/3)

#e2.3DrawPython.py
# import turtle
# def drawSnake(radius, angle, length):
#     turtle.seth(-40)
#     for i in range(length):
#         turtle.circle(radius, angle)
#         turtle.circle(-radius, angle)
#     turtle.circle(radius, angle/2)
#     turtle.fd(40)
#     turtle.circle(16, 180)
#     turtle.fd(40* 2/3)
# turtle.setup(650, 350, 200, 200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor("purple")
# drawSnake(40, 80, 4)
# turtle.done()

#作业画圆
# import  turtle
# turtle.setup(650,600,200,200)
# turtle.pendown()
# turtle.pensize(20)
# turtle.circle(100,None)
# turtle.penup()
import cv2
import numpy as np
