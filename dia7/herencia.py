class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")


class Pajaro(Animal):
    pass


mi_pajaro = Pajaro(3, "verde")

mi_pajaro.nacer()
