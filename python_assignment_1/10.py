def program(string):
    lower_case,upper_case=0,0
    for i in range(len(string)):
             if((ord(string[i])>=97)and(ord(string[i])<=122)):
                   lower_case=lower_case+1
             elif((ord(string[i])>=65)and(ord(string[i])<=90)):
                   upper_case=upper_case+1
    print("Number of Lower case characters : ",lower_case)
    print("Number of Upper case characters : ",upper_case)
string=input("Enter the string:")
program(string)
