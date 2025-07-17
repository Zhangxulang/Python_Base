#%% md
# # 一、Python 语法教学
# 适用：Python 初学者教学、演示基础语法（如 for 循环、函数等）
#%%
# 计算 1 到 100 的和
total = sum(range(1, 101))
print("1 到 100 的总和是：", total)
#%% md
# # 二、数据分析（Pandas）
# 适用：数据科学初学者、分析表格数据、探索数据构
#%%
import matplotlib.pyplot as plt
#第一个是x坐标，第二个是y坐标
plt.plot([1, 0, 9], [4, 5, 6])
#展示图像
plt.show()
#%%
import pandas as pd
# 读取销售数据
df = pd.read_csv("sales.csv")
# 显示前几行
df.head()
#%%
# 将日期列转换为 datetime 类型
df['日期'] = pd.to_datetime(df['日期'])

# 按日期汇总销售额
daily_sales = df.groupby('日期')['销售额'].sum()

# 展示
print(daily_sales)
#%%

import pandas as pd
import matplotlib.pyplot as plt

# 设置字体
plt.rcParams['font.family'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

daily_sales.plot(kind='bar', title="每日总销售额", ylabel='销售额')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
#%% md
# # 三、数据可视化（Matplotlib）
# 适用：图表教学、报告可视化展示、探索性数据析
#%%
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title("简单折线图")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.grid(True)
plt.show()
#%% md
# # 四、机器学习训练（sklearn）
# 适用：机器学习初学者、模型训练、模型评估、模型选择和部署演示
#%%
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
model = RandomForestClassifier()
model.fit(iris.data, iris.target)

print("预测结果：", model.predict([[5.1, 3.5, 1.4, 0.2]]))
#%% md
# # 五、Markdown 文档 + 数学公式（LaTeX）
# ## 一元二次方程的解法
# 
# 公式如下：
# 
# $$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
# 
# 这是求解 $ax^2 + bx + c = 0$ 的通用公式。
# 
# 适用：学生、科研人员、教学文档、数学推导、公式演示
#%% md
# # 六、交互式控件（使用 ipywidgets）
# 适用：教学演示、动态交互界面开发、参数调试具
#%%
from ipywidgets import interact

def greet(name):
    print(f"你好，{name}！")

interact(greet, name="小明")
#%% md
# # 七、图像处理（OpenCV）
# 适用：图像处理、机器视觉、计算机视觉、图像分析、图像识别
#%%
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.axis('off')
plt.title("Lena 图像")
plt.show()
#%%
