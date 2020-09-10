import re
x = open("test.txt", 'r') 
y=x.read()
dictionary = dict() 
lst=re.split(' |\n',y) 
for word in lst: 
    if word in dictionary: 
        dictionary[word] = dictionary[word] + 1
    else:  
        dictionary[word] = 1
   
for key in list(dictionary.keys()): 
    print(key, ":", dictionary[key])