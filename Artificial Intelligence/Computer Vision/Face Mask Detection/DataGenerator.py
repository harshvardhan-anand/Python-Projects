#!/usr/bin/env python
# coding: utf-8

# **Here we are not splitting data in train test and validation seperately, combining all img in one folder.**
# 

# In[ ]:


'''
1. BASE is base directory i.e dir where data file resides. Inside data file we have train test and validation folder.
2. Master folder name is the directory that have train,test and validaation folder
2. target is a list of all the labels
3. data_map={'filename':code}, filename is the name of directory used for label and 
                                'code' is the code for target.
5. IGNORE_FILE are the files that do not belong to image dataset like csv, md, txt files or any other folder except train, tes,t validation.

folder structure ->
desktop/dataset/train/with_mask/image.jpg
desktop/dataset/train/without_mask/image.jpg

BASE = desktop
DATASET_FOLDER_NAME = dataset
'''


# In[2]:


import os
import cv2
import numpy as np
import time


# In[19]:


def total_files():
    total = 0
    for i in MAIN_DIR:
        train_test_base = os.path.join(BASE, DATASET_FOLDER_NAME, i) #desktop/dataset/train
        train_test_dir = os.listdir(train_test_base) #['with_mask','without_mask']
        for j in train_test_dir:
            labeled_dir_path = os.path.join(train_test_base, j) #desktop/dataset/train/with_mask
            all_img = os.listdir(labeled_dir_path) #['img1.jpg','img2.jpg','img3.jpg'....]
            total += len(all_img)
    print(f'Total files are {total}')


# In[20]:


target = []
data = []
data_map = {
    'with_mask':1,
    'without_mask':0
}
skipped = 0

BASE = ""
DATASET_FOLDER_NAME = 'Dataset'
HAAR_CASCADE_PATH = r'haarcascade_frontalface_default.xml'
IGNORE_FILES = ['README.md']
img_shape = 50


# In[22]:


# MAIN_DIR have folder train,test,validation
MAIN_DIR = os.listdir(os.path.join(BASE, DATASET_FOLDER_NAME))
for ignore_file in IGNORE_FILES:
    MAIN_DIR.remove(ignore_file)
    
total_files()
for i in MAIN_DIR:
    train_test_base = os.path.join(BASE, DATASET_FOLDER_NAME, i) #desktop/dataset/train
    train_test_dir = os.listdir(train_test_base) #['with_mask','without_mask']
    for j in train_test_dir:
        labeled_dir_path = os.path.join(train_test_base, j) #desktop/dataset/train/with_mask
        all_img = os.listdir(labeled_dir_path) #['img1.jpg','img2.jpg','img3.jpg'....]
        print(f'\nExecuting - {i}/{j}')
        for k in all_img:
            image_path = os.path.join(labeled_dir_path, k)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            # classifier = cv2.CascadeClassifier(HAAR_CASCADE_PATH) # Detecting Face
            # rect = classifier.detectMultiScale(image)
            # for x,y,w,h in rect:
            #     image = image[y:y+h, x:x+w] # cropping Face
            try:
                # sometimes face is not detected so we get empty array and that array cant be resized
                # resizing to (50 x 50)
                image = cv2.resize(image,(img_shape,img_shape))
            except Exception as E:
                skipped += 1
                print(E)
                continue
            data.append(image)
            target.append(data_map[j])
print(f'\n{skipped} files skipped.')

with open(r'CleanedData/data.npy','wb') as file:
    np.save(file,np.array(data))
    print('\nData file saved.')
    
with open(r'CleanedData/target.npy','wb') as file:
    np.save(file,np.array(target))
    print('Target file saved.')

print('\nFinished')
time.sleep(6000)




