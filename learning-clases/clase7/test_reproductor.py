from tkinter import *
from tkinter.ttk import *
from reproductor import Reproductor

musica = Reproductor("wefere.mp3")

def play_musica():
    musica.volume (0.8)
    musica.play()
    label.config(text=f"Reproduciendo {musica.archivo}")

def pausar_musica():
    musica.pausa()
    label.config(text="Musica en pausa")

def despausar_musica():
    musica.despausar()
    label.config(text=f"Reproduciendo {musica.archivo}")

def parar_musica():
    musica.stop()
    label.config(text="Musica Parada")

def change_volume():
    musica.volume()
    label.config(text=f"Cambiando volumen")

master = Tk()

master.geometry("400x400")
master.title("Spotify")
master.iconbitmap("c:/Users/SNPP/Downloads/spotify_alt_macos_bigsur_icon_189704.ico")
label = Label(master, text = "Bienvenido a Spotify")
label.pack(pady = 10)

btn_play = Button(master, text = "▶", command = play_musica ) 
btn_play.pack(pady = 5) 
btn_play = Button(master, text = "⏸", command = pausar_musica) 
btn_play.pack(pady = 5) 
btn_play = Button(master, text = "⏯", command = despausar_musica ) 
btn_play.pack(pady = 5) 
btn_play = Button(master, text = "⏹", command = parar_musica ) 
btn_play.pack(pady = 5) 

mainloop()