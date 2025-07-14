# 作者: 大数据 浪哥
# 2025年07月14日17时00分57秒
# 1054074422@qq.com
#__init__.py文件在包中的作用是将包中的模块导入到当前的命名空间中，使得我们可以直接使用包中的模块。
# 这里我们只需要导入send_message和receive_message两个模块即可。
# 导入方式：from wd_message import send_message, receive_message
# 这样就可以直接使用send_message和receive_message模块了。
# 注意：这里的导入方式是相对导入，即从当前目录开始导入，而不是从包的根目录开始导入。
# 另外，这里的导入方式是导入模块，而不是导入包。
# 因此，如果要导入整个包，则需要使用：import wd_message
# 或者：from wd_message import *
# 这样就可以直接使用包中的所有模块了。

#说白了，就是进行一个权限划分，只对外暴露需要的模块，而把其他依赖的模块隐藏起来。
from . import send_message
from . import receive_message