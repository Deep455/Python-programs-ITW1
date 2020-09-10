from array import *
alphabets=array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
string=input("Enter the string:")
for i in range(len(string)):
       temp=ord(string[i])-97
       alphabets[temp]=alphabets[temp]+1
for i in range(26):
    if(alphabets[i]>1):
        print(chr(i+97),alphabets[i])
       



