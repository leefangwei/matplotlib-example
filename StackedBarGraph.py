'''
堆积条形图
'''

import numpy as np # 维度数组与矩阵运算的数学函数库
import matplotlib.pyplot as plt # 对于简单的绘图，pyplot模块提供类似MATLAB的接口

N = 5
menMeans = (20,35,30,35,27)
womenMeans = (25,32,34,20,25)
menStd = (2,3,4,1,2)
womenStd = (3,5,2,3,3)
ind = np.arange(N) #坐标的x轴
width = 0.35 # 条形大小

p1 = plt.bar(ind,menMeans,width,yerr=menStd)
p2 = plt.bar(ind, womenMeans,width,bottom=menMeans,yerr=womenStd)

plt.ylabel("Scores")
plt.title("Scores by group and gender")
plt.xticks(ind,("G1","G2","G3","G4","G5"))
plt.yticks(np.arange(0,81,10)) # 起始：0，截至：81，间隔：10
plt.legend((p1[0],p2[0]),("men","women")) # 条形和对应的名称

plt.show()