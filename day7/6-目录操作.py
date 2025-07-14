# 作者: 大数据 浪哥
# 2025年07月14日22时54分30秒
# 1054074422@qq.com

import os


# 重命名文件或目录
def rename_file():
    """
    重命名文件或目录
    s.rename(old_name, new_name)
    :param old_name: 旧文件或目录名
    :param new_name: 新文件或目录名
    :return:
    """
    os.rename('file1.txt', 'file2.txt')


def delete_file():
    """
    删除文件或目录 (慎用)
    os.remove(file_name)
    :param file_name: 文件或目录名
    :return:
    """
    os.remove('file2.txt')


def create_file():
    """
    创建文件
        open(file_name, mode)
    :param file_name: 文件名
    :param mode: 读写模式
    :return:
    """
    with open('file1.txt', 'w') as f:
        f.write('goodmorning')


def create_dir():
    """
    创建目录
        os.mkdir(dir_name)
    :param dir_name: 目录名
    :return:
    """
    os.mkdir('dir1')  # 创建目录 dir1


# 修改工作目录
def change_dir():
    """
    修改工作目录
        os.chdir(dir_name)
    :param dir_name: 目录名
    :return:
    """
    os.chdir('dir1')  # 类似于cd命令，切换到目录 dir1
    # 列出目录下的所有文件和目录
    with open('file1.txt', 'w') as f:
        f.write('goodnight')
    print(os.listdir())


def delete_dir():
    """
    删除目录
        os.rmdir(dir_name)
    :param dir_name: 目录名
    :return:
    """
    # os.chdir('..')  # 切换到上级目录
    os.remove('dir1/file1.txt')  # 删除文件 file1.txt
    os.rmdir('dir1')  # 删除目录 dir1（只能删除空目录）


# 获取当前目录
def get_current_dir():
    """ 获取当前目录
        os.getcwd()
    :return: 当前目录路径
    """
    print(os.getcwd())


# 获取文件或目录的属性
def get_file_attr():
    """ 获取文件或目录的属性
        os.stat(file_name)
    :param file_name: 文件或目录名
    :return: 包含文件或目录属性的对象
    """
    print(os.stat('dir1/file1.txt'))
    print(os.stat('dir1'))  # st_size=0表示目录，非0表示文件
    os.chdir('dir1')  # 类似于cd命令，切换到目录 dir1
    os.mkdir('new_dir')
    os.chdir('new_dir')  # 类似于cd命令，切换到目录 dir1
    with open('file1.txt', 'w') as f:
        f.write('hello')
    print(os.stat('file1.txt'))  # 目录属性和文件属性不同，目录没有大小属性


# 获取文件大小
def get_file_size():
    """ 获取文件大小
        os.path.getsize(file_name)
    :param file_name: 文件名
    :return: 文件大小，单位为字节
    """
    print(os.path.getsize('dir1/file1.txt'))


# 判断文件或目录是否存在
def is_file_exist():
    """ 判断文件或目录是否存在
        os.path.exists(file_name)
    :param file_name: 文件或目录名
    :return: True/False
    """
    print(os.path.exists('file1.txt'))


# 判断是否为文件
def is_file():
    """ 判断是否为文件
        os.path.isfile(file_name)
    :param file_name: 文件名
    :return: True/False
    """
    print(os.path.isfile('dir1/file1.txt'))


# 判断是否为目录
def is_dir():
    """ 判断是否为目录
        os.path.isdir(dir_name)
    :param dir_name: 目录名
    :return: True/False
    """
    print(os.path.isdir('dir1'))


# 显示当前目录下的所有文件和目录
def list_dir():
    """ 显示当前目录下的所有文件和目录
        os.listdir()
    :return: 包含文件和目录名的列表
    """
    # items=os.listdir()
    # for item in items:  #每行显示一个
    #     print(item)
    #     print(os.path.join(os.getcwd(), item))  #显示完整路径
    for item in sorted(os.listdir()):
        print(item)  # 按字母顺序排序


def use_stat(file_path):
    """
    使用stat模块获取文件属性
    :param file_path: 文件路径
    :return:
    """
    file_info = os.stat(file_path)
    print('size:{},uid:{},mode:{},mtime:{}'.format(file_info.st_size,
                                                   file_info.st_uid, file_info.st_mode,
                                                   file_info.st_mtime))

    # mtime表示的是 从 1970 年 1 月 1 日 00:00:00 UTC 起，到某一时间点的秒数（浮点型时间戳）
    from time import gmtime, strftime
    gm_time = gmtime(file_info.st_mtime)
    print(gm_time)  # 时间元组
    print(strftime("%Y-%m-%d %H:%M:%S", gm_time))  # 格式化时间元组,前6个参数


# 深度优先遍历目录
def traverse_dir(current_path, width):
    """
    遍历目录
    :param dir_path: 目录路径
    :return:
    """
    file_list = os.listdir(current_path)#os.listdir(current_path) 得到的是当前目录下的文件/子目录的名称列表，而不是它们的完整路径。
    for file in file_list:
        print(' ' * width, file)  # 打印当前目录下的文件
        """
        构建当前项目的完整路径（用于后续判断是否是文件夹）
        os.path.isdir() 需要的是完整路径，否则判断可能出错。
        """
        new_path = os.path.join(current_path, file)  # 构造新路径
        if os.path.isdir(new_path):  # 如果是目录，递归调用
            traverse_dir(new_path, width + 4)


# 遍历当前目录及其子目录
if __name__ == '__main__':
    # rename_file()
    # delete_file()
    # create_file()
    # create_dir()
    # change_dir()
    # delete_dir()     # 删除目录 dir1（只能删除空目录）
    # get_current_dir()
    # get_file_attr()
    # get_file_size()
    # is_file_exist()
    # is_file()
    # is_dir()
    # use_stat('dir1/file1.txt')
    traverse_dir('.', 0)
