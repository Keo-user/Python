
x = 1
print("\nDel 1 al 100\n")
while (x <= 100):
    print(x)
    x += 1

a = 2
b = 101

print("\nNumeros pares del 2 al 100\n")
for i in range(a, b, 2):

    if a % 2 == 0:
        print(i)
    elif b % 2 != 0:
        print(i+1)