
num1 = float(input("\nIngrese el primer numero: "))
num2 = float(input("\nIngrese el segundo numero: "))

print(f"\nLos numeros ingresados: {num1} y {num2}")

if num1 > num2:
        print(f"\nEl numero {num1} es mayor que el numero {num2}")
elif num1 < num2:
        print(f"\nEl numero {num2} es mayor que el numero {num1}")
elif num1 == num2 or num2 == num1:
        print(f"\nLos numeros {num1} y {num2} son identicos")
else:
        print("xd")