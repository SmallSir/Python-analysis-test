import numpy as np
a = np.arange(15).reshape(3,5)
#依次是和平均值，加权平均值，平均差，方差
print(np.sum(a))
print(np.mean(a,axis=1))
print(np.average(a,axis=0,weights=[10,5,1]))
print(np.std(a))
print(vars(a))