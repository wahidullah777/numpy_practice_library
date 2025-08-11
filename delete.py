
'''
import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr)
new_arr=np.delete(arr,2)   # insert (orignal array  ,  index num  )
print(new_arr)
'''
import numpy as np
rr=np.array([[1,2],
             [5,6]])
print(rr)
new_arr1=np.delete(rr,1,axis=0)   # insert (orignal array  ,  index num   ,  [value,value] )
print(new_arr1)


new_arr2=np.delete(rr,1,axis=0)   # axis=1 mean x axis,,axis=0 mean y axis 
print(new_arr2)
