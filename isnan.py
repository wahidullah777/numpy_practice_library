import numpy as np
arr=np.array([1,2,3,np.nan,5,np.nan,6,np.nan])  # jha np.nan wha pr true a jye ga wo bty ga ye 
  # value missing ha    
print(np.isnan(arr))