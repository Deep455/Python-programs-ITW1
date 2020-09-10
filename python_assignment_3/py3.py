x = open("myfile.txt",'a')
string = input("enter a string : ")
x.write("\n"+string)
x.close()

x=open("myfile.txt",'r')
y=x.read()
print(y)
x.close()