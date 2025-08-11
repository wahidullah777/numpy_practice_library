import numpy as np
arr =np.array([2,3,4,5,6,7,8])
print(arr[0])
print(arr[0:5])  # PRINT 0-4 INDEX ELEMENT
print(arr[0:6:2])  # (START : END : STEP)
  # method 1:
print(arr[0:-5])  # 0 WALA WASY HI AYE GA OR - WALY KO HUM TOTAL MA SA NIKAL JO AYE WHA TAK LY 
# GYE INDEX IS MA TOTAL AB 6 AND OR -5 TO 6-5 GARY TO 1 RHA JYE MTLB POSITIVE VALUE A GYI HA 0:1

#method 2
print(arr[0:len(arr)-5]) # same answer 


print(arr[::2])   # only to step hi ly gaa start or end pori arry hi lya ga 
print(arr[::-1])  # pori array ko reverse ka dye ga 