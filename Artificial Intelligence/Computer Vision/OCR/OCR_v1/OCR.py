import time
import cv2
import numpy as np
import pytesseract as gocr
import time
from selectImage import image


# In[13]:


gocr.pytesseract.tesseract_cmd = r'C:\Users\Brothers\AppData\Local\Tesseract-OCR\tesseract.exe'


# In[17]:


class ocr():
    def __init__(self,
                 path=input("Enter the path of image: "),
#                  path='morg.jpg',
                 full_img=False,
                 selected_img=True,
                 saveText=True,
                 printText=True,
                 showRaw=False,
                 saveRaw=False):
        self.path = path
        self.full_img = full_img
        self.selected_img = selected_img
        self.saveText = saveText
        self.printText = printText
        self.showRaw = showRaw
        self.saveRaw = saveRaw

        if (self.full_img == self.selected_img == False):
            raise Exception("You can't get tea without tea leaves.")
        if (self.full_img == self.selected_img == True):
            raise Exception("No!!! this is not a method to prepare a cup of tea.")

        self.getText()

    def getText(self):
        if self.full_img:
            try:
                img = cv2.imread(self.path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            except:
                print('Could Not find image at specified location.')
            else:
                self._fullImage(img)
        elif self.selected_img:
            try:
                img = image(self.path)
                img = img.selectedImg
            except:
                print('Could Not find image at specified location.')
            else:
                self._fullImage(img)

    def _fullImage(self, img):
        text = gocr.image_to_string(img)

        if (self.printText == True) and (self.showRaw == False):
            self._textProcessing(text)
            print(self._text)
            self.saveRaw = 1
        if (self.printText == True) and (self.showRaw == True):
            print(text)
        if self.saveText:
            if not self.saveRaw:
                self._textProcessing(text)  # remove tags
            with open('recognised_text.txt', 'w') as file:
                try:
                    file.write(self._text)
                except:
                    file.write(text)



    def _textProcessing(self, text):
        # this is not a efficient method.
        temp = text.split()
        flag=0
        sentence=[]
        for i in temp:
            word=''
            for j in i:
                if (j=='\\'):
                    flag = 1
                    continue
                if flag:
                    continue
                    flag=0
                word+=j
            sentence.append(word)
        self._text = ' '.join(sentence).strip()

# In[18]:


o = ocr()
time.sleep(999)

# In[ ]:




