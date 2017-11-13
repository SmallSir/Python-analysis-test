import numpy as np
a = np.array([[0, 1, 2, 3, 4],[9, 8, 7, 6, 5]])
print(a.ndim)#表示秩，轴的数量或者维度数量
print(a.shape)#表示尺寸，n行m列
print(a.size)#元素个数，n*m
print(a.dtype)#元素类型
print(a.itemsize)#元素字节

a = np.arange(24).reshape((2,3,4))
print(a[1:4:2])
