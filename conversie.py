import obsrecorder
import moviepy.editor as mp

def cnv():
    videotoaudio = mp.VideoFileClip(obsrecorder.getPth2())
    videotoaudio.audio.write_audiofile(r"de_analizat.wav")
