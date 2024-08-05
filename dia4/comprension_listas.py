# La comprensión de listas es una forma de crear listas
# de forma dinámica

nombres = ["Pepe", "Juan", "Luis"]

palabra = "Python"

nombres_mayusculas = [nombre.upper() for nombre in nombres]

print(nombres_mayusculas)


letras_de_la_palabra = [letra for letra in palabra]

deletrear_mi_nombre = [letra for letra in "Iván"]

print(letras_de_la_palabra)

print(deletrear_mi_nombre)
