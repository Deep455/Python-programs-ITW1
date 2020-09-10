num_line = 0
with open("test.txt",) as f:
    for line in f:
        num_line += 1

x=open("test.txt",'r')
n=int(input("enter number of lines you want to see from bottom : "))
y=x.readline()
for i in range(1,num_line+1,1):
    if i>num_line-n:
        print(y,end="")
    y=x.readline()

x.close()