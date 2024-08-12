class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        return "Pío-pío"

    def volar(self, metros):
        return f"El pájaro vuela {metros} metros de distancia"

    def pintar_negro(self):
        self.color = "negro"
        print("Este pájaro ahora es de color negro")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"El pájaro puso {cantidad} huevos")

    @staticmethod
    def volar_en_circulos():
        return "El pájaro vuela en circulos"

    def __str__(self):
        return f"Mi pájaro es de color {self.color} y de la especie {self.especie}"


Pajaro.poner_huevos(3)

print(Pajaro.volar_en_circulos())
