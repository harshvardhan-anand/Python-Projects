# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 02:27:16 2019

@author: Brothers
"""
from importer import import_func
from loop import loop
import time
import_func()
# sub-function of {dir_check_encrypt}
# it will take input from user and encode it 
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
    time.sleep(10000)