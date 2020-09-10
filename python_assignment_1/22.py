a=input("enter numbers in list seperated by commas:").split(",")
arr=[]
for i in a:
    arr.append(int(i))
print("list is : ")
print(arr)
print("Output:")
for i in arr:
    print(i,end="")
