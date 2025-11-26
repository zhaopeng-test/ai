import numpy as np
import pandas as pd

np.random.seed(42)

# 正常数据
x1_normal = np.random.normal(loc=50, scale=5, size=900)
x2_normal = np.random.normal(loc=50, scale=5, size=900)

# 异常数据
x1_anomaly = np.random.normal(loc=80, scale=5, size=10)
x2_anomaly = np.random.normal(loc=20, scale=5, size=10)

# 合并
x1 = np.concatenate([x1_normal, x1_anomaly])
x2 = np.concatenate([x2_normal, x2_anomaly])

# 构建 DataFrame
df = pd.DataFrame({'x1': x1, 'x2': x2})

# 打乱顺序
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# 保存为 CSV 文件
df.to_csv('anomaly_dataset_no_label.csv', index=False)

print("✅ 已生成 anomaly_dataset_no_label.csv 文件（仅包含 x1 和 x2）")
