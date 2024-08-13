def suma():
    try:
        numero1 = int(input("Introduce el primer número: "))
        numero2 = int(input("Introduce el segundo número: "))
        print(f"{numero1} + {numero2} = {numero1 + numero2}")
    except ValueError:
        print("Por favor, introduce dos números enteros")
        return suma()


suma()


def pedir_numero():
    while True:
        try:
            return int(input("Introduce un número entero: "))
        except ValueError:
            print("Por favor, introduce un número entero")


pedir_numero()
