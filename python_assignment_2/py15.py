n = int(input("enter size of list : "))
lst=[]
print("enter elements of list : ")
for i in range(n):
    element = int(input())
    lst.append(element)
print("initially list : ") 
print(lst)
for i in range(n):  
    x = i 

    for j in range(i+1,n,1): 
        if lst[j] < lst[x]: 
            x = j 

    temp = lst[i]
    lst[i] = lst[x]
    lst[x] = temp
    print(lst)

print ("After sorting : ") 
print(lst)