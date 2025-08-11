'''list1=[39.4,55.5,34.2,66.7]
total =0
for list2 in list1:
   total +=  list2

average = total/len(list1)
print(average)

# agar ak bara data set a jye to is ko handle karn list or loop ka lye bhot hi muhkil 
# isi lye numpy library ka used ka gia js ma hum special array ka used karty ha 
 
'''
import numpy as np  # import numpy sa humay koi loop used ni karn aparta hai b
list1=np.array([39.4,55.5,34.2,66.7]) # array ky lye hum () barket used karty ha 
average =np.mean(list1) 
print(average )

# numpy is lye behitar ha kuo ka is ma large amount of data ko haldle kia jta hai is ki speed
# bi bhot zyada hoti ha 2,mempry kaam lyta hai ,is ka ilwa is ka use machine learning ma ,data 
# scientist ma goole ma har jaga numpy ka use dkia jta hai 


