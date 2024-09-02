def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if (b != 0):
        a / b 
    else:
        return "Error, Div por cero"


if __name__ == "__main__":
    print(suma(3, 2))
    print(resta(3, 2))
    print(mul(3, 2))
    print(div(3, 2))    