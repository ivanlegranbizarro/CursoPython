class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"


class Cliente(Persona):
    def __init__(self, nombre, edad, numero_cuenta, salario=1000):
        super().__init__(nombre, edad)
        self.numero_cuenta = numero_cuenta
        self.salario = salario

    def depositar(self, cantidad):
        self.salario += cantidad
        return print(f"{self.nombre} ha depositado {cantidad} en su cuenta")

    def retirar(self, cantidad):
        if self.salario < cantidad:
            print("No tiene suficiente dinero para retirar esa cantidad")
            return self.retirar()
        self.salario -= cantidad
        return print(f"{self.nombre} ha retirado {cantidad} en su cuenta")

    def __str__(self):
        return f"{super().__str__()}, número de cuenta: {self.numero_cuenta}, salario: {self.salario}"


cliente1 = Cliente("Juan", 25, 12345678)


def retirar_dinero(cliente, cantidad):
    cliente.retirar(cantidad)


def depositar_dinero(cliente, cantidad):
    cliente.depositar(cantidad)


while True:
    eleccion = int(
        input(
            """
    ¿Qué quieres hacer?
    1. Depositar
    2. Retirar
    3. Ver saldo
    4. Salir
    """
        )
    )

    match eleccion:
        case 1:
            cantidad = int(input("¿Cuánto dinero quieres depositar? "))
            depositar_dinero(cliente1, cantidad)
        case 2:
            cantidad = int(input("¿Cuánto dinero quieres retirar? "))
            retirar_dinero(cliente1, cantidad)
        case 3:
            print(cliente1)
        case 4:
            exit()
