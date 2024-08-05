# Random: Generar números aleatorios

from random import *

aleatorio = round(uniform(0, 10), 2)

aleatorio_0_1 = random()

# Selección aleatorio en una lista

colores = ["rojo", "azul", "verde", "amarillo"]

numeros = list(range(5, 50, 5))

print(aleatorio)

print(aleatorio_0_1)

print(choice(colores))

shuffle(numeros)

print(numeros)
