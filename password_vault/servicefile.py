# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:58:17 2019

@author: Brothers
"""
#using this for importing os based operations
import os
#importing this for encoding
import base64
#defining function write
def write(param1,param2):
    #creating a folder a specified location
    os.makedirs("E:\\PROJ.RC\\python\\files\\catbot")
    str="this is my check file for"+ param1 + "with" +param2
    #getting encrypted text
    encryption=base64.b64encode(bytes(str,'utf-8'))
    #opening a text file to specified location with w=write and wb=write binary
    serv_catbot=open("E:\\PROJ.RC\\python\\files\\catbot\\catbot.txt", mode='wb')
    serv_catbot.write(encryption)
    serv_catbot.seek(0)
    serv_catbot.close()

#this fuction will take register module as argument
    #param1 is from register
    #param2 is for login

    
        
            