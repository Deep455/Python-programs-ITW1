def quick_sort(lst,start,end):
    temp1,temp2=start,end
    if(start>=end):     # terminating condition for quick_sort
        return 0
    pivot=lst[start]
    while(start<end):
        while(lst[start]<pivot):
            start+=1
        while(lst[end]>pivot):
            end-=1
        if(start<end):
            lst[start],lst[end]=lst[end],lst[start]
        else:
            break
    pivot,lst[end]=lst[end],pivot
    quick_sort(lst,temp1,end-1)  # left side sort
    quick_sort(lst,end+1,temp2)  # right side sort

n=int(input("Enter number of elements : "))
lst=[]
print("Enter {} numbers".format(n))
for i in range(n):
    x=int(input())
    lst.append(x)
print("Given Data : ")
print(lst)
quick_sort(lst,0,n-1)
print("Sorted Data : ")
print(lst)