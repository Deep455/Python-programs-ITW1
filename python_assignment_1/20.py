from collections import Counter
a=input("enter elements of list-1 seperated by commas : ").split(",")
b=input("enter elements of list-2 seperated by commas : ").split(",")
x,y=list(a),list(b)
l1=Counter(x)
l2=Counter(y)
print("Output:")
print("List1-List2: ",list(l1-l2))
print("List2-List1: ",list(l2-1))
