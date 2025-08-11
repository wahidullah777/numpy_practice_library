import numpy as np


arry2_d=np.array([[1.2,2.45,3.65,4.3],   # 2  float type
                  [2.4,3.6,4.7,5.87]])
print(arry2_d.dtype)
int_arry=arry2_d.astype(int)
print(int_arry.dtype)



