import numpy as np
arr=np.array([1,2,3,np.nan,5,np.nan,6,np.nan])  


arr2=print(np.nan_to_num(arr)) # default ha to 0 sa replace kar dye ga
print(arr2)



arr2=print(np.nan_to_num(arr,nan=10)) # agar koi value dyni ha jha misi ng hato wha pr nan=koi  bi value
print(arr2)