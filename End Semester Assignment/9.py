string=input("Enter a string : ")
length=len(string)
for i in range(int(length/2)):
    if(string[i]!=string[length-1-i]):
        print("False (Not Palindrome)")
        exit(1)
print("True (Palindrome)")