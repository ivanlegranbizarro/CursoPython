# Métodos


class Pajaro:
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        return "Pío-pío"

    def volar(self, metros):
        return f"El pájaro vuela {metros} metros de distancia"


mi_pajaro = Pajaro("verde", "periquito")


print(mi_pajaro.volar(200))
