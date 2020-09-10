import re
x=open("test.txt",'r')
y=x.read()
# splitting text on either " " or "\n"
lst=re.split(' |\n',y)

#  inserting empty tuple after every 10 elements
for i in range(10,len(lst),10):
    lst.insert(i,'()')
print("initially : ")
print(lst)

# now removing empty tuples
for x in lst:
    if x == '()':
        lst.remove(x)
print("After removing empty tuples : ")
print(lst)