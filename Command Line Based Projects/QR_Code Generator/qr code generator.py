#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 


# String which represent the QR code 
s = "url"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png" 
url.svg("myqr.svg", scale = 8) 


# In[ ]:




