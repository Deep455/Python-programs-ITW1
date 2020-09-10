import numpy as np
m=int(input("enter number of rows : "))
n=int(input("enter number of columns : "))
matrix=np.ndarray(shape=(m,n),dtype=int)
for i in range(m):
    for j in range(n):
        if i==0 or i==m-1 or j==0 or j==n-1:
            matrix[i][j]=1
        else:
            matrix[i][j]=0
print("matrix : ")
print(matrix)