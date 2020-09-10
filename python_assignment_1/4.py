def inserting(string,word):
	l=len(string)
	l=l//2
	new_string=string[:l]+word+string[l:]
	return new_string
string=input("enter a string : ")
word=input("enter a word u want to insert : ")
new_string=inserting(string,word)
print(new_string)
