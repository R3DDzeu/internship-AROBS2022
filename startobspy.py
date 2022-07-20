import os

def start():
    cwd = os.getcwd() # salvam working dir-ul de baza
    os.chdir("C:\Program Files\obs-studio\\bin\\64bit\\") # aici se va introduce dir-ul instalarii obs-ului deoarece obs-ul nu va porni dintr-un script decat daca working dir-ul este acelasi cu locul instalarii
    os.startfile("obs64.exe")
    os.chdir(cwd)  # am schimbat working dir-ul inapoi la cel de baza pentru a ne crea viitoarele fisere tot aici