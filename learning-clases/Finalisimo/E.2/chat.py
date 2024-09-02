import requests
from bs4 import BeautifulSoup
from plyer import notification

# Lista de palabras ofensivas
palabras_ofensivas = [
    "imbécil",
    "cabrón",
    "gilipollas",
]

# URL de la página web que deseas analizar
url = 'https://www.antena3.com/noticias/cultura/mapa-insultos-espana-cuales-son-improperios-mas-utilizados-comunidad-autonoma_202012185fdc94b3904ac7000171eab3.html'  # Reemplaza con la URL que deseas analizar

def obtener_contenido_web(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la respuesta HTTP es un error
        return response.text
    except requests.RequestException as e:
        print(f"Error al obtener el contenido de la web: {e}")
        return None

def buscar_palabras_ofensivas(contenido, palabras_ofensivas):
    texto_plano = BeautifulSoup(contenido, 'html.parser').get_text().lower()
    palabras_encontradas = [palabra for palabra in palabras_ofensivas if palabra in texto_plano]
    return palabras_encontradas

def enviar_notificacion(palabras_ofensivas):
    mensaje = f"Se encontraron las siguientes palabras ofensivas: {', '.join(palabras_ofensivas)}"
    notification.notify(
        title="Alerta de palabras ofensivas",
        message=mensaje,
        app_name="Buscador de palabras ofensivas"
    )

def main():
    contenido = obtener_contenido_web(url)
    if contenido:
        palabras_encontradas = buscar_palabras_ofensivas(contenido, palabras_ofensivas)
        if palabras_encontradas:
            print(f"Palabras ofensivas encontradas: {', '.join(palabras_encontradas)}")
            enviar_notificacion(palabras_encontradas)
        else:
            print("No se encontraron palabras ofensivas.")

if __name__ == "__main__":
    main()