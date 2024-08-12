class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice Muuuuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice Beeee")


mi_vaca = Vaca("Torrezna")

mi_oveja = Oveja("Nube")


def animal_habla(animal):
    animal.hablar()


animal_habla(mi_vaca)

animal_habla(mi_oveja)
