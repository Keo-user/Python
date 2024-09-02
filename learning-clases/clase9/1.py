notas = [2, 3, 1]

#leer datos
for x in range (3):
    nota = input(f"Ingrese la nota {x}: ")
    notas.append(nota)

#calcular el promedio

promedio = sum(notas) / len(notas)

if promedio > 1.7:
    