import numpy as np
import matplotlib.pyplot as plt

a = np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2 * np.pi * a),'r--')

plt.xlabel('横轴: 时间',fontproperties = 'SimHei',fontsize = 15,color = 'green')
plt.ylabel('纵轴: 振幅',fontproperties = 'SimHei',fontsize = 15)
plt.title(r'正弦波实例 $y=cos(2\pi x)$',fontproperties = 'SimHei',fontsize = 25)   #添加文本标题
plt.text(2,1,r'$\mu = 100$',fontsize = 15)   #在任意位置添加信息
plt.axis([-1,6,-2,2])
plt.grid(True)#添加网状格子
plt.show()