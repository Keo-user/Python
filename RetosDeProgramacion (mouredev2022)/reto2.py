# secuencia de fibonacci

n0 = 0
n = 1


contador = 0

print(f"{n0},")
for i in range(1, 50):
    n1 = n0 + n
    print(f"{n0}, {n}, {n1}")
    n0 = n
    n = n1