n=int(input("enter size of list : "))
lst=[]
print("enter elements of list : ")
for i in range(n):
    temp = input()
    lst.append(temp)
print("input list : ")
print(lst)
x=0
for temp in list(lst):
    if temp[0] == "(":
        break
    x=x+1
print("elements before tuple - {}".format(x))