import os
from os import system
from pathlib import Path


mi_ruta = Path().home() / "Recetas"


def recuento_recetas(ruta):
    contador = 0
    for _ in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def menu_inicio():
    system("clear")
    print("*" * 50)
    print("*" * 4 + " " + "Bienvenido a tu administrador de recetas" + " " + ("*" * 4))
    print("*" * 50)
    print("\n")
    print(f'Las recetas se encuentran en "{mi_ruta}"')
    print(f"El total de recetas es {recuento_recetas(mi_ruta)} recetas")

    while True:
        print("Elige una opción:")
        print("1. Mostrar todas las categorías")
        print("2. Crear una categoría")
        print("3. Crear una receta")
        print("4. Eliminar una receta")
        print("5. Eliminar una categoría")
        print("6. Salir")

        eleccion_menu = int(input())
        return eleccion_menu


# Mostrar menú de inicio
# menu_inicio()


def mostrar_categorias(ruta):
    print("Categorías: ")
    listado_de_categorias = []

    for index, directorio in enumerate(Path(ruta).iterdir()):
        if directorio.is_dir():
            print(f"{index + 1}. {directorio.name}")
            listado_de_categorias.append(directorio.name)

    return listado_de_categorias


def elegir_categoria(lista):
    while True:
        try:
            categoria_seleccionada = int(input("\nElige una categoría (número): "))
            if 0 < categoria_seleccionada <= len(lista):
                return lista[categoria_seleccionada - 1]
            else:
                print(f"Por favor, elige un número entre 1 y {len(lista)}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")


def mostrar_recetas(ruta):
    print("Estas son tus recetas almacenadas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []

    for index, archivo in enumerate(ruta_recetas.glob("**/*.txt")):
        print(f"{index + 1}. {archivo.name}")
        lista_recetas.append(archivo.name)

    return lista_recetas


def elegir_receta(lista):
    while True:
        try:
            receta_seleccionada = int(input("\nElige una receta (número): "))
            if 0 < receta_seleccionada <= len(lista):
                return lista[receta_seleccionada - 1]
            else:
                print(f"Por favor, elige un número entre 1 y {len(lista)}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")


menu = 0

match menu:
    case 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_ruta + mi_categoria)
        mi_receta_escogida = elegir_receta(mis_recetas)
        # mostrar esa receta
        # volver al inicio
        pass
    case 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        # crear receta nueva
        # volver al inicio
        pass
    case 3:
        # crear categoría nueva
        # volver al inicio
        pass
    case 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_ruta + mi_categoria)
        mi_receta_escogida = elegir_receta(mis_recetas)
        # eliminar esa receta
        # volver al inicio
        pass
    case 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        # eliminar la categoría
        # volver al inicio
        pass
    case 6:
        # salir del programa
        pass
    case _:
        # manejar caso en el que `menu` no coincide con ningún valor esperado
        pass
