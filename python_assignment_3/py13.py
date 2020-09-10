x = open("test.txt")
y=x.read()
lst=y.splitlines()
print(len(lst))
for i in range(len(lst)):
    lst[i]=lst[i].split(" ")
    
print(lst)