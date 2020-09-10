import pandas as pd
def store_list():
    print("---------------------------------------------------------------------------------------------------")
    print("            STORE LIST            ")
    store={'Item':['Chicken Strips','French Fries','Hamburger','Hotdog','Large Drink','Medium Drink','Milk Shake','Salad','Small Drink'],
    'Rate':['$3.50','$2.50','$4.00','$3.50','$1.75','$1.50','$2.25','$3.75','$1.25']}
    labels=['1','2','3','4','5','6','7','8','9']

    data=pd.DataFrame(store,labels)
    print(data)
    print("0\t To exit ")

    print("---------------------------------------------------------------------------------------------------")

def check(x,lst):        #to check wheather item already ordered or not
    for element in lst:
        if x==element:
            return 1,
    return 0

def item_name(x):
    Item=['Chicken Strips','French Fries','Hamburger','Hotdog','Large Drink','Medium Drink','Milk Shake','Salad','Small Drink']
    temp=Item[x-1]
    return temp

def rate_query(x):
    Rate=['$3.50','$2.50','$4.00','$3.50','$1.75','$1.50','$2.25','$3.75','$1.25']
    temp=Rate[x-1]
    return temp

def price_calculation(r,q):
    r=float(r[1:])
    p=r*q
    p='$'+str(p)
    return p

def total_calculation(p):
    t=float(0)
    for x in p:
        x=float(x[1:])
        t+=x
    t='$'+str(t)
    return t

lst,item,quantity,rate,price,label=[],[],[],[],[],[]
i=1
k=1
while k==1:
    store_list()
    string=input("Enter your orders : ")
    for x in string:
        x=int(x)
        if x==0:
            print("EXIT--As you pressed 0")
            exit()
        if check(x,lst)==0:
            lst.append(x)
            quantity.append(1)
            item.append(item_name(x))
            rate.append(rate_query(x))
            price.append(rate_query(x))
            label.append(i)
            i+=1
        else:
            quantity[lst.index(x)]+=1
            price[lst.index(x)]=price_calculation(rate[lst.index(x)],quantity[lst.index(x)])
    temp={'Item':item,'Quantity':quantity,'Rate':rate,'Price':price}
    orders=pd.DataFrame(temp,label)
    print()
    print("            YOUR ORDER            ")
    print()
    print(orders)
    total=total_calculation(price)
    print()
    print("\t\t Total Price  :   " + total)
    print()
    k=int(input("Do you want to order more (1-Yes/2-No) : "))