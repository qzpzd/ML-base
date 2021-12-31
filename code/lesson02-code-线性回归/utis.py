from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x, y = make_blobs(n_features=2, n_samples=100, centers=3, random_state=2021, cluster_std=[0.6,0.7,0.5] )
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.title(u"原始数据分布")
plt.show()