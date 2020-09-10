import pickle
import pandas as pd
def start():
    print("----------------------------------------------------------------------------------------------")
    print("                   CODES                   ")
    print("1. Add_contact")
    print("2. Display_contact")
    print("3. Delete_contact")
    print("4. Modify_contact")
    print("5. Seach_contact")
    print("6. To_exit")
    print("----------------------------------------------------------------------------------------------")

name,phone,email=[],[],[]
filename="contacts.pickle"
while True:
    start()
    pickle_in=open(filename,'rb')
    try:    
        temp=pickle.load(pickle_in)
        name=temp[0]
        phone=temp[1]
        email=temp[2]
    except:
        pass
    pickle_in.close()

    x=int(input("Enter your code : "))
    if x==1:
        pickle_out=open(filename,'wb')
        name.append(input("enter name : "))
        phone.append(int(input("enter phone number : ")))
        email.append(input("enter email : "))
        print("Contact added")
        pickle.dump([name,phone,email],pickle_out)
        pickle_out.close()
    elif x==2:
        pickle_in=open(filename,'rb')
        try:
            temp=pickle.load(pickle_in)
            data=pd.DataFrame({'Name':temp[0],'Phone':temp[1],'Email':temp[2]})
            print(data)
        except:
            print("No contact in address book")
        pickle_in.close()
    elif x==3:
        pickle_out=open(filename,'wb')
        query_name=input("enter name whose contact you want to delete : ")
        try:
            i=name.index(query_name)
            name.pop(i)
            phone.pop(i)
            email.pop(i)
            print("Contact deleted")
        except:
            print("No contact with this name")
        pickle.dump([name,phone,email],pickle_out)
        pickle_out.close()
    elif x==4:
        pickle_out=open(filename,'wb')
        query_name=input("enter name whose contact you want to modify : ")
        try:
            i=name.index(query_name) 
            a=int(input("Do you want to change contact name (1-Yes/2-No) : "))
            if a==1:
                name[i]=input("enter new name : ")
            elif a==2:
                pass
            else:
                print("Wrong input")
            a=int(input("Do you want to change phone number (1-Yes/2-No) : "))
            if a==1:
                phone[i]=input("enter new phone number : ")
            elif a==2:
                pass
            else:
                print("Wrong input")
            a=int(input("Do you want to change contact email (1-Yes/2-No) : "))
            if a==1:
                email[i]=input("enter new email : ")
            elif a==2:
                pass
            else:
                print("Wrong input")
            print("Contact modified")
        except:
            print("No contact with this name")
        pickle.dump([name,phone,email],pickle_out)
        pickle_out.close()
    elif x==5:
        pickle_out=open(filename,'rb')
        query_name=input("enter name whose contact you want to search : ")
        try:
            i=name.index(query_name)
            print("Name : "+name[i])
            print("Phone number : "+str(phone[i]))
            print("Email : "+email[i])
        except:
            print("No contact with this name")
        pickle_out.close()
    elif x==6:
        exit()
    else:
        print("WRONG OUTPUT")