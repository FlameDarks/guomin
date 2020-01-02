import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'simhei' #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #设置正常显示字符
data = np.load('gdp.npz',allow_pickle=True) #读取文件
values = data['values']
label = ['第一产业', '第二产业', '第三产业'] #定义饼状图的标签
explode = [0.05,0.05,0.05] #设置间隔
plt.pie(values[-1,3:6],labels=label,explode=explode,autopct='%.1f%%',
        shadow = True,pctdistance=0.8,colors=['#FF0000','#008000','#0000FF'])
#autopct，圆里面的文本格式
#shadow，饼是否有阴影
#pctdistance，百分比的text离圆心的距离
plt.title('2017年各产业占比饼图')
plt.savefig('bing.png')
plt.show()
