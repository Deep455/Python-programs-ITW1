a=input("Enter elements in list-1 seperated by commas : ").split(",")
b=input("Enter elements in list-2 seperated by commas : ").split(",")
l1=list(a)
l2=list(b)
for (a,b) in zip(l1,l2):
    print(a,b)
