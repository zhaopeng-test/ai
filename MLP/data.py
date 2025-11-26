import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子以确保结果可重现
np.random.seed(42)

# 生成数据点数量
n_samples = 1000

# 生成特征数据
x1 = np.random.uniform(-5, 5, n_samples)
x2 = np.random.uniform(-5, 5, n_samples)

# 创建非线性决策边界：使用圆形边界
# 计算每个点到原点的距离
distance = np.sqrt(x1**2 + x2**2)

# 创建非线性分类：内部圆为一类，外部圆为另一类
# 添加一些噪声使边界不那么完美
y = np.where(distance + np.random.normal(0, 0.5, n_samples) < 3, 1, 0)

# 创建DataFrame
data = pd.DataFrame({
    'x1': x1,
    'x2': x2,
    'y': y
})

# 保存为CSV文件
data.to_csv('data.csv', index=False)

print("data.csv 文件已生成成功！")
print(f"数据集形状: {data.shape}")
print("\n前5行数据:")
print(data.head())
print("\n标签分布:")
print(data['y'].value_counts())
