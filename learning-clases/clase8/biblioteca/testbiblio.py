from biblioteca import Biblioteca
from libro import Libro

if __name__ == "__main__":
    ejecutar = True

    while ejecutar:
        print("- - - Bienvenido al sistema bibliotecario - - -")
        opcion = int(input("¿ Que vas a hacer ? \n\n1-Crear Biblioteca\n2-Agregar Libro\n3-Ver Catalogo\n4-Quitar Libro\n5-Salir\n\nElige tu opcion:"))


        if opcion == 1:
            nombre = input("Nombre de la biblioteca: ")
            biblioteca = Biblioteca(nombre)

            print("Se creo la biblioteca: {}".format(biblioteca.consultar_nombre_biblioteca))

        elif opcion == 2:
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            cantidad_de_paginas = input("Paginas: ")
            genero = input("Genero: ")
            sinopsis = input("Sinopsis: ")

            libro = Libro(titulo, autor, cantidad_de_paginas, genero, sinopsis)
            biblioteca.agregar_libro(libro)

        elif opcion == 3:
            print("Catalogo de libros ")
            for i in biblioteca.consultar_libro():
                print(i)

        elif opcion == 4:
            indice = input("Id del libro a eliminar: ")
            biblioteca.quitar_libro()

        elif opcion == 5:
            print("Gracias por visitar ❤")
            break

        else:
            print("Opcion inconrrecta")