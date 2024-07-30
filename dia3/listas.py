# Las listas son mutables: pueden ser modificadas en tiempo de ejecución

mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]

mi_lista2.append("g")

resultado = len(mi_lista)
resultado_2 = mi_lista[0]
resultado_3 = mi_lista[0:2]

mi_lista_3 = mi_lista + mi_lista2


guardar_elemento_eliminado = mi_lista_3.pop()


lista_desordenada = ["g", "o", "m", "b", "a", "f"]

lista_desordenada.sort()

print(lista_desordenada)
