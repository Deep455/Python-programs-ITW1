a=input("enter the elements seperated by comma : ").split(",")
l=list(a)
arr=[]
for i in range(len(l)):
    c=0
    for j in range(i):
        if(l[i]==l[j]):
            c=c+1
    if(c==0):
        arr.append(l[i])
print("Entered list:")
print(l)
print("New list:")
print(arr)
