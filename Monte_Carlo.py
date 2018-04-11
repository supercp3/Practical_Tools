import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle 
'''
蒙特卡洛方法来计算圆周率
精髓：用统计值来近似真实值
'''
#投点次数
n=10000
#圆的信息
r=1.0 #半径
a,b=(0.,0.) #圆心

#正方形区域边界
x_min,x_max=a-r,a+r
y_min,y_max=b-r,b+r

x=np.random.uniform(x_min,x_max,n)
y=np.random.uniform(y_min,y_max,n)

#计算点到圆心的距离
d=np.sqrt((x-a)**2+(y-b)**2)

#统计落在圆内的点的数目
res=sum(np.where(d<r,1,0))
pi=4*res/n
print('pi:',pi)
#画图表示
fig=plt.figure()
axes=fig.add_subplot(1,1,1)
axes.plot(x,y,'ro',markersize=1)
plt.axis('equal')

circle=Circle(xy=(a,b),radius=r,alpha=0.5)
axes.add_patch(circle)

plt.show()