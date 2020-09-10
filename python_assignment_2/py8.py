n = int(input("enter size of set : "))
numbers = set()
print("enter elements of set : ")
for i in range(n):
    temp=int(input())
    numbers.add(temp)
temp=list(numbers)
minimum = temp[0]
maximum = temp[0]
for i in range(1,n,1):
    if temp[i] < minimum:
        minimum = temp[i]
    if temp[i] > maximum:
        maximum = temp[i]
print("minimum = {} and maximum = {}".format(minimum,maximum))