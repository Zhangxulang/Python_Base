# # 作者: 大数据 浪哥
# # 2025年07月14日01时55分01秒
# # 1054074422@qq.com
#
#
# #如果要循环读取文件，可以使用for循环，每次读取一行数据，并对数据进行处理。
# #以下代码使用for循环读取文件，并将每行数据打印到屏幕上。
#
# #打开文件
# f = open('test.txt', 'r',encoding='utf-8')
#
# #循环读取文件
# for line in f:
#     print(line)
#
# #关闭文件
# f.close()
# #也可以使用while循环读取文件，每次读取一行数据，并对数据进行处理。
#
# #打开文件
# f = open('test.txt', 'r',encoding='utf-8')
#
# #循环读取文件
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
#
# #关闭文件
# f.close()

#也可以使用readlines()方法一次性读取文件的所有行，并返回一个列表。
#打开文件
# f = open('test.txt', 'r',encoding='utf-8')
#
# #读取所有行
# lines = f.readlines()
#
# #打印所有行
# for line in lines:
#     print(line)
#
# #关闭文件
# f.close()
#
# #也可以使用with语句自动关闭文件。
# with open('test.txt', 'r',encoding='utf-8') as f:
#     for line in f:
#         print(line)
#
# #以上代码将自动关闭文件，不需要手动关闭文件。
#
# #注意：如果文件很大，使用readlines()方法可能会导致内存溢出，建议使用for循环或while循环逐行读取文件。

num=input()
my_list=num.split()
print(my_list)
"""
    输入： 安小姐 设计 纠结啊 纠结啊和
    输出：[ '安小姐', '设计', '纠结啊', '纠结啊和']
    
"""