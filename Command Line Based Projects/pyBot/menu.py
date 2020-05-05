# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 02:28:45 2019

@author: Brothers
"""

from loop import loop
from encryption import encryption
from calc import calc
import time

def menu():
    loop()
    while True:
        x=input(" So what do you want to do: \n (C)Open  Calculator\n (E)Encrypted vaults: ")
        if x=="C" or x=="c":
            calc()
            break
        elif x=="E" or x=="e":
            encryption()
            break
        else:
            print(" Wrong input")
            continue
        
        time.sleep(10000)
    