x=open("file1.txt",'r')
y=open("file2.txt",'r')
z=open("file3.txt",'w')

a=x.read()
b=y.read()
a=a.split("\n")
b=b.split("\n")
i,j=0,0
while i<len(a) and i<len(b):
    z.write(a[i]+"\n")
    z.write(b[i]+"\n")
    i+=1
if len(a)>len(b):
    temp=a
else:
    temp=b
while i<len(temp):
    z.write(temp[i]+"\n")
    i+=1

x.close()
y.close()
z.close()

print("\n \n file1.txt and file2.txt is written in file3.txt according to given condition \n \n ")