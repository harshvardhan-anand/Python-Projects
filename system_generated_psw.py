#!/usr/bin/env python
# coding: utf-8

# # ALGORITHM
# 1.take a name 
# 
# 2.take dob 
# 
# 3.take phone no.
# 
# 
# 
# 4.split phone number in step of 2 
# 
# 5.split name in 3 halves
# 
# 
# 
# 6.take date of dob 
# 
# 7.take second part of name 
# 
# 8.take second part of phone number
# 
# 9.catenate==>psw: date+name+phone_no 
# 
# 10.catenate==>usname: 1st_halves_name+3rd_halve_name
# 
# check number could not be entered in name
# if no. entered then say agent <number> is at rest 

# In[4]:





# In[1]:


#user input fuction
def user():
    
    #user name
    while True:
        try:
            name=input("Enter your name: ")
        except ValueError:
            print("Only characters")
            continue
        else:
            if len(name)<=2:
                print("Wrong input")
                continue
            elif name.isalpha()==False:
                print("Only characters are allowed")
                continue
            else:
                break
                
    #user favourite number
    fav = input('%s'%("Enter your favourite character: "))
    while len(fav)<2 or len(fav)>2:
        print("Give 2 characters\n")
        fav = input('%s'%("Enter your favourite character: "))
    
    #user phone number
    while True:
        try:
            phone=int(input("Enter your phone number: "))
        except ValueError:
            print("Wrong Input:")
        else:
            phone=str(phone)
            if len(phone)==10 and phone[0]!=0:
                break
            else:
                print("Wrong input")
                continue
                
    #catenating name 
    name=name.lower()
    name=name[0]+name[-2]
    name=name[::-1]
    #catenating phone
    phone=phone[3]+phone[4]+phone[5]
      
     #replcing with special character and reversing some
    name=name.replace('a','@')
    name=name.replace('1','!')
    name=name.replace('o','0')
    name=name.replace('h','#')
    name=name.replace('s','$')
    name=name.upper()
    fav=fav[::-1]
    phone=phone.replace("0","o")

    #password function
    from random import randint
    psw=name+str(randint(1,30))+fav+phone
    print(psw)
    import time
    time.sleep(30)
    
    


# In[2]:


user()


# In[ ]:





# In[ ]:




