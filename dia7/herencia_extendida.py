class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def comunicarse(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):
    def __init__(self, edad, color, especie):
        super().__init__(edad, color)
        self.especie = especie

    def comunicarse(self):
        print("Pío pío")

    def volar(self, kms):
        return f"El pájaro vuela {kms} kilómetros"

    def __str__(self):
        return f"Mi pájaro es de color {self.color} y de la especie {self.especie}"


piolin = Pajaro(3, "amarillo", "canario")

piolin.comunicarse()

print(piolin.volar(100))


print(piolin)


# Herencia múltiple


class Madre:
    def reir(self):
        print("jajaja")

    def hablar(self):
        print("¿Qué tal estás?")


class Padre:
    def hablar(self):
        print("Hola")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.hablar()

mi_nieto.reir()


class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Vertebrado, Ave, Reptil, Pez, Mamifero):
