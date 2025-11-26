import pandas as pd
import numpy as np

np.random.seed(42)

# 生成训练数据
x1_train = np.random.uniform(0, 10, 100)
x2_train = np.random.uniform(0, 10, 100)
score_train = 3 * x1_train + 2 * x2_train + np.random.normal(0, 3, 100)
y_train = (score_train > 25).astype(int)  # 阈值可调

train_df = pd.DataFrame({
    'x1': x1_train,
    'x2': x2_train,
    'y': y_train
})
train_df.to_csv('train.csv', index=False)
print("✅ 已生成 train.csv 文件")

# 生成测试数据
x1_test = np.random.uniform(0, 10, 30)
x2_test = np.random.uniform(0, 10, 30)
score_test = 3 * x1_test + 2 * x2_test + np.random.normal(0, 3, 30)
y_test = (score_test > 25).astype(int)

test_df = pd.DataFrame({
    'x1': x1_test,
    'x2': x2_test,
    'y': y_test
})
test_df.to_csv('test.csv', index=False)
print("✅ 已生成 test.csv 文件")
