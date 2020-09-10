lst = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print("initially we have : ")
print(lst)
for x in list(lst):
    if len(x) == 0 :
        lst.remove(x)
print("Afte update we have : ")
print(lst)