arr=[]
width=3
temp=[]
for x in range(10,34,1):
    temp.append(x)
    if(len(temp)==width):
        arr.append(temp)
        temp=[]
print("8x3 array : ")
print(arr)

new_arr=[]
sub_width=int(len(arr)/4)
temp=[]
for x in arr:
    temp.append(x)
    if(len(temp)==sub_width):
        new_arr.append(temp)
        temp=[]
print("Dividing 8x3 array into 4 sub-arrays : ")
print(new_arr)

