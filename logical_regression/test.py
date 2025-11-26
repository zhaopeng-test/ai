import pandas as pd
import numpy as np

# 设置随机种子以保证结果可重现
np.random.seed(42)

# 生成样本数据
n_samples = 1000

# 生成两个考试分数 (exam1, exam1_2)，范围在0-100之间
exam1 = np.random.normal(65, 15, n_samples)
exam1_2 = np.random.normal(70, 12, n_samples)

# 确保分数在0-100范围内
exam1 = np.clip(exam1, 0, 100)
exam1_2 = np.clip(exam1_2, 0, 100)

# 生成通过指标 - 严格执行两个考试都超过60分才通过
pass_indicator = []
for i in range(n_samples):
    if exam1[i] > 60 and exam1_2[i] > 60:
        pass_indicator.append(1)  # 两个都超过60分，通过
    else:
        pass_indicator.append(0)  # 其他情况，不通过

# 创建DataFrame
data = pd.DataFrame({
    'exam1': exam1,
    'exam1_2': exam1_2,
    'pass': pass_indicator
})

# 保存到CSV文件
data.to_csv('exam_pass_prediction.csv', index=False)

# 显示数据的基本统计信息
print("数据基本信息:")
print(f"总样本数: {len(data)}")
print("\n数据描述性统计:")
print(data.describe())
print("\n通过率统计:")
print(f"总通过率: {data['pass'].mean():.2%}")

print("\n按分数区间统计:")
print("两个考试都>60分的情况:")
both_pass_condition = (data['exam1'] > 60) & (data['exam1_2'] > 60)
print(f"人数: {both_pass_condition.sum()}")
print(f"通过率: {data[both_pass_condition]['pass'].mean():.2%}")

print("\n只有一个考试>60分的情况:")
one_pass_condition = ((data['exam1'] > 60) & (data['exam1_2'] <= 60)) | ((data['exam1'] <= 60) & (data['exam1_2'] > 60))
print(f"人数: {one_pass_condition.sum()}")
print(f"通过率: {data[one_pass_condition]['pass'].mean():.2%}")

print("\n两个考试都<=60分的情况:")
both_fail_condition = (data['exam1'] <= 60) & (data['exam1_2'] <= 60)
print(f"人数: {both_fail_condition.sum()}")
print(f"通过率: {data[both_fail_condition]['pass'].mean():.2%}")

# 显示前几行数据
print("\n前10行数据:")
print(data.head(10))

# 显示一些边界情况的例子
print("\n边界情况示例 (分数接近60分):")
boundary_cases = data[
    ((data['exam1'] >= 55) & (data['exam1'] <= 65)) & 
    ((data['exam1_2'] >= 55) & (data['exam1_2'] <= 65))
].head(10)
print(boundary_cases)