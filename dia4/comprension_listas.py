# La comprensión de listas es una forma de crear listas
# de forma dinámica

nombres = ["Pepe", "Juan", "Luis"]

palabra = "Python"

nombres_mayusculas = [nombre.upper() for nombre in nombres]

print(nombres_mayusculas)


letras_de_la_palabra = [letra for letra in palabra]

deletrear_mi_nombre = [letra for letra in "Iván"]


lista_de_numeros_pares = [num for num in range(0, 100, 2)]

pies = [10, 20, 30, 50]
metros = []

convertir_pies_a_metros = [round((pie / 3.281), 2) for pie in pies]

# print(letras_de_la_palabra)

# print(deletrear_mi_nombre)

# print(lista_de_numeros_pares)

print(convertir_pies_a_metros)

lista_numeros = [2, 3, 10, 12, 41]
