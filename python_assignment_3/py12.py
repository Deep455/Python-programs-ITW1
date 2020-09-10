lst = []
n=int(input("enter number of lines : "))
print("enter lines : ")
for i in range(n):
    temp = input()
    lst.append(temp.upper())
print("enter lines in uppercae : ")
for temp in lst:
    print(temp)