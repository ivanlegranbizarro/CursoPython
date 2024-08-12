class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"


class Cliente(Persona):
    def __init__(self, nombre, edad, numero_cuenta, salario):
        super().__init__(nombre, edad)
        self.numero_cuenta = numero_cuenta
        self.salario = salario

    def depositar(self, cantidad):
        self.salario += cantidad
        return print(f"{self.nombre} ha depositado {cantidad} en su cuenta")

    def retirar(self, cantidad):
        self.salario -= cantidad
        return print(f"{self.nombre} ha retirado {cantidad} en su cuenta")

    def __str__(self):
        return f"{super().__str__()}, número de cuenta: {self.numero_cuenta}, salario: {self.salario}"
