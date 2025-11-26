import numpy as np
import pandas as pd

# 模拟温度区间 0 ~ 80℃
T = np.linspace(0, 80, 100)

# 模拟酶活性曲线 (高斯函数模型)
T_opt = 37   # 最适温度
rate = np.exp(-((T - T_opt)**2) / (2 * 10**2)) * 100  # 模拟反应速率

# 加入少量噪声
rate += np.random.normal(0, 2, len(rate))

# 生成 DataFrame
df = pd.DataFrame({'T': T, 'rate': rate})

# 保存为 CSV 文件
df.to_csv('enzyme_activity.csv', index=False)
print("✅ enzyme_activity.csv 已生成！")

