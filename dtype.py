import numpy as np
arry1_d=np.array(["wahid","ali","ahad"])    # string type

arry2_d=np.array([[1.2,2.45,3.65,4.3],   # 2  float type
                  [2.4,3.6,4.7,5.87]])

arry3_d=np.array([[[1,2,3,4],   # 3 integer type
                  [2,3,4,5],
                  [6,7,8,9]]])



print(arry1_d.dtype) 
print(arry2_d.dtype)  # is ma humay baty ga is ki  data type kn si ha  
print(arry3_d.dtype) 