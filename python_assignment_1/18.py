a=[]
n=int(input("enter size of list : "))
for i in range(n):
    a.append([])
for i in range(n):
    print("enter size of list "+str(i+1)+" : ")
    x=int(input())
    print("enter elements of list "+str(i+1)+" : ")
    for j in range(x):
        a[i].append(int(input()))
maximum,index=0,0
for i in range(n):
    s=0
    for j in a[i]:
        s=s+j
    if(s>maximum):
        maximum=s
        index=i
print("list with highest sum is : ")
print(a[index])
