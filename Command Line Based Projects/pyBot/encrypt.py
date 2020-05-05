# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 02:27:31 2019

@author: Brothers
"""
from importer import import_func
from loop import loop
from encode import encode
from menu import menu
import time
import_func()
# sub-function of {encryption}
# directory check for encrypted file
def encrypt():
    try:
        # creating new directory or checking if file exist or not
        os.path.exists("E:\\PROJ.RC\\python\\pyBot\\enc_files")
         #if file exist if will run except code
    except IOError:
        #if file exist call encode function
        encode()    
    else: 
        # otherwise (if there is no exception then it meas that file do not exist so create new file and call encode function)
            loop()
            print(" Directory does not exist")
            os.makedirs("E:\\PROJ.RC\\python\\pyBot\\enc_files")
            loop()
            print(" Created new file")        
            encode()
            menu()
time.sleep(10000)