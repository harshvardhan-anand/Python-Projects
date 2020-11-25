#!/usr/bin/env python
# coding: utf-8

# In[22]:


import PyPDF2 as reader
from gtts import gTTS
import os
from playsound import playsound
import threading


# # Multithreading

# In[13]:


def create_file():
    filename = input("Enter the filename (with path)")
    try:
        dirname = filename.split('.')[0]
        os.mkdir(dirname)
    except:
        pass
    file = open(filename, 'rb')
    pdf = reader.PdfFileReader(file)
    print(f"Total pages in pdf: {pdf.numPages}")
    totalpages = pdf.numPages
    return totalpages, dirname,pdf,file


# In[18]:


def create_audio(totalpages,pdf,only_create_first_file=0):
    
    if not(only_create_first_file):
        start = 1
    else:
        start=0
        print("Contacting Google...\nReading...")
    for num in range(start,totalpages):
        page = pdf.getPage(num)
        text = page.extractText()
        tts = gTTS(text)
#         print(tts.get_urls())
        savefile = f'{str(num)}.mp3'
        tts.save(savefile)
        print(f'Audio file created for page: {num+1}')
        if only_create_first_file:
            break


# In[19]:


def play_sound(dirname, all_created_audio):
    # argument need to be passed = totalpages
    to_be_played = 0
    retry = 0
    exception_occured = 0
    while retry<3: 
        for audio in range(to_be_played ,all_created_audio):
            filename = f'{str(audio)}.mp3'
            print(f'Playing audio for page: {audio+1}')
            audiofile = os.path.join(os.getcwd(), dirname, filename)
            try:
                playsound(audiofile)
                retry = 0
                to_be_played = audio
            except Exception as E:
                print(E)
                exception_occured = 1
                retry+=1
                retry_log = f"We have encountered some issues. Retrying : {retry}"
                print(retry_log)
                playsound(retry_log)
                break
        #print(f'Debug Info:\nLast file to be played:{to_be_played}\t All Created Audio:{all_created_audio-1}\t IsException:{exception_occured}')       
        if (to_be_played == (all_created_audio-1) and not(exception_occured)) or (retry==3):
            break
        exception_occured = 0


# In[20]:


def main():
    totalpages, dirname, pdf,file = create_file()
    create_audio(totalpages,pdf,only_create_first_file=1)
    create_audio_thread = threading.Thread(target=create_audio, args=(totalpages,pdf))
    play_sound_thread = threading.Thread(target=play_sound, args=(dirname, totalpages))
    create_audio_thread.start()
    play_sound_thread.start()
    create_audio_thread.join()
    play_sound_thread.join()
    file.close()


# In[21]:


main()

