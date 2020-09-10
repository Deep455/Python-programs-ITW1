def reverse(lst):
    rev_string=""
    temp=len(lst)-1
    while(temp>=0):
        rev_string+=lst[temp]
        rev_string+=" "
        temp-=1
    return rev_string

string=str(input("enter a string : "))
lst=string.split()
rev_string=reverse(lst)
print("Output : ")
print(rev_string)