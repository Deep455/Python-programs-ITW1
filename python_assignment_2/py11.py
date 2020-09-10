def harmonic(n):
    sum = 0
    for i in range(n):
        sum = sum + (1/(i+1))
    return sum

n=int(input("enter number upto which you want to see harmonic sum : "))
sum = harmonic(n)
print(sum)