# Los enumeradores se usan cuando queremos iterar
# sobre los índices de un interable


from hamcrest import starts_with


nombres = ["Pepe", "Juan", "Luis"]

for indice, nombre in enumerate(nombres):
    print(indice, nombre)


for i, item in enumerate(range(50, 55)):
    print(i, item)

# Usar el enumerate para convertir una lista
# una lista con tuples de índice-valor

mi_tuple = list(enumerate(nombres))

print(mi_tuple)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if not nombre.startswith("M"):
        continue
    else:
        print(nombre)
