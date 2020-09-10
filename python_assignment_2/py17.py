string = input("enter a string : ")
lst = string.split(" ")
n = len(lst)
mid = n//2
for i in range(mid):
    temp = lst[i]
    lst[i] = lst[n-1-i]
    lst[n-1-i] = temp
newstring = ""
for element in lst:
    newstring = newstring + element + " "
string = newstring
print("updated string : ")
print(string)