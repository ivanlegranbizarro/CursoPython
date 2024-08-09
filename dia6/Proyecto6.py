from os import system
from pathlib import Path

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


def mostrar_listado_recetas_de_categoria_escogida(ruta_categoria_escogida):
    print(f"Las recetas de {ruta_categoria_escogida.name} son:")
    listado_recetas = list(ruta_categoria_escogida.iterdir())
    for i, receta in enumerate(listado_recetas, start=1):
        print(i, receta.name)


def escoger_receta(ruta_categoria_escogida):
    mostrar_listado_recetas_de_categoria_escogida(ruta_categoria_escogida)
    listado_recetas = list(ruta_categoria_escogida.iterdir())
    while True:
        try:
            seleccion = int(input("Elige una receta: "))
            if seleccion < 1 or seleccion > len(listado_recetas):
                print("La receta no existe")
            else:
                return listado_recetas[seleccion - 1]
        except ValueError:
            print("Por favor, introduce un número")


def abrir_receta_escogida(receta_escogida):
    with open(receta_escogida) as f:
        print(f.read())


def crear_nueva_receta(ruta_categoria_escogida):
    escoger_nombre_nueva_receta = input("Introduce el nombre de la nueva receta: ")
    if Path(ruta_categoria_escogida / escoger_nombre_nueva_receta).exists():
        print("La receta ya existe")
    else:
        with open(ruta_categoria_escogida / escoger_nombre_nueva_receta, "w") as f:
            f.write(input("Introduce el contenido de la nueva receta: "))


ruta_categoria_escogida = elegir_categoria(ruta_categorias)

crear_nueva_receta(ruta_categoria_escogida)
