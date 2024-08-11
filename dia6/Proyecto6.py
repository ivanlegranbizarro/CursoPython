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
        try:
            print("Elige una opción:")
            print("1. Mostrar todas las categorías")
            print("2. Crear una categoría")
            print("3. Crear una receta")
            print("4. Eliminar una receta")
            print("5. Eliminar una categoría")
            print("6. Salir")

            menu = int(input())
            return menu

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")


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

    for index, archivo in enumerate(ruta_recetas.glob("*.txt")):
        print(f"{index + 1}. {archivo.name}")
        lista_recetas.append(archivo)

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


def leer_receta(receta):
    print(receta.read_text())


def crear_nueva_receta(ruta):
    ruta = Path(ruta)
    while True:
        nombre_receta = input("Introduce el nombre de la nueva receta: ") + ".txt"
        receta_path = ruta / nombre_receta
        if receta_path.exists():
            print("Ya existe una receta con ese nombre.")
        else:
            contenido_receta = input("Introduce el contenido de la nueva receta: ")
            receta_path.write_text(contenido_receta)
            print("Receta creada con éxito.")
            break


def crear_nueva_categoria(ruta):
    ruta = Path(ruta)
    while True:
        nombre_categoria = input("Introduce el nombre de la nueva categoría: ") + ".txt"
        categoria_path = ruta / nombre_categoria
        if categoria_path.exists():
            print("Ya existe una categoría con ese nombre.")
        else:
            categoria_path.mkdir()
            print("Categoría creada con éxito.")
            break


def eliminar_mi_receta(receta):
    receta.unlink()
    print("Receta eliminada con éxito")


def eliminar_categoria(categoria):
    categoria.rmdir()
    print("Categoría eliminada con éxito")


def volver_inicio():
    while True:
        print("¿Quieres volver al inicio?")
        print("1. Sí")
        print("2. No")
        eleccion = int(input())
        if eleccion == 1:
            return
        elif eleccion == 2:
            exit()


while True:
    menu = menu_inicio()

    match menu:
        case 1:
            mis_categorias = mostrar_categorias(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            mis_recetas = mostrar_recetas(mi_ruta / mi_categoria)
            mi_receta_escogida = elegir_receta(mis_recetas)
            leer_receta(mi_receta_escogida)
            volver_inicio()
        case 2:
            mis_categorias = mostrar_categorias(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            crear_nueva_receta(mi_ruta / mi_categoria)
            volver_inicio()
        case 3:
            crear_nueva_categoria(mi_ruta)
            volver_inicio()
        case 4:
            mis_categorias = mostrar_categorias(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            mis_recetas = mostrar_recetas(mi_ruta / mi_categoria)
            mi_receta_escogida = elegir_receta(mis_recetas)
            eliminar_mi_receta(mi_receta_escogida)
            volver_inicio()
        case 5:
            mis_categorias = mostrar_categorias(mi_ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            eliminar_categoria(mi_ruta / mi_categoria)
            volver_inicio()
        case 6:
            exit()
