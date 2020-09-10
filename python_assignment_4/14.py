import numpy as np
arr=[[1,2,3,4], ['Red', 'Green', 'White', 'Orange'], [12.20, 15.0, 20.0, 40.0]]
result= np.core.records.fromarrays([arr[0], arr[1], arr[2]],names='x,y,z')
for record in result:
    print(record)