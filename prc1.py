import os
from collections import Counter

data=os.listdir(r"test")#读取test文件夹下面的文件名字
x=[x.split(".")[0] for x in data]#文件名字进行分割
list1=[]
for i in x:
	path="test"+"\\"+i+".txt"#文件名连接
	with open(path) as f:
		list1.extend(f.read().split())
#print(list1)
count=Counter(list1)
for key,value in count.items():
	print(key+":",value)

