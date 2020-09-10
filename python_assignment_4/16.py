import numpy as np
import pandas as pd
lst1,lst2=[],[]
n=int(input("enter size of array : "))
print("enter {} integers for array-1 : ".format(n))
for i in range(n):
    temp=int(input())
    lst1.append(temp)
print("enter {} integers for array-2 : ".format(n))
for i in range(n):
    temp=int(input())
    lst2.append(temp)
add,sub,mul,div=[],[],[],[]

for i in range(n):
    add.append(lst1[i]+lst2[i])
    sub.append(lst1[i]-lst2[i])
    mul.append(lst1[i]*lst2[i])
    div.append(lst1[i]/lst2[i])
arr=pd.Series([add,sub,mul,div])
print("add : ",arr[0])
print("subtract : ",arr[1])
print("multiply : ",arr[2])
print("divide : ",arr[3])