import os
import time

#------------------------------------------- can be ignored, varianta primitiva de cod----------------------------------------

def start():
    with open('start_obs.txt', 'w') as f:
         f.write('@echo off \n cd "C:\Program Files\obs-studio\\bin\\64bit\  \n start obs64.exe \n exit') #a se modifica 64 cu 32, dupa caz
         text = "start_obs.txt"
         bat = "start_obs.bat"

    os.rename(text,bat)

    os.startfile("start_obs.bat")
    time.sleep(5)
    os.remove("start_obs.bat") #daca nu l stergem nu mai merge codu