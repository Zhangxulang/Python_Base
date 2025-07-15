# 作者: 大数据 浪哥
# 2025年07月16日01时21分21秒
# 1054074422@qq.com
import os
import sys
"""
将一个项目子目录 module 加入模块搜索路径，并导入自定义模块 my_module.py，从而调用其函数。
"""
sys.path.insert(0,'module')  #把当前项目中的 module 文件夹加入模块搜索路径的最前面
                                            #这样就可以像导入标准库一样导入 module 目录下的 my_module.py 文件了
for i in sys.path:  #sys.path 是 Python 查找模块的路径列表。默认情况下只会查找内置库和当前工作目录
    print(i)
print('-'*50)
import my_module
my_module.test1()

print("当前工作路径：", os.getcwd())
print("模块路径是否存在：", os.path.exists('module/my_module.py'))