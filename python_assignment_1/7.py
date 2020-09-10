def pascal_triangle(rows):
    a=[]
    for i in range(rows):
    	a.append([])
    	a[i].append(1)
    	for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
    	if(rows!=0):
            a[i].append(1)
    for i in range(rows):
    	print(" "*(rows-i-1),end="",sep="")
    	for j in range(0,i+1):
            print(a[i][j],end=" ")
    	print()
rows=int(input("Enter number of rows:"))
pascal_triangle(rows)
