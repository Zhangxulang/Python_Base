[跳至内容](https://chatgpt.com/c/688210b9-c480-8008-b9fe-6217a4ed1172#main)

## 历史聊天记录









##### 您说：

""" 线性回归直接预测房子价格 :return: None """ # 获取数据 fe_cal = fetch_california_housing(data_home='data') print("获取特征值") print(fe_cal.data.shape) print('-' * 50) print(fe_cal.data[0]) print("目标值") print(fe_cal.target) #单位是10万美金 print(fe_cal.DESCR) print('-' * 50) print(fe_cal.feature_names) #特征列的名字.代码作用

###### ChatGPT 说：

这段代码是用来**获取并查看加利福尼亚房价数据集**（California Housing dataset），为后续的**线性回归建模预测房价**做准备。下面是逐行解释及其作用：

------

### 🔧 所需模块

```
from sklearn.datasets import fetch_california_housing
```

- `fetch_california_housing` 是 `sklearn.datasets` 中的一个函数，用于下载和加载加州房价数据集（California Housing dataset）。

------

### 🏠 加载数据

```
fe_cal = fetch_california_housing(data_home='data')
```

- 加载加州房价数据集。
- `data_home='data'` 指定将数据下载并缓存到本地 `data` 目录。
- 返回的是一个 **`Bunch`** 类型（类似字典），包含了特征值、目标值、特征名、描述信息等。

------

### 📊 打印特征值形状

```
print("获取特征值")
print(fe_cal.data.shape)
```

- `.data` 是数据集中的特征矩阵，类型为 `numpy.ndarray`。
- `.shape` 返回的是 (样本数, 特征数)，比如 `(20640, 8)` 表示共有 20640 个样本，每个样本有 8 个特征。

------

### 🔍 打印首行特征数据

```
print('-' * 50)
print(fe_cal.data[0])
```

- 打印第一个样本的所有特征值（8 个 float 数值）。

------

### 🎯 打印目标值（房价）

```
print("目标值")
print(fe_cal.target) #单位是10万美金
```

- `.target` 是每个样本对应的房价目标值（单位：10万美元）。
- 是一个一维数组，形如 `[4.526, 3.585, 3.521, ...]`。

------

### 📘 数据集说明文档

```
print(fe_cal.DESCR)
```

- `.DESCR` 是该数据集的文字描述，包括来源、各特征的含义、使用建议等。

------

### 🏷️ 特征名称

```
print('-' * 50)
print(fe_cal.feature_names)
```

- `.feature_names` 是一个包含 8 个字符串的列表，对应每列特征的名称：

```
['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
 'Population', 'AveOccup', 'Latitude', 'Longitude']
```

| 特征名     | 含义                 |
| ---------- | -------------------- |
| MedInc     | 区域住户收入中位数   |
| HouseAge   | 房屋平均建造年限     |
| AveRooms   | 每个家庭的平均房间数 |
| AveBedrms  | 每个家庭的平均卧室数 |
| Population | 区域人口             |
| AveOccup   | 每户平均人数         |
| Latitude   | 纬度                 |
| Longitude  | 经度                 |

------

### ✅ 总结：代码的作用

这段代码的主要作用是：

- 下载并加载加州房价数据集；
- 输出特征矩阵的形状、首行数据、目标值、特征名及数据描述；
- 为后续构建如线性回归模型等机器学习任务提供数据基础。

如果你后续要用 `LinearRegression` 来预测房价，这段代码就作为数据加载和探索的第一步。

------

如需继续，我可以帮你写出 **线性回归建模、训练、评估与可视化完整流程**，是否需要？

##### 您说：

以下代码作用是什么：fe_cal.target.shape #%% # 分割数据集到训练集和测试集 x_train, x_test, y_train, y_test = train_test_split(fe_cal.data, fe_cal.target, test_size=0.25, random_state=1) # print(x_train.shape) # # # 进行标准化处理(?) 目标值处理？ # # 特征值和目标值是都必须进行标准化处理, 实例化两个标准化API std_x = StandardScaler() # x_train = std_x.fit_transform(x_train) #训练集标准化 x_test = std_x.transform(x_test) #测试集标准化 # 目标值进行了标准化，暂时没有对目标值进行标准化处理 # std_y = StandardScaler() # # temp = y_train.reshape(-1, 1) #-1代表把剩余的元素都堆到哪一维 # # #标签（目标）进行标准化 # # 目标值是一维的，这里需要传进去2维的 # y_train = std_y.fit_transform(y_train.reshape(-1, 1))  #把一维的标签变成二维的 # print(y_train.shape) # y_test = std_y.transform(y_test.reshape(-1, 1)) # print(y_test.shape) #%% test1=np.array([1,2,3]) print(test1.shape) test1.reshape(-1,1).shape #%% import os # # estimator预测 # # # 正规方程求解方式预测结果，正规方程进行线性回归 lr = LinearRegression() # fit是耗时的 lr.fit(x_train, y_train) #回归系数可以看特征与目标之间的相关性，系数越大，相关性越强，负相关意味着特征与目标的方向相反 print('回归系数', lr.coef_) # y_predict = lr.predict(x_test) # 预测测试集的房子价格，通过inverse得到真正的房子价格 # y_lr_predict = std_y.inverse_transform(y_predict) # 保存训练好的模型，模型中保存的是w的值，也保存了模型结构 #保存模型放在fit之后即可 os.unlink('./tmp/test.pkl') # 删除之前的模型文件 joblib.dump(lr, "./tmp/test.pkl")  # 保存模型 print("正规方程测试集里面每个房子的预测价格：", y_predict[0:10]) #下面是求测试集的损失，用均方误差，公式是(y_test-y_predict)^2/n print("正规方程的均方误差：", mean_squared_error(y_test, y_predict)) #%% #正规方程的均方误差： 0.535653284542256 #%% md # 2 加载保存的模型 #%% #模拟上线时加载模型 model = joblib.load("./tmp/test.pkl") # # 因为目标值进行了标准化，一定要把预测后的值逆向转换回来 y_predict = model.predict(x_test) # print("保存的模型预测的结果：", y_predict) print("正规方程的均方误差：", mean_squared_error(y_test, y_predict)) # print("正规方程inverse后的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), #                                                std_y.inverse_transform(y_predict))) #%% y_true = [3, -0.5, 2, 7] y_pred = [2.5, 0.0, 2, 8] mean_squared_error(y_true, y_pred) #%% #人工求均方误差 (np.square(3 - 2.5) + np.square(0.5) + 1) / 4 #%% md # 3 线性回归之梯度下降去进行房价预测 #%% # 梯度下降去进行房价预测,数据量大要用这个 # learning_rate的不同方式，代表学习率变化的算法不一样,比如constant,invscaling,adaptive # 默认可以去调 eta0 = 0.008，会改变learning_rate的初始值 # learning_rate='optimal',alpha是正则化力度，但是会影响学习率的值，由alpha来算学习率 # penalty代表正则化，分为l1和l2 # eta0=0.01, penalty='l2',max_iter=1000 sgd = SGDRegressor(eta0=0.01,penalty='l2', max_iter=1000) # # 训练 sgd.fit(x_train, y_train) # print('梯度下降的回归系数', sgd.coef_) # # 预测测试集的房子价格 # y_sgd_predict = std_y.inverse_transform(sgd.predict(x_test).reshape(-1, 1)) y_predict = sgd.predict(x_test) # print("梯度下降测试集里面每个房子的预测价格：", y_sgd_predict) print("梯度下降的均方误差：", mean_squared_error(y_test, y_predict)) # print("梯度下降的原始房价量纲均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_sgd_predict)) #%% w=1 lreaning_rate=0.1  #学习率 def loss(w):    return 2*w**2+3*w+2 def dao_shu(w):    return 4*w+3 for i in range(30):    w=w-lreaning_rate*dao_shu(w)    print(f'w {w} 损失{loss(w)}') #%% md # 4 岭回归 #%% # # # 岭回归去进行房价预测 #岭回归是对线性回归加入L2正则化，L2正则化是对系数的平方和进行惩罚 #alpha就是补偿的系数 #正规方程求解，加补偿就可以让正规方程可逆 rd = Ridge(alpha=0.02) rd.fit(x_train, y_train) print(rd.coef_) # # # 预测测试集的房子价格 print(rd.predict(x_test).shape) # y_rd_predict = std_y.inverse_transform(rd.predict(x_test)) y_predict = rd.predict(x_test) # print("岭回归里面每个房子的预测价格：", y_rd_predict) print("岭回归的均方误差：", mean_squared_error(y_test, y_predict)) # print("岭回归的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_rd_predict)) #%% md # 5 lasso回归 #%% # # # Lasso回归去进行房价预测 #alpha就是补偿的系数 print(x_train.shape) print(y_train.shape) ls = Lasso(alpha=0.001) ls.fit(x_train, y_train) print(ls.coef_) # # # 预测测试集的房子价格 print(ls.predict(x_test).shape) print('-'*50) # y_ls_predict = std_y.inverse_transform(ls.predict(x_test).reshape(-1,1)) y_predict = ls.predict(x_test) # print("Lasso回归里面每个房子的预测价格：", y_rd_predict) # print("Lasso回归的均方误差：", mean_squared_error(y_test, y_predict)) # print("Lasso回归的均方误差：", mean_squared_error(std_y.inverse_transform(y_test), y_ls_predict)) #%% md # 6 逻辑回归 可以做分类问题，预测癌症是否良性，预测股票涨跌，预测病人是否会死亡等等 #%% np.log(0.5) #%% np.log(0.3) #%% x=np.arange(0.001,1,0.01) #0-1之间，步长0.01 import matplotlib.pyplot as plt plt.plot(x,-np.log(x))  #以e为底部 plt.show() #%% x=np.arange(0,1,0.01) import matplotlib.pyplot as plt plt.plot(x,-np.log(1-x)) plt.show() #%% """ 逻辑回归做二分类进行癌症预测（根据细胞的属性特征） :return: NOne """ # 构造列标签名字 column = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',          'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli',          'Mitoses', 'Class'] # 读取数据 # data = pd.read_csv( #     "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data", #     names=column) data = pd.read_csv(    "./data/breast-cancer-wisconsin.csv",    names=column) # print(data) #想看可以解除 #当你读取数据时，看上去是数值的列，读进来是字符串，说明里边 # 存在了非数值情况 print(data.info()) print(data.describe(include='all')) #%% data['Bare Nuclei'].unique() #因为上面发现它是object类型 #%% # 缺失值进行处理 data = data.replace(to_replace='?', value=np.nan) #直接删除，哪一行有空值，就删除对应的样本 data = data.dropna() print('-' * 50) print(data.shape) #%% data.info() #%% column[10] #%% #分类的类别是2和4,对应 "良性", "恶性" data[column[10]].unique() #%% data.info() #%% column[6] #%% #把第6列的字符串转化为数字类型 data[column[6]] = data[column[6]].astype('int16') #%% data.info() #%% # 进行数据的分割,第零列是编号，不可以作为特征，把第1-9列作为特征，第10列作为标签 x_train, x_test, y_train, y_test = train_test_split(data[column[1:10]], data[column[10]], test_size=0.25,                                                    random_state=1) # 进行标准化处理 std = StandardScaler() x_train = std.fit_transform(x_train) #训练集标准化 x_test = std.transform(x_test) #测试集标准化 x_train[0] #%% # # # 逻辑回归预测 # C正则化力度 # solver = 'liblinear'  solver是学习率优化算法，就是学习率会随着epoch的变化而变化 #epoch就代表第几次迭代 #max_iter 最大迭代次数 lg = LogisticRegression(C=0.5, solver='lbfgs') # lg.fit(x_train, y_train) # 逻辑回归的权重参数，了解，没那么重要 print(lg.coef_) y_predict = lg.predict(x_test) print(y_predict) #预测的标签 print("准确率：", lg.score(x_test, y_test)) print(y_test[0:5]) print('-'*50) print(lg.predict_proba(x_test)[0:5])  #得出对应分类的概率 #%% # 为什么还要看下召回率，labels和target_names对应 # macro avg 平均值  weighted avg 加权平均值 print(classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"])) #AUC计算要求是二分类，不需要是0和1 print("AUC指标：", roc_auc_score(y_test, y_predict)) #%% print(x_train.shape) print(x_test.shape) #%% print(-np.log(0.1)) #%% -np.log(0.9)  #%% x=-3/10 y=5*x**2+3*x+4 y #%%

###### ChatGPT 说：

已更新保存的记忆

这段代码是一个完整的机器学习建模流程，涵盖了：

1. **房价预测（回归任务）**：
   - 使用了线性回归（正规方程）、梯度下降、岭回归、Lasso回归；
   - 目标是使用加州房价数据集预测房屋价格；
   - 使用 `mean_squared_error` 作为模型评估标准；
   - 使用了 `StandardScaler` 进行特征标准化；
   - 用 `joblib` 对模型进行保存与加载；
   - 包含了均方误差（MSE）人工推导过程。
2. **癌症预测（分类任务）**：
   - 使用了逻辑回归；
   - 数据为乳腺癌数据集（来自UCI）；
   - 对“是否为恶性肿瘤”进行分类；
   - 使用了 `accuracy`、`precision`、`recall`、`f1-score`、`AUC` 等评价指标。

------

下面对关键代码和知识点逐块解释：

------

## 🔍 `fe_cal.target.shape` 的作用

```
fe_cal.target.shape
```

这是为了查看目标值 `y` 的形状（维度）：

- 输出：如 `(20640,)`，表示共有 20640 个目标值（房价数据），是一维数组。
- 如果需要对目标值进行标准化，需 `.reshape(-1, 1)` 转成二维数组。

------

## 🧪 数据划分与标准化

```
x_train, x_test, y_train, y_test = train_test_split(...)
```

- 将数据划分为训练集和测试集；
- `test_size=0.25` 表示测试集占 25%。

```
std_x = StandardScaler()
x_train = std_x.fit_transform(x_train)
x_test = std_x.transform(x_test)
```

- 使用 `StandardScaler` 对特征进行标准化处理；
- 目的是让特征值服从标准正态分布，有利于梯度下降算法收敛。

> ✅ 注意：你没有对目标值 `y` 进行标准化处理，但注释里说明了如何做（如 reshape, fit_transform）。

------

## 🧮 模型1：正规方程线性回归

```
lr = LinearRegression()
lr.fit(x_train, y_train)
y_predict = lr.predict(x_test)
```

- 使用 `LinearRegression` 建模（正规方程法）；
- 训练后可以输出 `coef_` 回归系数。

```
mean_squared_error(y_test, y_predict)
```

- 计算预测结果与实际房价的 **均方误差（MSE）**。

------

## 💾 模型保存与加载

```
joblib.dump(lr, "./tmp/test.pkl")
model = joblib.load("./tmp/test.pkl")
```

- 用 `joblib` 将训练好的模型保存并再次加载（模拟上线部署）；

------

## 🧮 模型2：梯度下降线性回归

```
sgd = SGDRegressor(...)
sgd.fit(x_train, y_train)
y_predict = sgd.predict(x_test)
```

- 使用 `SGDRegressor`（随机梯度下降法）；
- 学习率 `eta0=0.01`；
- 正则化项 `penalty='l2'` 表示 L2 正则。

------

## 📉 梯度下降演示（自定义例子）

```
def loss(w): ...
def dao_shu(w): ...
```

- 演示梯度下降优化过程；
- 用一个简单的二次函数 L(w)=2w2+3w+2*L*(*w*)=2*w*2+3*w*+2；
- 每步根据导数 dLdw=4w+3*d**w**d**L*=4*w*+3 迭代更新 `w`。

------

## 🧮 模型3：岭回归（L2正则）

```
rd = Ridge(alpha=0.02)
rd.fit(x_train, y_train)
```

- 岭回归是在线性回归中加入了 L2 正则化；
- 可防止过拟合，尤其在特征共线性明显时效果好。

------

## 🧮 模型4：Lasso回归（L1正则）

```
ls = Lasso(alpha=0.001)
ls.fit(x_train, y_train)
```

- Lasso 是加入了 L1 正则化的线性回归；
- 可以产生稀疏解（即部分特征的系数为 0，自动特征选择）。

------

## 🧪 模型5：逻辑回归进行分类（癌症预测）

- 加载数据集 `breast-cancer-wisconsin`；
- 删除缺失值；
- 将特征标准化；
- 使用逻辑回归 `LogisticRegression` 进行二分类；
- 使用 `.score()` 计算准确率；
- 使用 `classification_report` 和 `roc_auc_score` 进一步评价模型：

```
print(classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"]))
print("AUC指标：", roc_auc_score(y_test, y_predict))
```

------

## 📈 对数函数可视化部分：

```
x = np.arange(0.001, 1, 0.01)
plt.plot(x, -np.log(x))
```

- 展示了逻辑回归中的对数损失函数的形状；
- 对分类模型的解释（如 log loss）有帮助。

------

## ✅ 总结

这段代码系统地展示了：

| 类型 | 模型               | 描述               |
| ---- | ------------------ | ------------------ |
| 回归 | LinearRegression   | 正规方程           |
| 回归 | SGDRegressor       | 梯度下降           |
| 回归 | Ridge              | 岭回归（L2）       |
| 回归 | Lasso              | L1回归             |
| 分类 | LogisticRegression | 二分类预测（癌症） |

你已经掌握了回归与分类两大类模型的使用，包括模型保存、标准化处理、误差计算等，下一步可以进一步：

- 进行 **交叉验证** 和 **网格搜索调参**；
- 使用 `Pipeline` 管理数据流；
- 尝试集成模型（如 `RandomForest`, `GradientBoosting`）等。

需要我帮你扩展成一个系统性项目流程/报告模板吗？或者你想尝试网格搜索调参、特征工程等内容？

##### 您说：

逐行代码注释

###### ChatGPT 说：

以下是你给出的 **房价预测与逻辑回归分类代码的逐行详细注释**，涵盖了数据加载、预处理、模型训练、预测、保存/加载、可视化与评价等完整过程。按代码结构分段整理，方便你学习与复盘：

------

## 🚩**1. 获取加州房价数据集**

```
fe_cal = fetch_california_housing(data_home='data')  # 下载加州房价数据并缓存到本地 data 目录
print("获取特征值")
print(fe_cal.data.shape)  # 打印特征矩阵的维度（样本数 × 特征数）
print('-' * 50)
print(fe_cal.data[0])     # 打印第一个样本的所有特征值
print("目标值")
print(fe_cal.target)      # 打印目标值（每个样本对应的房价，单位：10万美元）
print(fe_cal.DESCR)       # 打印数据集的详细描述（数据来源、字段含义等）
print('-' * 50)
print(fe_cal.feature_names)  # 打印特征名列表，如 ['MedInc', 'HouseAge', ...]
fe_cal.target.shape  # 查看目标值（y）的 shape，结果为 (20640,) 表示是一维数组
```

------

## ✂️ **2. 划分训练集和测试集**

```
x_train, x_test, y_train, y_test = train_test_split(
    fe_cal.data, fe_cal.target, test_size=0.25, random_state=1
)  # 按 75% / 25% 划分训练集和测试集
print(x_train.shape)  # 打印训练特征集的维度
```

------

## 🔧 **3. 特征值标准化处理**

```
std_x = StandardScaler()  # 实例化特征标准化器
x_train = std_x.fit_transform(x_train)  # 对训练特征做标准化：均值为0、方差为1
x_test = std_x.transform(x_test)        # 测试集也要用训练集的标准进行转换
```

> ✅（注：你注释了目标值 `y` 的标准化部分，常用于岭回归、SGD 回归中）

------

## 🧪 **4. 训练线性回归模型（正规方程法）**

```
lr = LinearRegression()   # 实例化线性回归模型
lr.fit(x_train, y_train)  # 用训练数据拟合模型（计算权重 w 和偏置 b）
print('回归系数', lr.coef_)  # 打印每个特征的权重系数
y_predict = lr.predict(x_test)  # 用模型对测试数据进行预测，得到预测房价
```

------

## 💾 **5. 保存并加载模型**

```
os.unlink('./tmp/test.pkl')  # 删除旧模型文件（避免影响）
joblib.dump(lr, "./tmp/test.pkl")  # 保存训练好的模型到本地文件
print("正规方程测试集里面每个房子的预测价格：", y_predict[0:10])  # 显示前10个预测房价
print("正规方程的均方误差：", mean_squared_error(y_test, y_predict))  # 评估模型性能（MSE）
```

------

## 📂 **6. 加载已保存模型并评估**

```
model = joblib.load("./tmp/test.pkl")  # 从磁盘加载已保存的模型
y_predict = model.predict(x_test)      # 用加载的模型再次对测试数据进行预测
print("保存的模型预测的结果：", y_predict)
print("正规方程的均方误差：", mean_squared_error(y_test, y_predict))
```

------

## 🔢 **7. 人工计算 MSE**

```
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
mean_squared_error(y_true, y_pred)  # sklearn 自带均方误差计算
(np.square(3 - 2.5) + np.square(0.5) + 1) / 4  # 手动计算 MSE = ((0.5)^2 + (0.5)^2 + 0 + 1^2) / 4
```

------

## ⚙️ **8. 梯度下降模拟演示**

```
w = 1
lreaning_rate = 0.1  # 学习率

def loss(w): return 2 * w**2 + 3 * w + 2   # 自定义损失函数
def dao_shu(w): return 4 * w + 3           # 自定义导数函数（梯度）

for i in range(30):
    w = w - lreaning_rate * dao_shu(w)  # 梯度更新公式
    print(f'w {w} 损失{loss(w)}')        # 输出每次迭代后的 w 和损失值
```

------

## 📉 **9. 使用 SGDRegressor（梯度下降）**

```
sgd = SGDRegressor(eta0=0.01, penalty='l2', max_iter=1000)  # SGD 回归器，L2正则
sgd.fit(x_train, y_train)                                   # 训练模型
print('梯度下降的回归系数', sgd.coef_)
y_predict = sgd.predict(x_test)                             # 预测
print("梯度下降的均方误差：", mean_squared_error(y_test, y_predict))
```

------

## 🧊 **10. 岭回归（Ridge：L2正则）**

```
rd = Ridge(alpha=0.02)        # 实例化岭回归模型
rd.fit(x_train, y_train)      # 训练模型
print(rd.coef_)               # 打印回归系数
y_predict = rd.predict(x_test)
print("岭回归的均方误差：", mean_squared_error(y_test, y_predict))
```

------

## 🔍 **11. Lasso回归（L1正则）**

```
ls = Lasso(alpha=0.001)       # 实例化 Lasso 回归（L1正则）
ls.fit(x_train, y_train)      # 训练模型
print(ls.coef_)
y_predict = ls.predict(x_test)
print("Lasso回归的均方误差：", mean_squared_error(y_test, y_predict))
```

------

## 📦 **12. 加载乳腺癌数据集（逻辑回归）**

```
column = [...]  # 定义列名
data = pd.read_csv("./data/breast-cancer-wisconsin.csv", names=column)
print(data.info())              # 查看数据类型
print(data.describe(include='all'))  # 数据概览
data['Bare Nuclei'].unique()   # 查看特定列是否有异常字符
```

------

## 🧼 **13. 缺失值处理 + 类型转换**

```
data = data.replace(to_replace='?', value=np.nan)  # 用 NaN 替换 '?'
data = data.dropna()                               # 删除含 NaN 的行
data[column[6]] = data[column[6]].astype('int16')  # 类型转换：字符串 ➝ 整数
```

------

## ✂️ **14. 划分训练集与测试集 + 标准化**

```
x_train, x_test, y_train, y_test = train_test_split(
    data[column[1:10]], data[column[10]], test_size=0.25, random_state=1
)
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)
```

------

## 🤖 **15. 逻辑回归分类器**

```
lg = LogisticRegression(C=0.5, solver='lbfgs')  # 实例化逻辑回归，带正则项
lg.fit(x_train, y_train)                        # 训练模型
print(lg.coef_)             # 打印模型系数
y_predict = lg.predict(x_test)  # 预测标签
print("准确率：", lg.score(x_test, y_test))  # 计算准确率
print(lg.predict_proba(x_test)[0:5])          # 输出预测为每类的概率
```

------

## 📊 **16. 分类性能评价指标**

```
print(classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"]))
print("AUC指标：", roc_auc_score(y_test, y_predict))  # AUC 值评价模型性能
```

------

## 📈 **17. 对数函数绘图（损失函数原理）**

```
x = np.arange(0.001, 1, 0.01)
plt.plot(x, -np.log(x))          # 画 -log(x) 图像
plt.show()

x = np.arange(0, 1, 0.01)
plt.plot(x, -np.log(1 - x))      # 画 -log(1-x) 图像
plt.show()
```

------

## ✅ 小结

你实现了从数据预处理 ➝ 回归预测 ➝ 模型保存 ➝ 模型评估 ➝ 分类预测 ➝ 性能评估的完整流程，是机器学习训练-预测流程的经典样板。

------

如果你需要，我可以进一步：

- 帮你生成**汇报文档（Word、PDF）**
- 加入**网格搜索调参**
- 将多个模型整合为**统一 Pipeline**
- 使用交叉验证、学习曲线评估过拟合

是否需要我协助下一步？







ChatGPT 也可能会犯错。请核查重要信息。