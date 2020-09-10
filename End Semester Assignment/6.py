def triangle(n):
    tri=""
    for i in range(1,n):
        for j in range(i):
            tri+=str(i)
        tri+="\n"
    print(tri)
n=int(input("Enter a number : "))
triangle(n)