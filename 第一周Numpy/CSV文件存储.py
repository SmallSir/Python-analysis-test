import numpy as np

#csv文件存储方式
a = np.arange(100).reshape(5,20)
b = np.savetxt('a.csv',a,fmt = '%d',delimiter = ',')
#csv文件读入
b = np.loadtxt('a.csv',delimiter=',')
#多维度
c = a.tofile("b.dat",sep=',',format='%d')
#文件读出
np.fromfile(frame,dtype=float,count=-1,sep='')