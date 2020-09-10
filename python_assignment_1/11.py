def binary_to_decimal(binary_number):
    x=int(binary_number)
    i,sum=0,0
    while(i<4):
        r=x%10
        sum=sum+r*(2**i)
        x=x//10
        i=i+1
    return sum
a=input("Enter the binary numbers:")
a=a.split(",")
b=[]
for i in range(len(a)):
    x=binary_to_decimal(a[i])
    if(int(x)%5==0):
        b.append(a[i])
for i in range(len(b)-1):
    print(b[i],end=',')
print(b[-1])

