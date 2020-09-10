import numpy as np
m=int(input("enter number of rows : "))
n=int(input("enter number of columns :"))
matrix=np.ndarray(shape=(m,n),dtype=int)
print("enter {} numbers : ".format(m*n))
for i in range(m):
    for j in range(n):
        matrix[i][j]=int(input())

print("entered matrix :")
print(matrix)
print()
diag=matrix.diagonal()
sum_diag=diag.sum()
print("sum of diagonal elements : " + str(sum_diag))
print()