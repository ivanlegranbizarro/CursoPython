class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro("negro", "Tucán")

print(f"Mi pájaro es de color {mi_pajaro.color} y de la especie {mi_pajaro.especie}")

print(Pajaro.alas)
print(mi_pajaro.alas)


class Casa:
    def __init__(self, color, cantidad_pisos=1):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa("blanco", 4)
