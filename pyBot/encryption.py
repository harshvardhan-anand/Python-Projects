# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 02:27:50 2019

@author: Brothers
"""
from importer import import_func
from loop import loop
from encrypt import encrypt
from decrypt import decrypt
from menu import menu
import time
import_func()
# menu==?encryption
def encryption():
    loop()
    while True:
        o=input(" How do you want to proceed\n (W)Encrypt text\n (S)Show encrypted text: \n")
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