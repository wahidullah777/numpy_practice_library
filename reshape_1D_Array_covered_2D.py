
#reshape(rows,column)



import numpy as np
arr=np.array([20,30,40,50,60,70])
reshaped=arr.reshape(2,3)     # it retuen not copy only view return 
print(reshaped)


reshaped=arr.reshape(3,2)
print(reshaped)


reshaped=arr.reshape(6,1)
print(reshaped)