
# broadcasting basically ye hota ha hum na 2d arry ko 1d array ka saat plus karna ha to hum mathmeticall opertion perform karty ha 
# agar ye n ho to broadcasting ni ho gyi  



import numpy as np
price=np.array([200,300,400,500,600,700])
dicount =10

new_price=price-(price*dicount/100)
print(new_price)
