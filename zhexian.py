import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = 'simhei'#用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #设置正常显示字符
data = np.load('gdp.npz',allow_pickle=True) #读取文件
values = data['values']
pl = plt.figure(figsize=(10,15)) #调节图形大小，宽，高
ax = pl.add_subplot(2,1,1)#设置子图
plt.plot(values[:,0],values[:,3], '#FF0000',
         values[:,0],values[:,4], '#008000',
         values[:,0],values[:,5], '#0000FF')
plt.legend(['第一产业','第二产业','第三产业'])#设置图例
plt.xticks(range(1,73,4),values[range(0,70,4),1],rotation=45)
#1：ticks放置的地方,2：添加的标签，3：字体旋转角度
plt.ylabel('生产总值（亿元）')
plt.title('2000-2017各行业与各产业各季度国民生产总值折线图')
ax = pl.add_subplot(2,1,2)
plt.plot(values[:, 0], values[:, 6], '#FF0000',
         values[:, 0], values[:, 7], '#0000FF',
         values[:, 0], values[:, 8], '#FFFF00',
         values[:, 0], values[:, 9], '#008000',
         values[:, 0], values[:, 10], '#A0522D',
         values[:, 0], values[:, 11], '#FF4500',
         values[:, 0], values[:, 12], '#800000',
         values[:, 0], values[:, 13], '#808080',
         values[:, 0], values[:, 14], '#000000')
plt.legend(['农业', '工业', '建筑', '批发', '交通', '餐饮', '金融', '房地产', '其他'])
plt.xticks(range(1,73,4),values[range(0,70,4),1],rotation=45)
#1：ticks放置的地方,2：添加的标签，3：字体旋转角度
plt.savefig('zhexian.png')
plt.show()