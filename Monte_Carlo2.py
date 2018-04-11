import numpy as np 
import matplotlib.pyplot as plt 
'''
蒙特卡洛方法来求函数y=x^2在区间【0,1】内的定积分
'''
def f(x):
	return x**2

n=10000
x_min,x_max=0.0,1.0
y_min,y_max=0.0,1.0

x=np.random.uniform(x_min,x_max,n)
y=np.random.uniform(y_min,y_max,n)
#统计落在函数y=x^2图像下方的点的数目
res=sum(np.where(y<f(x),1,0))
integral=res/n
print("integral:",integral)
#画图
fig=plt.figure()
axes=fig.add_subplot(1,1,1)
axes.plot(x,y,'ro',markersize=1)
plt.axis('equal')
axes.plot(np.linspace(x_min,x_max,10), f(np.linspace(x_min, x_max, 10)), 'b-')

plt.show()
