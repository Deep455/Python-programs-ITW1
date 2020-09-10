from array import *
arr=array('i',[5,48,17,15,133,11,45])
print("existing array : "+str(arr))
temp=int(input("Enter the number u want to insert before second element in the array:"))
arr.insert(1,temp)
print("New array : "+str(arr))
