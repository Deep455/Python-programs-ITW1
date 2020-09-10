N=int(input("Enter size of A : "))
A=[]
print("Enter {} numbers : ".format(N))
for i in range(N):
    x=int(input())
    A.append(x)
K=int(input("Enter k : "))
ans=0
for i in range(N-2):
    game=True
    sub_A=[]
    sub_A.append(A[i])
    sub_A.append(A[i+1])
    max_element_of_sub_A=max(sub_A[0],sub_A[1])
    z=2
    while(z<=N-1):
        add=0
        for x in sub_A:
            add+=x
        
        if(len(sub_A)*max_element_of_sub_A-add<=K):
            if(ans<len(sub_A)):
                ans=len(sub_A)
            sub_A.append(A[z])
            max_element_of_sub_A=max(max_element_of_sub_A,A[z])
            z+=1
        else:
            break
        
print("Maximum possible length of subarray : ",ans)