from pathlib import Path
from os import system

# 1 - leer receta: elegir categoría, mostrar recetas, mostrar receta elegida
# 2 - crear receta: elegir categoría, escribir nombre nueva receta, crear contenido
# 3 - crear categoría: escribir nombre nueva categoría (crear carpeta con ese nombre)
# 4 - eliminar receta (como la 1 pero en lugar de mostrar la receta, la va a borrar)
# 5 - eliminar categoría: como la 3 pero en lugar de crearla, la va a borrar
# 6 - finalizar programa: salir del bucle principal

# Sería bueno que cada vez que el usuario sala del programa se limpie la pantalla

# Funciones


ruta_categorias = Path().home() / "Recetas"


def mostrar_categorias(ruta):
    print("Las categorías son:")
    listado_categorias = list(ruta.iterdir())
    for i, categoria in enumerate(listado_categorias, start=1):
        print(i, categoria.name)
    return listado_categorias


def elegir_categoria(ruta):
    listado_categorias = mostrar_categorias(ruta)

    while True:
        try:
            seleccion = int(input("Elige una categoría: "))
            if seleccion < 1 or seleccion > len(listado_categorias):
                print("La categoría no existe")
            else:
                return listado_categorias[seleccion - 1]
        except ValueError:
            print("Por favor, introduce un número")


elegir_categoria(ruta_categorias)
