# 作者: 大数据 浪哥
# 2025年08月13日16时49分03秒
# 1054074422@qq.com

import torch
# 随机生成一个3x4的张量，元素值在0-1之间
input = torch.randint(10, (3, 4))  #左闭右开区间
print(input)
# 随机生成一个3x4的张量，元素值在0-100之间
input = torch.randint(0,100, (3, 4))
print(input)
#randint函数的第一个参数是下限，第二个参数是上限，第三个参数是形状
#高级用法：
#torch.randint(low=0, high=None, size=None, dtype=torch.int64, layout=torch.strided, device=None, requires_grad=False)
#low：下限，默认值为0。
#high：上限，必须大于等于low。
#size：形状，默认为None。
#dtype：数据类型，默认为torch.int64。
#layout：布局，默认为torch.strided。
#device：设备，默认为None。
#requires_grad：是否需要求导，默认为False。
