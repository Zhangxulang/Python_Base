import numpy as np
from PIL import Image
import cv2
# 读取图像
image_path = "path_to_your_image.jpg"
image = Image.open(image_path)
# 转换为NumPy数组
image_array = np.array(image)
# 获取图像大小
height, width, channels = image_array.shape
# 转换颜色空间（可选）
image_array_rgb = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
# 将图像转换为灰度图像
gray_image = cv2.cvtColor(image_array_rgb, cv2.COLOR_RGB2GRAY)
# 进行图像的尺寸调整（可选）
new_width, new_height = 1000, 800
resized_image = cv2.resize(gray_image, (new_width, new_height))
# 保存图像
output_path = "path_to_save_processed_image.jpg"
cv2.imwrite(output_path, resized_image)
