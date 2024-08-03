# Los loops son bloques de código que se repiten múltiples veces

nombres = ["Pepe", "Juan", "Luis"]

for nombre in nombres:
    indice = nombres.index(nombre) + 1
    print(f"{indice}. Hola {nombre}")

for nombre in nombres:
    if nombre.startswith("J"):
        print(nombre)
    else:
        print(f"{nombre} no empieza por J")


for letra in "Miracle":
    print(letra)

for a, b in [[1, 2], [3, 4], {5, 6}]:
    print(a)
    print(b)


mi_diccionario = {"a": 1, "b": 2, "c": 3}

for clave, valor in mi_diccionario.items():
    print(clave, valor)
