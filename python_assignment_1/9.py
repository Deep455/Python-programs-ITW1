def sorting(array1,array2,m,n):
    resulting_array=[None]*(m+n)
    i,j,k=0,0,0
    while(i<m and j<n):
        if(array1[i]<array2[j]):
            resulting_array[k]=array1[i]
            k,i=k+1,i+1
        else:
            resulting_array[k]=array2[j]
            k,j=k+1,j+1
    while(i<m):
        resuting_array[k]=array1[i]
        k,i=k+1,i+1
    while(j<n):
        resulting_array[k]=array2[j]
        k,j=k+1,j+1
    print("Output:")
    print(resulting_array)
m=int(input("Enter number of elements in array1:"))
array1=[]
print("Enter element of array 1 : ")
for i in range(m):
    array1.append(int(input()))
n=int(input("Enter number of elements in array2:"))
array2=[]
print("Enter elements of array 2 :")
for i in range(n):
    array2.append(int(input()))
sorting(array1,array2,m,n)
