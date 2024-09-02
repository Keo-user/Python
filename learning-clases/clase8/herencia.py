class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura 
    
    def perimetro(self):
         return (self.base + self.altura)*2
    
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == '__main__':
        rectangulo = Rectangulo(base=int(input("base del rectangulo: ")), altura=int(input("altura del rectangulo: ")))
        print(f"Area del rectangulo: {rectangulo.area()}\nPerimetro del rectangulo: {rectangulo.perimetro()}\n")

        cuadrado = Cuadrado(lado=int(input("Lado del cuadrado: ")))
        print(f"Area del Cuadrado: {cuadrado.area()}\nPerimetro del cuadrado: {cuadrado.perimetro()}")

