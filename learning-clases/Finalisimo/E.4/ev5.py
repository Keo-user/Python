cadena = input("Ingrese una oracion: ")
longCad = len(cadena)
vocales = 0

for i in range(0, longCad):

    if cadena[i] in "AaEeIiOoUu":
        vocales += 1

print(f"La palabra {cadena} tiene {vocales} vocal/es")