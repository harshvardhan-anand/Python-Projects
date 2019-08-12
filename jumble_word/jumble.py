#!/usr/bin/env python
# coding: utf-8

# # Getting dictionary for validation

# In[65]:


import pickle


# #this is not required because we have saved our data to pickle file
# with open('dictionary mega.txt', 'r', encoding='utf-8') as file:
#     data = (file.read()).lower().split(',')
# type(data)

# #saving variable 'data'  which have dictionary for future use even if we dont have our dictionary text file
# #using wb to write binary (non-text  file)
# with open('data.pickle', 'wb') as pfile:
#     pickle.dump(data, pfile)

# In[66]:


#loading variable 'data' which have dictionary  data
with open('data.pickle', 'rb') as rpfile:
    data = pickle.load(rpfile)


# # Algorithm to find the perfect string from jumbled one

# jumbled_string = input("Enter the jumbled string: ")

# char_set = set(jumbled_string)

# In[69]:


def resolver(data):
    jumbled_string = input("Enter the jumbled string: ")
    char_set = set(jumbled_string)
    found = 0
    # iterating over every wors in dictionary that is saved in variable 'data'.
    for word in data:    
        # 'flag' is used to identify whether word is found or not. Default is word not found.
        flag = 0
        # iterating over all the unique characters in jumbled string
        for char in char_set:
            # checking whether the character in jumbled string is present in the word of dictioary or not. If yes then the occurance of that particular character in jumbled string matched with that of charaters in word of dictionary 
            if (char in word) and (word.count(char) == jumbled_string.count(char)):
                # if found then put flag to 1
                flag = 1
            else:
                # otherwise stop checking that particular word and move to another one
                flag = 0
                break
        if flag:
            found = 1
            # if word is is founded with given criteria then check whether the length of word in dictionary is same as that of the length of jumbled string.
            if len(word) == len(jumbled_string):
                found = 1
                break
            else:
                found = 0

    if found:
        print("Rearranged word is: {}".format(word))
    else:
        print('Oops!! No word found')    


# In[79]:


resolver(data)

