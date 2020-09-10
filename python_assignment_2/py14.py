n=int(input("enter size of list : "))
lst = []
print("enter elements : ")
for i in range(n):
    element = int(input())
    lst.append(element)
print("initially list : ")
print(lst)
for i in range(n-1):
    for j in range(n-1-i):
        if lst[j] > lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
print("after sorting : ")
print(lst)