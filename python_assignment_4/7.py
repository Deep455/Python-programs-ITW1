class pro():
    def three_sum_zero(self,n,l):
        size=n
        lst=l
        new_lst=[]
        for i in range(size-2):
            for j in range(i+1,size-1):
                for k in range(j+1,size):
                    if lst[i]!=lst[j] and lst[j]!=lst[k] and lst[i]!=lst[k]:
                        if lst[i]+lst[j]+lst[k]==0:
                            new_lst.append([lst[i],lst[j],lst[k]])
        return new_lst

n=int(input("enter size of list : "))
x=[]
print("enter {} numbers : ".format(n))
for i in range(n):
    temp=int(input())
    x.append(temp)
print("entered list : ")
print(x)
print()
a=pro()
new_lst=a.three_sum_zero(n,x)
print("after execution new list : ")
print(new_lst)