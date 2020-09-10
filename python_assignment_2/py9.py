a = set()
m = int(input("enter size of set-1 : "))
for i in range(m):
    temp = input()
    a.add(temp)
b = set()
n = int(input("entter size of set-2 : "))
for i in range(n):
    temp = input()
    b.add(temp)
print("set-1 : ")
print(a)
print("set-2 : ")
print(b)

x = a-b
y = b-a

print("difference set1 - set2 : {}" .format(x))
print("difference set2 - set1 : {}" .format(y))

x = a.union(b)
y = a.intersection(b)

print("set1 Union set2 : {}".format(x))
print("set1 intersection set2 : {}".format(y))