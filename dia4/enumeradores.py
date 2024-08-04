# Los enumeradores se usan cuando queremos iterar
# sobre los índices de una lista


nombres = ["Pepe", "Juan", "Luis"]

for indice, nombre in enumerate(nombres):
    print(indice, nombre)


for i, item in enumerate(range(50, 55)):
    print(i, item)
