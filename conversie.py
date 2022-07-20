import obsrecorder
import moviepy.editor as mp

def cnv():
    videotoaudio = mp.VideoFileClip(obsrecorder.getPth2()) # preia locatia inregistrarii video
    videotoaudio.audio.write_audiofile(r"de_analizat.wav") # o converteste in audio


