# 作者: 大数据 浪哥
# 2025年07月14日21时45分00秒
# 1054074422@qq.com

import os  # 导入os模块作用是操作文件和目录

def seek_start():
    file = open('file.txt', 'rb')
    file.seek(5, os.SEEK_SET)
    print(file.read())
    file.close()


def seek_end():  #从文件末尾向后偏移  正数表示向后偏移，负数表示向前偏移
    file = open('file.txt', 'rb')
    file.seek(10, os.SEEK_END)  #从文件末尾向后偏移10个字节
    print(file.read())
    file.seek(-5, os.SEEK_END)  #从文件末尾向前偏移5个字节
    print(file.read())
    file.close()


def seek_cur():
    f = open('file.txt', 'rb')
    print("初始位置：", f.tell())  # 应该是 0
    # 第一次读取 5 个字节
    part1 = f.read(5)
    print("读取前5字节：", part1)
    print("当前位置：", f.tell())  # 打印当前位置
    # 从当前位置偏移 3 字节（跳过3个字节）
    f.seek(3, os.SEEK_CUR)
    print("偏移后位置：", f.tell())  # 新的位置
    # 再次读取接下来的内容
    part2 = f.read()
    print("跳过3字节后读到的内容：", part2)
    print("最终的位置：", f.tell())

def moive_to_start():
    f = open('gpt.png', 'rb')
    text = f.read()
    f2=open('gpt2.png','wb')  #创建新文件
    f2.write(text)
    print(f2.tell())
    f2.seek(-3,os.SEEK_CUR)
    print(f2.tell())

def moive_to_end():
    f=open('gpt.png','rb')
    print(f.tell())
    original_bytes = f.read(3)
    print(f.tell())
    inverted_bytes = bytes([b ^ 0xFF for b in original_bytes])#反转字节
    f1=open('gpt.png','r+b')  #'r+b' 模式：允许同时读取和写入二进制文件，不会清空原文件
    f1.seek(0)
    f1.write(inverted_bytes)
    f.close()


if __name__ == '__main__':
    #seek_start()
    #seek_cur()
    #seek_end()
    #moive_to_start()
    moive_to_end()