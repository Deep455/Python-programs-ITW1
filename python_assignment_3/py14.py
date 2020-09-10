import os
import shutil
x=os.getcwd()
print("\n")
print("path = "+x)

os.mkdir("newdir")
print("\n A. new directory created")

y=open(x+"\\newdir\\newfile.txt",'w')
y.close()
print("\n B. new text file created")

shutil.rmtree("newdir")
print("\n C. directory deleted \n")