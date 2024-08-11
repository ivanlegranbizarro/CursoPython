from os import system
from pathlib import Path

# Mostrar menú de inicio

menu = 0

match menu:
    case 1:
        # mostrar todas las categorías
        # elegir categoría
        # mostrar recetas de esa categoría
        # elegir una de esas recetas
        # mostrar esa receta
        # volver al inicio
        pass
    case 2:
        # mostrar categorías
        # elegir categoría
        # crear receta nueva
        # volver al inicio
        pass
    case 3:
        # crear categoría nueva
        # volver al inicio
        pass
    case 4:
        # mostrar todas las categorías
        # elegir categoría
        # mostrar recetas de esa categoría
        # elegir una de esas recetas
        # eliminar esa receta
        # volver al inicio
        pass
    case 5:
        # mostrar todas las categorías
        # elegir una categoría
        # eliminar la categoría
        # volver al inicio
        pass
    case 6:
        # salir del programa
        pass
    case _:
        # manejar caso en el que `menu` no coincide con ningún valor esperado
        pass
