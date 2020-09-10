def sorting(string):
    order=string.split()
    order.sort()
    for i in order:
        print(i)
string=input("Enter the string:")
sorting(string)
