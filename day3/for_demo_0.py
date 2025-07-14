# 作者: 大数据 浪哥
# 2025年06月12日22时31分07秒
# 1054074422@qq.com

# for 循环
mylist = [1, 2, 3]
for i in mylist:
    print(i)  # 输出1 2 3
    print(i, end="\t")

print("")
for i in range(10):
    if i == 5:
        print('i have 5')
        break
    else:
        print(i)  # 输出0 1 2 3 4 6 7 8 9
        print("don't find")
