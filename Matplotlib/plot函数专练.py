import numpy as np
import matplotlib.pyplot as plt
import  matplotlib


a = np.arange(0.0,5.0 ,0.02)
plt.xlabel('横轴：时间',fontproperties = 'SimHei',fontsize = 20)
plt.ylabel('纵轴:振幅',fontproperties = 'SimHei',fontsize = 20)
plt.plot(a, np.cos(2*np.pi * a),'r--')
plt.show()





'''
a = np.arange(10)
plt.plot(a, a*1.5,'b-', a, a*0.5,'--' ,a,a*5.5,'go-')#绘制多条曲线#format_string,在'   '之间添加所有控制曲线格式的因素
plt.show()
'''



