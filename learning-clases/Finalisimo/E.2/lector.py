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
    
def verificar():

    if Palabra(input("Ingrese la palabra a filtrar: ")) == verContenido('https://www.antena3.com/noticias/cultura/mapa-insultos-espana-cuales-son-improperios-mas-utilizados-comunidad-autonoma_202012185fdc94b3904ac7000171eab3.html'):
        texto = Palabra
        nombre_fichero = 'Palabra-'+ texto + '.txt'
        f = open(nombre_fichero, 'w')
        f.write(f'{texto}\n')
        f.close
    else:
        print("No se encontro la palabra")

print (verificar())



