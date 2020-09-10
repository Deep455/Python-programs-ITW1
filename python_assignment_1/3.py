string=input("enter a string : ")
result1=string.find('not')
result2=string.find('poor')
if (result1 != -1) and (result2 != -1):
	string=string[:result1]+'good'+string[result2+4:]
print(string)
