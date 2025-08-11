


import numpy as np

arr=np.array([1,2,3,np.inf,5,-np.inf,6,np.inf])  # jha np.inf wha pr true a jye ga wo bty ga ye 
  # value infinite hai  
print(np.isinf(arr))



arr2=np.nan_to_num(arr,posinf=100,neginf=200)  
print(arr2)
