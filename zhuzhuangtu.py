import matplotlib.pyplot as plt
import numpy as np

def draw_data(n, a, b, c, d, values, fig, plt, t, ticks):
    fig.add_subplot(2, 2, n)  # 设置子图
    x = np.arange(1, c, 1)  # 创建等差数组，开始，结束，步长
    y = values[d, a:b + 1]
    color = ["#CAE1FF", "#BCD2EE", "#A2B5CD"]
    plt.bar(x, y, width=0.5, color=color)  # 设置x坐标，条形的高度，颜色，宽度
    plt.title(t)
    plt.ylabel("生产总值（亿元）")
    plt.xticks(x, ticks) #设置刻度的名称
    return plt

res = np.load("gdp.npz", allow_pickle=True)
fig = plt.figure(figsize=(20, 12)) #调节图形大小，宽，高
plt.rcParams['font.sans-serif'] = 'SimHei' #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #设置正常显示字符
columns = res["columns"]
values = res["values"]
title1 = "2000年第一季度国民总值产业构成分布柱状图"
title2 = "2017年第一季度国民总值产业构成分布柱状图"
ticks1 = [tmp[:4] for tmp in columns[3:6]]
ticks2 = [tmp[:2] for tmp in columns[6:-1]]
draw_data(1, 3, 5, 4, 0, values, fig, plt, title1, ticks1)
draw_data(2, 3, 5, 4, 68, values, fig, plt, title2, ticks1)
draw_data(3, 6, 13, 9, 0, values, fig, plt, title1, ticks2)
draw_data(4, 6, 13, 9, 68, values, fig, plt, title2, ticks2)
plt.savefig("zhuzhuangtu.png")
plt.show()