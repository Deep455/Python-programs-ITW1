n=int(input("enter size of dictionary : "))
lst1=[]
print("enter list-1 : ")
for i in range(n):
    lst1.append(input())
lst2=[]
print("enter list-2 : ")
for i in range(n):
    lst2.append(input())
dic={}
for i in range(n):
    dic.update({lst1[i]:lst2[i]})
print(dic)