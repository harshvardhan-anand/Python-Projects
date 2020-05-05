# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 02:24:58 2019

@author: Brothers
"""

from  loop import loop
from helpu import helpu
import time

#main fuction
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
# here we can get introduced