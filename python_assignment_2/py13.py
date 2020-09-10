
def binarysearch (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid  
        elif arr[mid] > x: 
            return binarysearch(arr, l, mid-1, x) 
  
        else: 
            return binarysearch(arr, mid + 1, r, x) 
    else: 
        return -1

n = int(input("enter size of list : "))
a = []

print("enter numbers in increasing order : ")
for i in range(n):
    temp = int(input())
    a.append(temp)

x = int(input("enter number you want to search : "))

position = binarysearch(a, 0, len(a)-1, x)
index = position - 1
  
if position != -1: 
    print ("{} found at index {}".format(x,index)) 
else: 
    print ("{} not found".format(x))