from array import *
arr=array('i',[])
n=int(input("enter size of array : "))
for i in range(n):
    temp=int(input())
    arr.insert(i,temp)
print("array is : ")
print(arr)
print("after converting array in list form : ")
arr=list(arr)
print(arr)
