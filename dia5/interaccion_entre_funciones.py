from random import shuffle

# Lista inicial que contenga los palitos
palitos = ["-", "--", "---", "----"]

# Una función que mezcle los palitos


def mezclar_palitos(lista):
    shuffle(lista)
    return lista


# Pedirle al usuario que escoja entre 1 de los 4 palitos


def probar_suerte():
    intento = ""

    while intento not in ["1", "2", "3", "4"]:
        intento = input("Por favor, indica un número entre el 1 y el 4: ")

    return int(intento)


# Comprobar intento del usuario


def chequear_intento(lista, intento):
    if lista[intento - 1] == "-":
        print("Tienes que lavar los platos")
    else:
        print("Te salvaste")

    print(f"Te ha tocado el {lista[intento - 1]}")


palitos_mezclados = mezclar_palitos(palitos)

usuario_elige_palito = probar_suerte()

chequear_intento(palitos_mezclados, usuario_elige_palito)

from random import randint


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


def evaluar_jugada(tirada1, tirada2):
    suma_dados = tirada1 + tirada2

    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:  # suma_dados >= 10
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


# Ejemplo de uso
tirada1, tirada2 = lanzar_dados()
resultado = evaluar_jugada(tirada1, tirada2)
print(resultado)

lista_numeros = [1, 2, 2, 500, 14, 38]


def reducir_lista(lista):
    lista.remove(max(lista))
    lista_sin_duplicados = set(lista)

    return list(lista_sin_duplicados)


from random import randint

lista_numeros = [1, 2, 3, 4, 5, 6, 7]


def lanzar_moneda():
    lanzar_moneda = randint(0, 1)

    if lanzar_moneda == 0:
        return "Cara"
    else:
        return "Cruz"


def probar_suerte(moneda, lista):
    if moneda == "Cara":
        lista = []
        return "La lista se autodestruirá", lista
    else:
        return "La lista fue salvada", lista
