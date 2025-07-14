# 作者: 大数据 浪哥
# 2025年07月12日02时55分08秒
# 1054074422@qq.com

def measure():
    """
    掌握返回多个值时，如何解包
    :return
    """

    print("开始测量...")
    temp = 39
    wetness = 0.5
    humidity = 0.8
    print("测量结束...")
    return temp, wetness, humidity

result = measure()
print(result)
r1, r2, r3 = result# 对元组解包
print(r1, r2, r3)
