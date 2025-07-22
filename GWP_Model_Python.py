import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义函数：水泥用量计算
def cement_content(fc, base=400, alpha=1.2):
    return base * (fc / 30.0) ** alpha

# 定义函数：GWP模型
def gwp_model(fc, cacs_ratio_percent, k1=0.93, k2=0.9):
    cement = cement_content(fc)
    cacs = cement * cacs_ratio_percent / 100.0
    gwp = k1 * (cement - cacs) - k2 * cacs
    return gwp

# 定义变量范围
fc_range = np.arange(30, 61, 1)  # MPa
cacs_range = np.arange(5, 26, 1)  # %

# 构建网格
FC, CACS = np.meshgrid(fc_range, cacs_range)

# 计算 GWP 值
GWP = gwp_model(FC, CACS)

# 绘制3D图
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(FC, CACS, GWP, cmap='viridis')

# 添加标签
ax.set_xlabel('Compressive Strength fc (MPa)')
ax.set_ylabel('CaCS Replacement Rate (%)')
ax.set_zlabel('GWP (kg CO₂-eq/m³)')
ax.set_title('GWP Surface vs. fc and CaCS Replacement')

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.tight_layout()
plt.show()