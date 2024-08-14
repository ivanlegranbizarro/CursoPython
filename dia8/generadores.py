# Los generadores son funciones que retornan valores a medida
# que los vas necesitando (en lugar de usar return, usamos yield)


def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10


g = mi_generador()

print(next(g))


def otro_generador():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x


o_g = otro_generador()


def generando_infinito():
    x = 1
    while True:
        yield x
        x += 1


infinito = generando_infinito()


def multiplos_de_7():
    x = 7
    while True:
        yield x
        x += 7


generador = multiplos_de_7()

print(next(generador))
print(next(generador))
print(next(generador))
