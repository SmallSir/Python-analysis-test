import matplotlib.pyplot as plt
import numpy as np
'''
plt.plot([0,2,4,6,8],[3,1,4,5,2])#先x后y
plt.ylabel("次数")
plt.axis([-1,10,0,6])#x坐标起始于-1终止与10，y坐标起始于0，终止为6
plt.savefig('test',dpi = 600)#在当前文件下图像保存以png格式下名字叫做test，600像素
plt.show()#展示
'''
def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)
a = np.arange(0.0, 5.0 ,0.02)
plt.subplot(2, 1, 1)#将图像用两行一列分割开来，用上面的部分
plt.plot(a,f(a))
plt.subplot(2,1,2)
plt.plot(a, np.cos(2*np.pi*f(a)),'r--')
plt.show()