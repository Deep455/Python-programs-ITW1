n=int(input("size of list : "))
a=[]
print("enter elements of list : ")
for i in range(n):
    temp=str(input())
    a.append(temp)
print("entered list is:")
print(a)
string=input("enter string : ")
for i in range(len(a)):
    a[i]=str(string)+str(a[i])
print("after adding list is :")
print(a)
