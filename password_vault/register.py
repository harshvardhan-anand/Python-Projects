import base64
from random import shuffle
def register():
    #reading user name
    while True:
        try:
            name=input("Enter your name: ")
        except ValueError:
            pass
        else:
            if name.isalpha()==False:
                print("Only characters are allowed")
                continue
            elif len(name)<3:
                print("Name can't be less than 3 characters")
                continue
            else:
                break
    #reading user phone number
    while True:
        try:
            phone=int(input("Enter your phone number: "))
        except ValueError:
            print("Only numbers are allowed")
            continue
        else:
            #phone in string format
            phone=str(phone)
            if len(phone)==10:
                print("\n You have successfully registered!")
                break
            else:
                print("Wrong input")
                continue
                
    #shuffling
    name=list(name)
    phone=list(phone)
    shuffle(name)
    shuffle(phone)
    
    #revercing and catenating
    name=name[::-1]
    name=name[1]+name[-1]
    print(type(name))
    phone=phone[3]+phone[4]+phone[7]
    
    #saving to name
    name=name+phone
    #encoding
    name=base64.b64encode(bytes(name,'utf-8'))
    #returning
    return name
   

#this fuction will be passed as parameter for servicefile module