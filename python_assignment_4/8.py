class pro:
    def target_sum(self,size,l,target):
        
        for i in range(size-1):
            for j in range(i+1,size):
                if l[i]+l[j]==k:
                    print(i,j)

import array as arr
n=int(input("enter size of arrary "))
lst=[]
print("enter {} numbers : ".format(n))
for i in range(n):
    temp=int(input())
    lst.append(temp)
x=arr.array('i',lst)
k=int(input("enter target sum : "))

a=pro()
a.target_sum(n,x,k)