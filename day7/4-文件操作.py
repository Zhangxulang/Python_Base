# 作者: 大数据 浪哥
# 2025年07月14日18时08分06秒
# 1054074422@qq.com

def open_r():  # 只读模式
    """
    以只读方式打开文件。文件的指针将会放在文件的开头，这是默认模式。
如果文件不存在，抛出异常
    :return:
    """
    text = open('file.txt', 'r', encoding='utf-8')
    f = text.read()
    print(f)
    text.close()


def open_rj():  # 读写模式
    """
    以读写方式打开文件。文件的指针将会放在文件的开头。如果文件不存
在，抛出异常(写入时，文件位置指针会跳转到尾部）
    :return:
    """
    text = open('file.txt', 'r+', encoding='utf-8')
    f = text.read()
    print(f)
    text.write('0000 1111')
    print(text.read())
    text.close()


def open_rb():  # 二进制读模式
    """
    以二进制只读方式打开文件。文件的指针将会放在文件的开头，这是默认模式。
如果文件不存在，抛出异常
    :return:
    """
    text = open('file.txt', 'rb')
    f = text.read()
    print(f)
    text.close()


def open_w():  # 只写模式
    """
    以写方式打开文件。如果文件不存在，则创建新文件。如果文件存在，则清空文件（覆盖原有内容）。
文件的指针将会放在文件的开头，这是默认模式。
    :return:
    """
    text = open('file.txt', 'w', encoding='utf-8')
    text.write('hello world')
    text.close()


def open_wb():  # 二进制写模式
    """
    以二进制写方式打开文件。如果文件不存在，则创建新文件。如果文件存在，则清空文件。
文件的指针将会放在文件的开头，这是默认模式。
    :return:
    """
    text = open('file.txt', 'wb')
    text.write(b'hello world11')
    text.close()


def open_w_n():  # 读写模式
    """
    以写方式打开文件。如果文件不存在，则创建新文件。如果文件存在，则清空文件。
文件的指针将会放在文件的结尾，文件写入时不会覆盖已有内容。
    :return:
    """
    text = open('file.txt', 'w+', encoding='utf-8')
    text.write('我爱你中国母亲')
    text.seek(0)  # 移动文件指针到开头，作用是清空文件
    print(text.read())
    text.close()


def open_a():  # 追加模式
    """
    以追加模式打开文件。如果文件不存在，则创建新文件。
文件的指针将会放在文件的结尾，文件写入时不会覆盖已有内容。
    :return:
    """
    text = open('file.txt', 'a', encoding='utf-8')
    text.write('\nhello world')#换行追加
    #text.seek(0)#移动文件指针到开头，作用是清空文件
    text.close()


def open_ab():
    """
    以二进制追加模式打开文件。如果文件不存在，则创建新文件。
文件的指针将会放在文件的结尾，文件写入时不会覆盖已有内容。
    :return:
    """
    text = open('file.txt', 'ab')
    text.write(b'\nhello world')
    text.close()


def open_a_n():  # 读写模式
    """
    以追加模式打开文件。如果文件不存在，则创建新文件。
文件的指针将会放在文件的结尾，文件写入时不会覆盖已有内容。
    :return:
    """
    text = open('file.txt', 'a+', encoding='utf-8')
    text.write('\nhello world')
    text.seek(0)#移动文件指针到开头，作用是清空文件
    print(text.read())
    text.close()


def open_x():#创建模式
    """
    以创建模式打开文件。如果文件存在，则抛出异常。如果文件不存在，则创建新文件。
文件的指针将会放在文件的开头，这是默认模式。
    :return:
    """
    text = open('file1.txt', 'x', encoding='utf-8')
    text.write('hello world')
    text.close()


def open_xb():#创建模式
    """
    以二进制创建模式打开文件。如果文件存在，则抛出异常。如果文件不存在，则创建新文件。
文件的指针将会放在文件的开头，这是默认模式。
    :return:
    """
    text = open('file.txt', 'xb')
    text.write(b'hello world')
    text.close()


if __name__ == '__main__':
    # open_r()
    # open_rj()
    # open_rb()
    # open_w()
    # open_wb()
    #open_w_n()
    #open_a()
    # open_ab()
    #open_a_n()
    open_x()
    # open_xb()
