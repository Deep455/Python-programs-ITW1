import numpy as np
n=int(input("enter size of array : "))
original_arr=np.ndarray(shape=(n),dtype=int)
print("enter {} integers : ".format(n))
for i in range(n):
    x=int(input())
    original_arr[i]=x
print()
print("original array : ")
print(original_arr)
print()
another_arr=np.ndarray(shape=n,dtype=int)
for i in range(n):
    if i==0:
        another_arr[i]=0
    elif i==4:
        another_arr[i]=40
    else:
        another_arr[i]=original_arr[i]
print("another array : ")
print(another_arr)
print()