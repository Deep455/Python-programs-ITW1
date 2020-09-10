class convertor:
    def hexa_to_deci(hexa):
        deci=0
        for i in range(len(hexa)):
            x=hexa[-i-1]
            if ord(x)>=48 and ord(x)<=57:
                temp=int(x)
                deci+=temp*(16**i)
            elif ord(x)>=65 and ord(x)<=70:
                temp=ord(x)-55
                deci+=temp*(16**i)
            else:
                print("Wrong input")
                exit()
        return deci

hexa=input("input hexadecimal number : ")
deci=convertor.hexa_to_deci(hexa)
print(deci)