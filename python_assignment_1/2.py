string=input("enter a string : ")
temp=0
for i in range(len(string)):
	for j in range(i+1,len(string)):
		if string[i]==string[j]:
			string=string[:j]+'$'+string[j+1:]
			temp=1
	if temp==1:
		break
print(string)
