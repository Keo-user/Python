from pygame import mixer

class Reproductor:
    #atributos
    archivo = None
    nombre = None
    #constructor
    def __init__(self, archivo):
        self.archivo = archivo
        mixer.init()
        mixer.music.load(archivo)


    def play(self):
        mixer.music.play()
        return "Reproduciendo Musica"

    def pausa(self):
        mixer.music.pause()
        return "La musica se ha pausado"

    def despausar(self):
        mixer.music.unpause()
        return "La musica se ha despausado"

    def stop(self):
        mixer.music.stop()
        return "Se ha detenido la musica"

    def volume(self, v):
        mixer.music.set_volume(v)
        return "Definiendo volumen a {}".format(v) 
    
    
