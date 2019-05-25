# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 02:28:14 2019

@author: Brothers
"""
from importer import import_func
from loop import loop
import time
import_func()

# sub-function for encryption 
def decrypt():
    print(" Your datas are seperated by '|||' symbol")
    read=open("E:\\PROJ.RC\\python\\pyBot\\enc_files\\enc.txt", mode='r')
    read=read.read()
    read=base64.b64decode(bytes(read,'utf-8'))
    print(read)
    time.sleep(10000)