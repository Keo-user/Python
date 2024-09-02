acceso = {"Sara":"SNPP", "Claudia":"abc", "Yhonny":"Gael"}

i = 0 

acceso["Sara"] = "12345"

while i < 3:
    usuario = input("Ingresa eñ usuario: ")
    if usuario in acceso:
        print("Usuario no registrado")