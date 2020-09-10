a=input("enter elements of list seperated by commas:").split(",")
x=list(a)
arr=[]
n=int(input("Enter the value of n : "))
for i in range(1,n+1,1):
    for j in x:
        arr.append(str(j)+str(i))
print("given list is : ")
print(x)
print("After concatenating : ")
print(arr)
