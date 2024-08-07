# args se utiliza para pasar a una función un numéro indefinido de parámetros


def sumar_numeros(*args):
    resultado = 0
    for num in args:
        resultado += num

    return resultado


# kwargs se utiliza para pasar a una función un número indefinido de parámetros
# como un diccionario


def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(clave, valor)
        total += valor

    return total


print(suma(x=1, y=2, z=3))


def suma_total(num1, num2, *args, **kwargs):
    print(f"El primer argumento es {num1}")
    print(f"El segundo argumento es {num2}")

    for num in args:
        print(f"El argumento {num} es un argumento extra")

    for clave, valor in kwargs.items():
        print(clave, valor)

    return num1 + num2 + sum(args) + sum(kwargs.values())


print(suma_total(1, 2, 3, x=1, y=2, z=3))
