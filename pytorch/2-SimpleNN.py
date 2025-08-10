# 作者: 大数据 浪哥
# 2025年08月09日01时12分16秒
# 1054074422@qq.com
import torch
import torch.nn as nn

# 定义一个简单的神经网络
class SimpleNN(nn.Module):
    """
    一个两层全连接的简单神经网络:
    输入层 -> 隐藏层(ReLU激活) -> 输出层
    """
    def __init__(self):
        super(SimpleNN, self).__init__()
        # 输入层到隐藏层，全连接
        self.fc1 = nn.Linear(in_features=2, out_features=2)
        # 隐藏层到输出层，全连接
        self.fc2 = nn.Linear(in_features=2, out_features=1)

    def forward(self, x):
        # 先进行线性变换，再加ReLU非线性激活
        x = torch.relu(self.fc1(x))
        # 再进行一次线性变换得到最终输出
        x = self.fc2(x)
        return x

# 创建模型实例
model = SimpleNN()
print("模型结构：")
print(model)
# 打印模型参数数量
total_params = sum(p.numel() for p in model.parameters())
print(f"\n模型总参数量: {total_params}")

# 测试数据（2个特征）
sample_input = torch.tensor([[0.5, 1.0],
                              [1.5, -0.5],
                              [-1.0, 2.0]], dtype=torch.float32)

# 模型预测
output = model(sample_input)
print("\n输入数据:")
print(sample_input)
print("\n模型输出:")
print(output)

# 对比：去掉激活函数的效果
class WithoutActivationNN(nn.Module):
    def __init__(self):
        super(WithoutActivationNN, self).__init__()
        self.fc1 = nn.Linear(2, 2)
        self.fc2 = nn.Linear(2, 1)

    def forward(self, x):
        # 没有非线性激活，直接两次线性变换
        x = self.fc1(x)
        x = self.fc2(x)
        return x

model_no_act = WithoutActivationNN()
output_no_act = model_no_act(sample_input)

print("\n没有激活函数的输出:")
print(output_no_act)