import timeit


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


declaracion = """
prueba_for(10)
"""
mi_setup = """
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
"""

declaracion_while = """
prueba_while(10)
"""
mi_setup_while = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion_for = timeit.timeit(declaracion, mi_setup, number=1000000)

duracion_while = timeit.timeit(declaracion_while, mi_setup_while, number=1000000)


print(f"Intermedio {duracion_for}")

print(f"Intermedio {duracion_while}")
