
print("\nBienvenido al consultor de Impuestos :D")


MONTOIRP = 80000000
sueldo = int(input("\nIngrese cual es su sueldo: "))

sueldoAnual = sueldo * 12
if sueldoAnual > MONTOIRP : 
    print("\nEsta persona debe pagar impuestos\n")
else:
    print("\nEsta persona no debe pagar impuestos\n")