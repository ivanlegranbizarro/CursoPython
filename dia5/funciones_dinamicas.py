# Funciones más dinámicas, con un indeterminado número de parámetros


def chequear_3_cifras(numero):
    return numero in range(100, 1000)


def chequear_lista_numeros_3_cifras(lista):
    lista_de_numeros_de_3_cifras = []
    for numero in lista:
        if chequear_3_cifras(numero):
            lista_de_numeros_de_3_cifras.append(numero)
    return lista_de_numeros_de_3_cifras


numeros_a_chequear = [934, 34, 1000, 345]


print(chequear_lista_numeros_3_cifras(numeros_a_chequear))

lista_numeros = [-1, 10, 20]


def todos_positivos(lista_numeros):
    return all(num >= 0 for num in lista_numeros)


# Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.


def suma_menores(lista_numeros):
    return sum(num for num in lista_numeros if num > 0 and num < 1000)
