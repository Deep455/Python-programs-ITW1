# we have given four parameters id,subject,class-V,class-VI
temp = [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI': 82},
 {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
 {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}] 

print("initially we have : ")
print(temp)
for x in list(temp):
    k = (x['V'] + x['VI'])/2
    x.pop('V')
    x.pop('VI')
    x.update({'avg(V+VI)' : k})
print("After update we have : ")
print(temp)