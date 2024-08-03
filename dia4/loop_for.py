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


nombre = "Miracle"

for letra in nombre:
    print(letra)
