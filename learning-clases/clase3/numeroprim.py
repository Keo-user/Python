x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))

if x > y:
    print(f"El numero {x} es mayor")
    if x % 2 == 0:
        print("Y ademas es par")
    else:
        print("Y ademas es impar")
elif y > x:
    print(f"El numero {y} es mayor")
    if y % 2 == 0:
        print("Y ademas es par")
    else:
        print("Y ademas es impar")
else:
    print("Algo esta mal")