# 作者: 大数据 浪哥
# 2025年06月12日06时15分27秒
# 1054074422@qq.com

# • 在循环过程中，如果 某一个条件满足后，不 再希望 循环继续执行，可以使用break 退出循环
i = 0
while i < 10:
    # break 某一条件满足时，退出循环，不再执行后续重复的代码
    # i == 3 时，满足条件，退出循环
    print(i)
    i += 1
    if i == 3:
        break
print("over")
# break 只针对当前所在循环有效
