def upper_case():
    string=input("Enter string : ")
    upper_string=""
    for i in range(len(string)):
        if(ord(string[i])>=97 and ord(string[i])<=122):
            upper_string+=chr(ord(string[i])-32)
        else:
            upper_string+=string[i]
x=1
while(x==1):
    upper_string=upper_case()
    print(upper_string)
    print("Do yo want to write more string :\n For Yes - press 1 \n For No - press 2")
    x=int(input("enter code : "))
    if(x==2):
        exit()
    elif(x!=1 and x!=2):
        print("Wrong code")