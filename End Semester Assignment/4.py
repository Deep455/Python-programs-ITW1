string=input("Enter the string : ")
w=int(input("Enter the width : "))
lst=[]
i=0
while(i<len(string)):
    lst.append(string[i:i+w])
    i+=w
print("Output 1 : ")
for x in lst:
    print(x)
print("Output 2 : ")
for x in lst:
    print(x[0]+x[-1])