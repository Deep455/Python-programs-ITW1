a = {'key1': 1, 'key2': 3, 'key3': 2}
b = {'key1': 1, 'key2': 2}
for (key, value) in set(a.items()) & set(b.items()):
   temp = "{} : {} is present in both dictionaries".format(key,value)
   print(temp)