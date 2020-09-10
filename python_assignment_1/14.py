from array import *
arr=array('i',[])
n=int(input("enter size of the array : "))
print("enter elements of array : ")
for i in range(n):
    temp=int(input())
    arr.insert(i,temp)
b=int(input("enter the number to find its frequency : "))
count=0
for i in arr:
    if(b==i):
        count=count+1
print(count)
