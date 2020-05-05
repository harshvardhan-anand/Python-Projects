# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:07:58 2019

@author: Brothers
"""
import os
import base64
import time



def loop():
    t=0
    while t<5999999:
        pass
        t=t+1
        
        
# menu=?calculator 
#only addition is allowed
def calc():
    
    
    while True:
        o=input(" Which operation do you want to proceed\n (+)Sum\n (-)Subtraction\n (*)multiplication\n (/)Division\n (p)Exponent--> ")
        if o=="+":
            operand=int(input("How many operands do you want to proceed with: "))
            lst=[]
            add=0
            for i in range(operand):
                lst.append(int(input("Enter operands: ")))
                add=lst[i]+add
                print(lst)
                print(i)
            print(f"Summation is {add}")
            break
            
            
        elif o=="-":
            try:
                ope=int(input("Enter operand a(a>b)"))
                op=int(input("Enter operand b(a>b)"))
            except TypeError:
                print("Type error")
                continue
            else:
                sub=ope-op
                print(f"Substraction is = {sub}")
                break
        #multiply
        elif o=="*":
            try:
                ope=int(input("Enter operand 1= "))
                op=int(input("Enter operand 2= "))
            except TypeError:
                print("Type error")
                continue
            else:
                mul=ope*op
                print(f"Multiplication is = {mul}")
                break
        #divide
        elif o=="/":
            try:
                ope=int(input("Enter neumerator= "))
                op=int(input("Enter divisor= "))
            except TypeError:
                print("Type error")
                continue
            else:
                div=ope/op
                print(f"Division is = {div}")
            break
        #exponent
        elif o=="p":
            try:
                ope=int(input("Enter base= "))
                op=int(input("Enter exponent= "))
            except TypeError:
                print("Type error")
                continue
            else:
                ex=ope**op
                print(f"Exponent is = {ex}") 
                break
        else:
            print("wrong input")
            continue
        menu()
        
def encryption():
    
    while True:
        o=input(" How do you want to proceed\n (W)Encrypt text\n (S)Show encrypted text: ")
        if o=='w' or o=='W':
            encrypt()
            break # tell me more function
        elif o=='S' or o=='s':
            decrypt()
            break #tell me more function
        else:
            print(" I can't get it")
            continue
    menu()
    time.sleep(10000)
    
def encrypt():
    try:
        # creating new directory or checking if file exist or not
        os.path.exists("E:\\PROJ.RC\\python\\pyBot\\enc_files")
         #if file exist if will run except code
    except FileNotFoundError:
        #if file do not exist call encode function
            print(" Directory does not exist")
            os.makedirs("E:\\PROJ.RC\\python\\pyBot\\enc_files")
            loop()
            print(" Created new file")        
            encode()
            menu()    
    else: 
        # otherwise (if there is no exception then it meas that file do  exist  call encode function)
        encode() 
        menu()
            
    time.sleep(10000) 
    
def encode():
    loop()
    #taking input for encoding
    text=input("Enter what to be encrypted: ")
    text=text+"|||"
    # encoding
    encoded=base64.b64encode(bytes(text,'utf-8'))
     # writing text in it
    encoded_text=open("E:\\PROJ.RC\\python\\pyBot\\enc_files\\enc.txt", mode='b+a')
    encoded_text.write(encoded) 
    encoded_text.close()
    #time.sleep(10000)
    menu()
    
    

def decrypt():
    print(" Your datas are seperated by '|||' symbol")
    read=open("E:\\PROJ.RC\\python\\pyBot\\enc_files\\enc.txt", mode='r')
    read=read.read()
    read=base64.b64decode(bytes(read,'utf-8'))
    print(read)
    o=input("\n\n\n$ Press X to MENU $: ")
    if o=="x" or o=="X":
        menu()
    

def menu():
    
    while True:
        x=input(" So what do you want to do: \n (C)Open  Calculator\n (E)Encrypted vaults\n (X)Exit: ")
        if x=="C" or x=="c":
            calc()
            break
        elif x=="E" or x=="e":
            encryption()
            break
        elif x=="X" or x=="x":
            quit()
            break
        else:
            print(" Wrong input")
            continue
        time.sleep(10000)
    
        
        
def menuexpl():
    loop()
    print(" I can calculate, do a web search, encrypt your confidential texts or messages also I will tell you about the whole world and I can truely make you laugh")
    loop()
    menu()
    time.sleep(10000)
    
    
def helpu():
    loop()
    print(" I am your assistant")
    loop()
    print(" Let me tell you what can I do for you")
    menuexpl()
    time.sleep(10000)

def welcome():
    
    #intial welcome
    print(" Hi! I am Pybot")
    loop()
    
    #taking user name
    while True:
        try:
            name=input(" What's yours: ")
        except ValueError:
            pass
        else:
            if name.isalpha()==True:
                print(f" Hi! {name}")
                break
            else:
                print(" I can't get your name")
                continue
    #fuction call
    helpu()
    time.sleep(10000)
    
welcome()
