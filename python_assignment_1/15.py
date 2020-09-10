from array import *
arr=array('i',[])
n=int(input("enter size of array : "))
print("enter elements of array : ")
for i in range(n):
    temp=int(input())
    arr.insert(i,temp)
print("array is : ")
print(arr)
x=int(input("enter index of element u want to remove : "))
arr.remove(arr[x])
print("new array : ")
print(arr)
