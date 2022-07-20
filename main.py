import webbrowser
import logging
import datetime
import startobs
import time
import obsrecorder
import moviepy.editor as mp
import conversie
logging.basicConfig(level=logging.DEBUG, filename=f'log{datetime.datetime.now().strftime(" %d %m %Y %H-%M-%S")}.txt')
#log-ul va fi denumit dupa data,ora si secunda pentru a nu avea erori din cauza mai multor log-uri cu acelasi nume

if __name__ == '__main__':
    startobs.start()
    time.sleep(5)
    obsrecorder.startrec()
           #webbrowser.navigator()
           #locv = obsrecorder.getPth2()   #path-ul fisierului video
    time.sleep(5)
            #videotoaudio = mp.VideoFileClip(locv)
            #videotoaudio.audio.write_audiofile(r"de_analizat.wav")
    conversie.cnv()



