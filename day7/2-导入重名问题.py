# 作者: 大数据 浪哥
# 2025年07月14日16时43分16秒
# 1054074422@qq.com

# import module1
# module1.add(1, 2)

from module1 import add
from module2 import add as module2_add# 导入重名函数,需要用as给函数起别名

"""
经常使用add1时，可以只导入add1函数，而不用导入整个模块。
省去了写模块名的麻烦。
"""
print(add(1, 2))
