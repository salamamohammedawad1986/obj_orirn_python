import pandas as pd
import numpy as np


num = np.arange(5,52,3)
print('Numbers is :  ',num)

# How to find odd and even number:
for i in num:
    if(i %2) == 0:
        print('Even No: ', i)
    else:
        print('Odd No: ',i)    
        
        