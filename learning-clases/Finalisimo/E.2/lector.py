from urllib import request
from urllib.error import URLError

def Palabra(palabra):
    palabra = None
    return palabra

def verContenido(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return(' ¡La url '+ url + 'no existe!')
    else:
        contenido = f.read()
        return contenido
    

lista = ['bobo','imbécil']    
def verificar(url):

    contenido = verContenido(url)

    for po in lista:
        if po in contenido.decode():
            return f"La palabra {po} existe en el sitio"


url = 'https://www.antena3.com/noticias/cultura/mapa-insultos-espana-cuales-son-improperios-mas-utilizados-comunidad-autonoma_202012185fdc94b3904ac7000171eab3.html'
print (verificar(url))



