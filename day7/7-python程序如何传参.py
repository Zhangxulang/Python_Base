# 作者: 大数据 浪哥
# 2025年07月15日02时49分53秒
# 1054074422@qq.com

import sys

# print("命令行参数如下:")
# for i in sys.argv:
#     print(i)
# print("脚本名为:", sys.argv[0])  # 脚本名
# print("脚本路径为:", sys.path)  # 脚本路径
#
# print(type(sys.argv))
# print(sys.argv)

def write_file(file_path):
    with open(file_path, 'w+',encoding='utf-8') as f:
        f.write('hello world')

if __name__ == '__main__':
    write_file(sys.argv[1])