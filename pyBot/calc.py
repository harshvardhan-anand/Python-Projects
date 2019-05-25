# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 02:28:37 2019

@author: Brothers
"""
from importer import import_func
import loop
import time
import_func()
# menu=?calculator 
#only addition is allowed
def calc():
    loop()
    while True:
        o=input(" Which operation do you want to proceed\n (+)Sum\n (-)Subtraction\n (*)multiplication\n (/)Division\n (p)Exponent")
        if o=="+":
            operand=int(input("How many operands do you want to proceed with: "))
            for i in range(operand):
                operand.append(int(input()))
                add=0
                add=operand[i]+add
            print(f"Summation is {add}")
            break
            
        if o=="-":
            try:
                ope:int(input("Enter operand a(a>b)"))
                op:int(input("Enter operand b(a>b)"))
            except TypeError:
                print("Type error")
                continue
            else:
                sub=ope-op
                print(sub)
                break
                
        #multiply
        if o=="*":
            try:
                ope:int(input("Enter operand 1= "))
                op:int(input("Enter operand 2= "))
            except TypeError:
                print("Type error")
                continue
            else:
                mul=ope*op
                print(mul)
                break
        #divide
        if o=="/":
            try:
                ope:int(input("Enter neumerator= "))
                op:int(input("Enter divisor= "))
            except TypeError:
                print("Type error")
                continue
            else:
                div=ope/op
                print(div)
                break
        #exponent
        if o=="p":
            try:
                ope:int(input("Enter operand 1= "))
                op:int(input("Enter operand 2= "))
            except TypeError:
                print("Type error")
                continue
            else:
                ex=ope**op
                print(ex) 
                break
        else:
            print("wrong input")
            continue
        menu()
        time.sleep(10000)