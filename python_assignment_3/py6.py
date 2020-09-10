num_line=0
x = open("test.txt",'r')
for line in x:
    num_line+=1
print("Number of lines in the file : "+str(num_line))