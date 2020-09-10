num_lines = 0
with open("test.txt", 'r') as f:
    for line in f:
        num_lines += 1

x=open("test.txt",'r')
n=int(input("enter number of lines you want to see : "))
if n<=num_lines and n>=1:
    y=x.readline()
    for i in range(n):
        print(y,end="")
        y=x.readline()
else:
    print("input is wrong as there are only " + str(num_lines) + " lines in the file")
x.close()