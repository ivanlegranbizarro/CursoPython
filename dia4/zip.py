# zip combina dos listas en una lista de tuplas

nombres = ["Pepe", "Juan", "Luis"]

edades = [33, 38, 42]

ciudades = ["Madrid", "Barcelona", "Sevilla"]

# Hay que castear el zip a una lista
combinar_nombres_edades = list(zip(nombres, edades))

print(combinar_nombres_edades)

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
