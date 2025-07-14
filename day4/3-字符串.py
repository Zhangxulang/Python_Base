# 作者: 大数据 浪哥
# 2025年07月11日12时44分17秒
# 1054074422@qq.com

def is_type():
    """
    判断输入的字符串是否是数字或字母
    """
    s = input("请输入字符串: ")
    if s.isdigit():
        print("输入的字符串是数字")
    elif s.isalpha():
        print("输入的字符串是字母")
    elif s.isalnum():         #所有字符都是字母或数字则返回 True
        print("输入的字符串既是数字又是字母")
    else:
        print("输入的字符串不都是数字或者字母")
def str_find():
    """
    字符串查找与替换
    :return:
    """
    s = input("请输入字符串: ")
    sub = input("请输入要查找的子串: ")
    if sub in s:         #查找子串是否存在于字符串中
        print(f"{sub} 在 {s} 中第一次出现的位置是 {s.find(sub)}")
    else:
        print(f"{sub} 不在 {s} 中")

    s = s.replace(sub, "***",1)         #用 *** 替换子串、第二个
    print(f"替换后的字符串是: {s}")
    #print(s)


def str_split_join():
    """
    字符串分割与合并
    :return:
    """
    s = input("请输入字符串: ")
    sep = input("请输入分隔符: ")
    l = s.split(sep)         #分割字符串
    print(f"分割后的字符串列表是: {l}")

    #合并字符串
    sep1 = input("请输入合并后的分隔符: ")
    s=sep1.join(l)
    print(f"合并后的字符串是: {s}")


def study_r():
    """
    \r 回车符  \n 换行符    \r\n 回车换行的区别
    :return:
    """
    s = "hello\nworld"
    print(s)
    print("-"*50)
    """
    \r 是一个回车符，用于将光标移动到当前行的开头。
       主要用途是在输出时覆盖当前行的内容，而不换行。
       可用于实现进度条或动态更新的输出。
    """
    s = "hello\rworld"
    print(s)
    print("-" * 50)
    s = "hello\r\nworld"
    print(s)

def str_slice():
    """
    字符串切片
    :return:
    """
    s = "hello world"     #字符串[开始索引:结束索引:步长]
    print(s[0:5])         #从索引 0 开始，到索引 5 结束，但不包括索引 5
    print(s[6:])          #从索引 6 开始，到字符串末尾结束
    print(s[:5])          #从字符串开头开始，到索引 5 结束
    print(s[-5:-1])       #从倒数第 5 个字符开始，到倒数第 1 个字符结束，但不包括最后一个字符
    print(s[-1])          #获取最后一个字符
    print(s[::-1])        #字符串反转
    print(s[::2])         #步长为 2 的切片
    print(s[::1])         # 步长为 1 的切片
    print(s[1::2])        #从索引 1 开始，步长为 2 的切片

def list_slice():
    """
    列表切片
    :return:
    """
    my_list=list("hello world")
    print(my_list[0:5])         #从索引 0 开始，到索引 5 结束，但不包括索引 5
    print(my_list[6:])          #从索引 6 开始，到列表末尾结束
    print(my_list[:5])          #从列表开头开始，到索引 5 结束
    print(my_list[-5:-1])       #从倒数第 5 个元素开始，到倒数第 1 个元素结束，但不包括最后一个元素
    print(my_list[-1])          #获取最后一个元素
    print(my_list[::-1])        #列表反转
    print(my_list[::2])         #步长为 2 的切片
    print(my_list[::1])         # 步长为 1 的切片
    print(my_list[1::2])        #从索引 1 开始，步长为 2 的切片
if __name__ == '__main__':
    #is_type()
    #str_find()
    #str_split_join()
    #study_r()
    #str_slice()
    list_slice()

