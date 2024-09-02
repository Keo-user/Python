x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el ultimo numero: "))

for i in range(x, y, 2):
    if x % 2 == 0:
        print(i)
    elif x % 2 != 0:
        print(i+1)