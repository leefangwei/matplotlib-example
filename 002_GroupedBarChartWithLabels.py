'''
带标签的分组条形图

条形图对于可视化计数或带有错误栏的汇总统计信息非常有用。
此示例显示了使用Matplotlib创建分组条形图的方法，以及如何使用标签注释条形图。
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

men_means, men_std = (20,35,30,35,27), (2,3,4,1,2)
women_means, women_std = (25,32,30,20,25), (3,5,2,3,2)

ind = np.arange(len(men_means)) # # the x locations for the groups
width = 0.35 # the width of the bars

fig, ax = plt.subplots() # 创建一个图形和一组子图。
rects1 = ax.bar(ind - width/2, men_means, width,yerr=men_std, label="men")
rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,label="women")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Scores")
ax.set_title("Scores by group and gender")
ax.set_xticks(ind)
ax.set_xticklabels(("G1","G2","G3","G4","G5"))
ax.legend()

def autolabel(rects, xpos="center"):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate("{}".format(height),
        xy=(rect.get_x()+rect.get_width()/2,height),
        xytext=(offset[xpos]*3, 3), # use 3 points offset
        textcoords="offset points",# in both directions
        ha = ha[xpos],va="bottom")

autolabel(rects1, "left")
autolabel(rects2, "right")

fig.tight_layout()

plt.show()