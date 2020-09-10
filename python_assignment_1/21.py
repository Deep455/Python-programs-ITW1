def spliting(arr,n):
    return [arr[i::n] for i in range(n)]
a=input("enter the elements of list seperated by commas : ").split(",")
arr=list(a)
n=int(input("enter size of splitted list u want to see :"))
print("list : ")
print(arr)
print("list after spliting : ")
print(spliting(arr,n))
