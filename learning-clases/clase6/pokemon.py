class Pokemon():

    def __init__(self, nombre, tipo, vida, evolucion = 1):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.evolucion = evolucion 
        self.ataque = []

    def setAtaque(self, ataque):
        self.ataque.append(ataque)

    def atacar(self, i):
        return(f"{self.nombre} ataco con {self.ataque[i]}")

    def defenderse(self):
        return(f"{self.nombre} se defendio")


if __name__ == "__main__":
    pikachu = Pokemon(tipo = "Electrico", nombre = "Pikachu", vida = 200 )
    charizard = Pokemon(tipo = "Fuego", nombre = "Charizard", vida = 500, evolucion = 3)

    pikachu.setAtaque("Impactrueno")
    pikachu.setAtaque("Placaje")
    pikachu.setAtaque("Bola Voltio")

    print(pikachu.atacar(0))
    print(charizard.defenderse())