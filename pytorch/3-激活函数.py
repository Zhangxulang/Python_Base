# 作者: 大数据 浪哥
# 2025年08月09日01时29分07秒
# 1054074422@qq.com

import torch
import torch.nn.functional as F
# 创建一个示例张量（包含正数、负数、0）
input_tensor = torch.tensor([[-2.0, -0.5, 0.0, 0.5, 2.0]])
print("输入张量:")
print(input_tensor)
# ReLU 激活：负数变 0，正数不变
output_relu = F.relu(input_tensor)
print("\nReLU 输出 (负数变0):")
print(output_relu)
# 2Sigmoid 激活：将值映射到 (0, 1)，形状类似 S 曲线
output_sigmoid = torch.sigmoid(input_tensor)
print("\nSigmoid 输出 (映射到0~1):")
print(output_sigmoid)
# 3Tanh 激活：将值映射到 (-1, 1)，形状类似压缩的 S 曲线
output_tanh = torch.tanh(input_tensor)
print("\nTanh 输出 (映射到-1~1):")
print(output_tanh)
# 4LeakyReLU 激活（允许负数通过一定比例）
output_leakyrelu = F.leaky_relu(input_tensor, negative_slope=0.1)
print("\nLeakyReLU 输出 (负数衰减):")
print(output_leakyrelu)

# 5. Softmax 激活：将值映射为概率分布（和为1）
output_softmax = F.softmax(input_tensor, dim=1)  # dim=1表示对每一行计算
print("\nSoftmax 输出 (概率分布):")
print(output_softmax)
print("概率和:", torch.sum(output_softmax).item())  # 验证和为1