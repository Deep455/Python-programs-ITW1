class rectangle:
    length,width=0,0
    def area(self,l,w):
        self.length,self.width=l,w
        temp=self.length*self.width
        return temp

x=float(input("enter length of rectangle : "))
y=float(input("enter width of rectangle : "))

a=rectangle()
res=a.area(x,y)
print(res)