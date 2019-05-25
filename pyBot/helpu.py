# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 02:26:57 2019

@author: Brothers
"""

from loop import loop
from menuexpl import menuexpl
import time

# sub-fuction of {welcome}
# giving menu to the user
def helpu():
    loop()
    print(" I am your assistant")
    loop()
    print(" Let me tell you what can I do for you")
    menuexpl()
    time.sleep(10000)