# 作者: 大数据 浪哥
# 2025年07月14日17时04分56秒
# 1054074422@qq.com

import wd_message

wd_message.send_message.send()
wd_message.receive_message.receive()

import random
print(random.__file__)      #打印随机数模块的路径
print(wd_message.send_message.__file__)     #打印发送消息模块的路径
rand = random.randint(0, 10)
print(rand)