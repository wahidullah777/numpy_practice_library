
# ndim mean n mean number or dim mean dimension mtlb humay ye baty ga kn si demension ha 1_d,2_d,3_d

import numpy as np
arry1_d=np.array([1,2,3,4])    # 1  dimension array
arry2_d=np.array([[1,2,3,4],   # 2  dimension array
                  [2,3,4,5]])
arry3_d=np.array([[[1,2,3,4],   # 3 dimension array
                  [2,3,4,5],
                  [6,7,8,9]]])



print(arry1_d.ndim) 
print(arry2_d.ndim)  # shape ma humay ye baty ga ky  2 rows and 4 colums ha
print(arry3_d.ndim) 