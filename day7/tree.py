# 作者: 大数据 浪哥
# 2025年07月15日01时13分07秒
# 1054074422@qq.com

import os

def tree(dir_path, prefix=''):
    for i, name in enumerate(os.listdir(dir_path)):
        path = os.path.join(dir_path, name)
        connector = '└── ' if i == len(os.listdir(dir_path)) - 1 else '├── '
        print(prefix + connector + name)
        if os.path.isdir(path):
            extension = '    ' if i == len(os.listdir(dir_path)) - 1 else '│   '
            tree(path, prefix + extension)

if __name__ == '__main__':
    tree('.')