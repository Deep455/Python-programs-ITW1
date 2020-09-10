lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'), ('item4', '11.3'), ('item5', '57.3'), ('item6', '38.9'), ('item7', '73.2'), ('item8', '22.1')]
print("initially we have : ")
print(lst)
for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j][1] > lst[j+1][1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
print("After update we have : ")
print(lst)