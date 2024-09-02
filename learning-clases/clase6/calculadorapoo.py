#definicion de clase
"""se usa el PascalCase para las clases, y en singular
esto es un convenio, no es necesario seguirlo de esta manera"""
class Calculadora:
    """calculadora estandar (dos numeros)"""

    num1 = None
    num2 = None
    resultado = None
    """Asi se define un constructor en python"""
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y
        resultado = 0

    def sumar(self):
        self.resultado = self.num1 + self.num2
        return self.resultado
    
    def restar(self):
        self.resultado = self.num1 - self.num2
        return self.resultado

    def multiplicar(self):
        self.resultado = self.num1 * self.num2
        return self.resultado
    
    def dividir(self):
        self.resultado = self.num1 / self.num2
        return self.resultado
    def setValor(self, x, y):
        self.num1 = x
        self.num2 = y



if __name__ == "__main__":

    """esta es la construccion"""
    miCasio = Calculadora(float(input("Primer numero: ")), int(input("Segundo numero: "))) #instanciacion
    print(f"la suma es: {miCasio.sumar()}")
    print(f"La resta es: {miCasio.restar()} ")
    print(f"La multiplicacion es: {miCasio.multiplicar()} ")
    print(f"La division es: {miCasio.dividir()} ")

    miCasio.setValor(float(input("Primer numero: ")), int(input("Segundo numero: ")))
    print(f"la suma es: {miCasio.sumar()}")
    print(f"La resta es: {miCasio.restar()} ")
    print(f"La multiplicacion es: {miCasio.multiplicar()} ")
    print(f"La division es: {miCasio.dividir()} ")

    texas = Calculadora(float(input("Primer numero: ")), int(input("Segundo numero: ")))
    print(f"la suma es: {texas.sumar()}")
    print(f"La resta es: {texas.restar()} ")
    print(f"La multiplicacion es: {texas.multiplicar()} ")
    print(f"La division es: {texas.dividir()} ")