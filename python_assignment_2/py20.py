import sys
string = input("enter a string : ")
x = sys.getsizeof(string)
print(x)
print("memory size of '"+string+"' is {} bytes".format(x))
