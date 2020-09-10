def rangoli(n):
    temp=n
    design=""
    for i in range(temp,0,-1):
        for j in range(i-1,0,-1):
            design+=" "
        for k in range(temp,i-1,-1):
            design+=chr(k+96)
        for l in range(i+1,temp+1,1):
            design+=chr(l+96)
        design+="\n"
    for i in range(1,temp,1):
        for j in range(i):
            design+=" "
        for k in range(temp,i,-1):
            design+=chr(k+96)
        for l in range(i+2,temp+1,1):
            design+=chr(l+96)
        design+="\n"
    print(design)
            
n=int(input("Enter the size of rangoli : "))
rangoli(n)