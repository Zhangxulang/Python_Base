# 作者: 大数据 浪哥
# 2025年08月09日00时46分06秒
# 1054074422@qq.com

import torch
import numpy as np

print("-" * 60)
print("NumPy → PyTorch（共享内存）")
numpy_array = np.array([[1, 2, 3], [4, 5, 6]])
print(f"NumPy 数组:\n{numpy_array} | 类型: {type(numpy_array)}")

# from_numpy 不会复制数据（共享内存）
tensor_from_numpy = torch.from_numpy(numpy_array)
print(f"转换后的 PyTorch 张量:\n{tensor_from_numpy} | 类型: {type(tensor_from_numpy)}")

# 修改 NumPy，观察张量变化
numpy_array[0, 0] = 100
print(f"修改后的 NumPy 数组:\n{numpy_array}")
print(f"PyTorch 张量也同步变化:\n{tensor_from_numpy}")

print("-" * 60)
print("PyTorch → NumPy（共享内存）")
# 注意：如果张量在 GPU，需要先 .cpu()
tensor = torch.tensor([[7, 8, 9], [10, 11, 12]], dtype=torch.float32)
print(f"PyTorch 张量:\n{tensor} | 类型: {type(tensor)}")

numpy_from_tensor = tensor.numpy()
print(f"转换后的 NumPy 数组:\n{numpy_from_tensor} | 类型: {type(numpy_from_tensor)}")

# 修改张量，NumPy 也会变
tensor[0, 0] = 77
print(f"修改后的 PyTorch 张量:\n{tensor}")
print(f"NumPy 数组也同步变化:\n{numpy_from_tensor}")

print("-" * 60)
print("独立数据（不共享内存）")

# 方法1: clone()
tensor_independent = torch.tensor([[13, 14, 15], [16, 17, 18]], dtype=torch.float32)
numpy_clone = tensor_independent.clone().numpy()
tensor_independent[0, 0] = 0
print("使用 clone():")
print(f"修改后的张量:\n{tensor_independent}")
print(f"NumPy（不受影响）:\n{numpy_clone}")

# 方法2: numpy.copy()
numpy_copy = tensor.numpy().copy()
tensor[0, 0] = 999
print("\n使用 numpy.copy():")
print(f"修改后的张量:\n{tensor}")
print(f"NumPy（不受影响）:\n{numpy_copy}")