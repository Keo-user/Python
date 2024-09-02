import random

while True:
    aleatorio = random.randrange(0, 3)
    elijePc = ""
    print("1, Piedra")
    print("2, Papel")
    print("3, Tijera")
    opcion = int(input("Elige tu opcion: "))
    
    if opcion == 1:
        elijeUsuario = "Piedra"
    elif opcion == 2:
        elijeUsuario = "Papel"
    elif opcion == 3:
        elijeUsuario = "Tijeras"
    print("Elejiste: ", elijeUsuario)

    if opcion == 1:
        elijePc = "Piedra"
    elif opcion == 2:
        elijePc = "Papel"
    elif opcion == 3:
        elijePc = "Tijeras"
    print("La maquina elijio: ", elijePc)
    print("...")

    if elijePc == "Piedra" and elijeUsuario == "Papel":
        print("Ganaste, papel envuelve Piedra")
    if elijePc == "Papel" and elijeUsuario == "Tijera":
        print("Ganaste, Tijera corta Papel")
    if elijePc == "Tijera" and elijeUsuario == "Piedra":
        print("Ganaste, Piedra machaca tijera")
    if elijePc == "Papel" and elijeUsuario == "Piedra":
        print("perdiste, papel envuelve Piedra")
    if elijePc == "Tijera" and elijeUsuario == "Papel":
        print("Perdiste, Tijera corta Papel")    
    if elijePc == "Piedra" and elijeUsuario == "Tijera":
        print("Perdiste, Piedra machaca tijera")   