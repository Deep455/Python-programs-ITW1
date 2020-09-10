import numpy as np
import math
n=int(input("enter number of angles : "))
lst=[]
print("enter {} angles in degree : ".format(n))
for i in range(n):
    temp=float(input())
    lst.append(temp)

print("Angles entered : ")
print(lst)
print()

sin_lst=np.ndarray(shape=n, dtype=float)
cos_lst=np.ndarray(shape=n, dtype=float)
tan_lst=np.ndarray(shape=n, dtype=float)
for i in range(n):
    sin_lst[i]=math.sin(math.radians(lst[i]))
    cos_lst[i]=math.cos(math.radians(lst[i]))
    tan_lst[i]=math.tan(math.radians(lst[i]))
print("sine of given array : ")
print(sin_lst)
print()
print("cosine of given array : ")
print(cos_lst)
print()
print("tangent of given array : ")
print(tan_lst)
print()