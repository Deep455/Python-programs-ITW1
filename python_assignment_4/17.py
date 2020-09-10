import numpy as np
import pandas as pd

n=int(input("enter size of array : "))
arr=np.ndarray(shape=(n),dtype=int)
print("enter {} integers : ".format(n))
for i in range(n):
    arr[i]=int(input())
data=pd.Series(arr)
print(data)