# 一、折线图（Line Plot）


```python
import matplotlib.pyplot as plt  # 导入绘图库matplotlib的pyplot模块，常用别名plt

# 设置图表显示的中文字体为微软雅黑，防止中文乱码
plt.rcParams['font.family'] = 'Microsoft YaHei'
# 设置负号正常显示（避免负号变成方块）
plt.rcParams['axes.unicode_minus'] = False

# x轴数据：代表月份（第1月~第5月）
x = [1, 2, 3, 4, 5]

# y轴数据：代表每个月的销售额
y = [10, 20, 25, 30, 40]

# 绘制折线图
# 参数说明：
#   x, y：横纵坐标的数据
#   label：图例名称
#   color：线的颜色，这里是蓝色
#   marker：数据点的样式，这里是圆圈'o'
plt.plot(x, y, label="销售额", color='blue', marker='o')

# 设置图表标题
plt.title("折线图示例")

# 设置x轴标签
plt.xlabel("月份")

# 设置y轴标签
plt.ylabel("销售额")

# 显示图例（与label对应）
plt.legend()

# 显示网格线，便于观察
plt.grid(True)

# 正确设置x轴刻度和标签（注意标签是列表）  间距为1
# @range(起始值, 结束值（不含）, 步长):生成一个整数序列
# scale表示刻度尺度
# fontsize表示字体大小
# fontweight表示字体粗细 bold:粗体
# color表示字体颜色
# rotation表示旋转角度



plt.xticks(range(min(x), max(x)+1, 1),['1月', '2月',' 3月', '4月', '5月'],fontsize=12, fontweight='bold', color='red', rotation=45)

# 设置y轴刻度为整数，间隔为5
plt.yticks(range(min(y), max(y)+1, 5))


# 显示图表
plt.show()
```


    
![png](1-matplotlib%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE_files/1-matplotlib%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE_1_0.png)
    


1. 参数	说明
2. plt.plot()	用于绘制折线图
3. label	设置图例名称，需要与 plt.legend() 配合使用
4. color	折线颜色，如 'blue', 'red', '#FF5733'
5. marker	数据点标记样式，如 'o' 圆点，'s' 方形，'^' 三角形
6. plt.title()	设置图表的主标题
7. plt.xlabel() / plt.ylabel()	分别设置x轴和y轴的标签
8. plt.legend()	显示图例
9. plt.grid(True)	显示背景网格线

# 二、散点图（Scatter Plot）


```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 20, 15, 25, 10]

plt.scatter(x, y, color='green', label="样本数据")
plt.title("散点图示例")
plt.xlabel("X值")
plt.ylabel("Y值")
plt.legend()
plt.show()
```


    
![png](1-matplotlib%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE_files/1-matplotlib%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE_4_0.png)
    


# 三、柱状图（Bar Chart）


```python
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

plt.bar(labels, values, color='orange')
plt.title("柱状图示例")
plt.xlabel("产品")
plt.ylabel("销量")
plt.show()
```


    
![png](1-matplotlib%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE_files/1-matplotlib%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE_6_0.png)
    


# 四、饼图（Pie Plot）


```python
import matplotlib.pyplot as plt

labels = ['苹果', '香蕉', '橙子', '梨']
sizes = [30, 25, 25, 20]
colors = ['red', 'yellow', 'orange', 'green']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title("水果销量占比")
plt.axis('equal')  # 保证饼图为圆形
plt.show()

```


    
![png](1-matplotlib%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE_files/1-matplotlib%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE_8_0.png)
    


# 五、直方图（Histogram）


```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title("直方图示例")
plt.xlabel("值")
plt.ylabel("频率")
plt.grid(True)
plt.show()
```


    
![png](1-matplotlib%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE_files/1-matplotlib%E5%9F%BA%E7%A1%80%E7%BB%98%E5%9B%BE_10_0.png)
    



```python

```
