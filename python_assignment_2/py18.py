def reversing(string):
    n = len(string)
    newstring=""
    for i in range(n):
        newstring = newstring + string[n-1-i]
    return newstring

string = input("enter a string : ")
string = reversing(string)
print("updated string : {}".format(string))