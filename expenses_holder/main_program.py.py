#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
import time
yest=0       #global variable used to switch between yestarday expenses_w to today expenses_w
now=datetime.datetime.now()
filename=datetime.datetime.now().strftime("%d-%b-%y")

def input_fn():   #taking input from user
    item=input("Item: ")
    if item=='...':
        cost=None
        return item, cost
    while True:
        try:
            cost=input(f"Cost of {item}: ")
            if cost == '...':
                    item=None
                    return item, cost

            else:
                cost=int(cost)
        except ValueError:
            print('Cost is always an integer')
        else:
            return item, cost
        

def log():    #writing logs
    with open('log.txt', 'w') as loged:
        loged.write(now.strftime('%d-%b-%y :: %H-%M-%S'))

def expenses_w(filename):   #for writing
    log()
    total_e=0
    with open(filename +'.txt', 'w') as file:
        file.write('This is your expenses for date '+filename+'\n\n')
        print("Press period thrice(...) to exit\n")
        while True:
            item, cost=input_fn()
            if item==None or cost==None:
                file.write(f"\nYour total expenses is Rs {total_e}")
                break
            if (item != None) and (cost != None):
                total_e=cost+total_e
                file.write(item+' : '+str(cost)+'\n')
    print('_____________________________________')
    print(f"\nYour total expenses is {total_e}")
            
def expenses_r():   #for reading
    i=0
    while i!=3:
        try:
            filename=input("Enter the day in format of dd-month-yy: ")
            with open(filename+'.txt', 'r') as file:
                read_file=file.read()
            print('\n'+read_file)
        except FileNotFoundError:
            print("Oops! It seems that either file does not exits or please retry in correct format.")
            if i==2:
                print(f"File does not found ==> times checked: {i+1}\n")
                break
            i+=1
            continue
        else:
            break
            
def check(filename):   #run check at particular time
    
    try:
        with open("log.txt", 'r') as log:
            log_data=log.read()
    except:
        pass
    
        
    try:
        x=int(log_data[:2])   #this can create error if log file is modified
        y=int(filename[:2])
        if(y-x)==2:
            i=0
            while i<3:
                o=input("You have not given your expenses yestarday. Do you want to give(Y/N): ")
                if o.lower()=='y':
                    yest_filename=datetime.datetime.now()-datetime.timedelta(days=1)
                    yest_filename=yest_filename.strftime("%d-%b-%y")
                    global yest
                    yest=1
                    expenses_w(yest_filename)
                    yest=0
                    break
                if o.lower()=='n':
                    print("Ok jumping for today's expenses")
                    break
                else:
                    if i==3:
                        print('Too many unsuccesful attempts')
                    print("Give correct input")
                    i+=1
    except:
        #print("Sorry!! we are getting some error we will fix this. Please report.\n")
        print("Write today's expenses")
        expenses_w(filename)   
    else:
        print("Write today's expenses")
        expenses_w(filename)
        
        
def exe(filename):
    while True:
        x=input("Do you want to view expenses(R) or write expenses(W) or exit by period(.): ")
        if x.lower()=='r':
            expenses_r()
            check(filename)
            break
        if x.lower()=='w':
            check(filename)
            break
        if x=='.':
            os._exit(1)
        else:
            print('Please give correct input or exit by period(.)')
            continue

exe(filename)
time.sleep(99999)


# In[ ]:




