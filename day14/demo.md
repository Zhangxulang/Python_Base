代码注释和解释







我们以泰坦尼克号生存预测为例，详细注释代码并解释关键步骤。

 注意：由于实际数据文件路径和预处理细节可能不同，以下代码为通用示例。

 我们将使用pandas进行数据处理，sklearn的RandomForestClassifier构建模型。

 步骤：

1. 导入必要的库
2. 加载数据
3. 数据预处理（处理缺失值、特征转换）
4. 划分训练集和测试集
5. 训练随机森林模型
6. 评估模型
7. 查看特征重要性

以下是详细注释的代码示例，结合机器学习核心算法应用场景进行解释：

### 1. K-近邻算法（KNN）实现约会匹配预测

python

```
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

# 模拟数据集：年龄、年收入(美元)、每周游戏时长(小时)
data = np.array([
    [25, 50000, 10],
    [30, 80000, 2],
    [22, 30000, 15],
    [35, 120000, 1],
    [28, 75000, 3]
])
labels = np.array([1, 0, 1, 0, 0])  # 1:匹配成功, 0:不匹配

# 数据标准化：消除量纲差异（KNN对特征尺度敏感）
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)  # 计算均值和标准差并转换数据

# 数据集划分：80%训练，20%测试
X_train, X_test, y_train, y_test = train_test_split(
    scaled_data, labels, test_size=0.2, random_state=42
)

# 创建KNN分类器（选择3个最近邻居）
knn = KNeighborsClassifier(n_neighbors=3)

# 模型训练
knn.fit(X_train, y_train)

# 预测新样本：28岁/年收入6万/每周游戏5小时
new_sample = scaler.transform([[28, 60000, 5]])  # 必须使用相同的标准化转换
prediction = knn.predict(new_sample)

print("匹配可能性:", "成功" if prediction[0] == 1 else "失败")
print("测试集准确率:", knn.score(X_test, y_test))
```

### 2. 朴素贝叶斯垃圾邮件分类

python

```
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report

# 邮件数据集
emails = [
    "免费领取优惠券 限时特惠",  # 垃圾邮件
    "项目会议安排 周三下午",    # 正常邮件
    "双十一大促 全场五折",      # 垃圾邮件
    "季度报告提交截止通知"       # 正常邮件
]
labels = [1, 0, 1, 0]  # 1:垃圾邮件, 0:正常邮件

# 文本特征提取：将文本转换为词频矩阵
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)  # 学习词汇表并转换文本

# 创建朴素贝叶斯分类器（使用拉普拉斯平滑）
nb = MultinomialNB(alpha=1.0)

# 模型训练
nb.fit(X, labels)

# 测试新邮件
test_emails = ["限时优惠 点击领取", "项目进度汇报"]
X_test = vectorizer.transform(test_emails)
predictions = nb.predict(X_test)

# 输出预测结果和分类报告
print("预测结果:", ["垃圾邮件" if p == 1 else "正常邮件" for p in predictions])
print("\n分类评估报告:")
print(classification_report(
    [1, 0],  # 测试样本真实标签
    predictions,
    target_names=["正常邮件", "垃圾邮件"]
))
```

### 3. 决策树医疗诊断系统

python

```
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz

# 患者症状数据集：发烧(1是/0否)、咳嗽强度(1-3级)、血象指数
symptoms = np.array([
    [1, 3, 90],
    [0, 1, 120],
    [1, 2, 85],
    [0, 2, 110],
    [1, 1, 95]
])
diagnoses = np.array([1, 0, 1, 0, 0])  # 1:流感, 0:普通感冒

# 创建决策树（使用基尼系数，限制树深度防过拟合）
tree = DecisionTreeClassifier(
    criterion='gini', 
    max_depth=3,
    random_state=42
)

# 模型训练
tree.fit(symptoms, diagnoses)

# 可视化决策树
dot_data = export_graphviz(
    tree,
    out_file=None,
    feature_names=['发烧', '咳嗽', '血象'],  # 特征名称
    class_names=['普通感冒', '流感'],        # 目标类别名称
    filled=True,                           # 颜色填充
    rounded=True                           # 圆角边框
)
graph = graphviz.Source(dot_data)
graph.render("medical_tree")  # 生成PDF文件

# 预测新患者
new_patient = [[1, 2, 88]]
prediction = tree.predict(new_patient)
print("\n诊断结果:", "流感" if prediction[0] == 1 else "普通感冒")
```

### 4. 随机森林信用卡欺诈检测

python

```
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

# 模拟信用卡交易数据
transactions = np.array([
    [1000, 5, 300],    # 大额/高风险商户/夜间交易
    [20, 12, 10],      # 小额/超市/实时交易
    [5000, 3, 86400],   # 极大额/高风险商户/24小时前
    [150, 8, 1200]     # 中等额度/普通商户/20分钟前
])
fraud_labels = np.array([0, 1, 0, 0])  # 1:欺诈交易

# 创建随机森林（100棵树，限制深度防过拟合）
rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42,
    n_jobs=-1  # 使用所有CPU核心加速
)

# 模型训练
rf.fit(transactions, fraud_labels)

# 特征重要性分析
feature_importance = rf.feature_importances_
features = ['交易金额', '商户类型', '时间差']
print("特征重要性分析:")
for feat, imp in zip(features, feature_importance):
    print(f"{feat}: {imp:.2%}")

# 评估模型（使用AUC-ROC解决样本不平衡问题）
probabilities = rf.predict_proba(transactions)[:, 1]  # 预测欺诈概率
auc = roc_auc_score(fraud_labels, probabilities)
print("\n模型AUC-ROC评分:", f"{auc:.4f}")
```

### 关键代码解释

1. **数据标准化 (KNN示例)**

   python

   ```
   scaler = StandardScaler()
   scaled_data = scaler.fit_transform(data)
   ```

   - 解决特征量纲差异问题（如年龄和收入单位不同）
   - 避免数值大的特征主导距离计算

2. **文本特征提取 (朴素贝叶斯)**

   python

   ```
   vectorizer = CountVectorizer()
   X = vectorizer.fit_transform(emails)
   ```

   - 将文本转换为词频矩阵
   - 自动处理中文分词（需配合分词库）
   - 生成特征向量供模型使用

3. **决策树可视化**

   python

   ```
   export_graphviz(tree, out_file=None, feature_names=...)
   graphviz.Source(dot_data).render("tree")
   ```

   - 生成决策过程的图形化表示
   - 解释性强，适合医疗等需要透明决策的场景

4. **随机森林特征重要性**

   python

   ```
   rf.feature_importances_
   ```

   - 量化每个特征对预测的贡献度
   - 在金融风控中识别高风险特征（如大额夜间交易）

5. **AUC-ROC评估 (欺诈检测)**

   python

   ```
   roc_auc_score(fraud_labels, probabilities)
   ```

   - 解决样本不平衡问题（欺诈交易通常<1%）
   - 优于准确率，全面评估模型在不同阈值下的表现

这些代码展示了核心机器学习算法的实际应用，关键点在于：

1. 根据问题特性选择合适算法
2. 针对算法需求进行数据预处理
3. 使用领域相关的评估指标
4. 解释模型结果支持决策（如医疗诊断）