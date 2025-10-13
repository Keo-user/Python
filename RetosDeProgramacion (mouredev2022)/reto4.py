
def AreaPoligono(poligono):

    if poligono.lower() == "triangulo":
        b = float(input("Ingresa la base del triangulo: "))
        h  = float(input("Ingresa la altura del trianuglo: "))
        operacion = (b*h)/2
        print(f"El area del triangulo es: {operacion}")
    elif poligono.lower() == "cuadrado":
        l = float(input("Ingrese el valor de los lados del cuadrado: "))
        operacion = l**2
        print(f"El area del cuadrado es: {operacion}")
    elif poligono.lower() == "rectangulo":
        b = float(input("Ingrese el valor de la base del rectangulo: "))
        h = float(input("Ingresa el valor de la altura del rectangulo: "))
        operacion = b*h
        print(f"El area del rectangulo es: {operacion}")
    else:
        print("Error")

    
AreaPoligono(poligono=input("Ingrese el poligono al que quiera sacarle el area: "))
