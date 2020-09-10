def sum(arr,size):
   if (size == 0):
     return 0
   else:
     return arr[size-1] + sum(arr,size-1)
n=int(input("Enter size of list:"))
a=[]
print("enter elements of list : ")
for i in range(n):
    temp=int(input())
    a.append(temp)
print("The list is : ")
print(a)
print("Sum of items in list : {}".format(sum(a,n)))