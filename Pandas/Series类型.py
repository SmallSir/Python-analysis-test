import pandas as pd
# 数值索引
b = pd.Series([9,8,7,6,4],index = ['a','b','c','d','e'])
#字典索引
b = pd.Series({'a':9, 'b':-1, 'c':55},index=['c','a','e','j'])
#Series类型在运算中会自动对其不同索引的数据
print(b)
