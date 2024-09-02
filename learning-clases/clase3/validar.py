user = input("Ingrese el usuario: ")
password = int(input("Ingrese la contraseña: "))

if user == "admin" and password == 12345:
    print("Acceso concedido")
else:
    print("Acceso denegado")