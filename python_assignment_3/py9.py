lst=['blue','green','orange','purple','black','violet']
x = open("new.txt",'w')
for element in lst:
    x.write(element+"\n")
x.close()
print("\n \n list is written in new.txt file \n \n")