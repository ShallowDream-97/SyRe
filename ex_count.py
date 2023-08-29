import matplotlib.pyplot as plt

# 示例数据
y = [5, 22, 15, 40, 37, 23, 45, 12, 5, 30, 42, 55, 20, 15, 52]

# 使用plt.hist()创建直方图
# bins参数定义了你想要的"箱子"或范围的数量。
# 例如，如果你想要每10个单位一个范围，可以使用range和步进来定义这些箱子。
plt.hist(y, bins=range(0, 61, 10), edgecolor="k", align='left')

plt.xlabel('Range')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
