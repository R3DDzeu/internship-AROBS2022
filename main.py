import webbrowser
import logging
import datetime
logging.basicConfig(level=logging.DEBUG, filename=f'log_main_debug{datetime.datetime.now().strftime(" %d %m %Y %H-%M-%S")}.txt')
import startobs
import time
import obsrecorder
import moviepy.editor as mp
import conversie
import startobspy
import analizaaudio
import traceback

if __name__ == '__main__':
    try:
        startobspy.start()
        #startobs.start()  -------------------------- Varianta primitiva (functionala) de a depasi eroarea la pornirea OBS-ului (intai trebuie accest dir-ul)
        time.sleep(5)
        obsrecorder.startrec()
        #webbrowser.navigator()
        time.sleep(5)
        conversie.cnv()
        analizaaudio.measure_wav_db_level("de_analizat.wav")
    except:
        with open(f'exceptions{datetime.datetime.now().strftime(" %d %m %Y %H-%M-%S")}.log', "w") as logfile:
            traceback.print_exc(file=logfile)
            print('A fost intampinata o eroare! Verifica exceptions.log !')
            exit()






