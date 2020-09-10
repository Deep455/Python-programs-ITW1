def sorting(lst): 
    if len(lst) >1: 
        mid = len(lst)//2 
        L = lst[:mid]   
        R = lst[mid:]
  
        sorting(L) 
        sorting(R)
        
        i,j,k=0,0,0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                lst[k] = L[i] 
                i=i+1
            else: 
                lst[k] = R[j] 
                j=j+1
            k=k+1
          
        while i < len(L): 
            lst[k] = L[i] 
            i,k=i+1,k+1

        while j < len(R): 
            lst[k] = R[j] 
            j,k=j+1,k+1
    return lst
  
n = int(input("enter size of list : " ))
lst=[]
print("enter elements of list : ")
for i in range(n):
    element = int(input())
    lst.append(element)
print("initially lsit : ")
print(lst)
lst = sorting(lst)
print("After sorting : ")
print(lst)