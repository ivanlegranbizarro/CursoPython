# Juego del ahorcado

from random import choice

palabras = ["galletas", "cerveza", "chocolate", "leche"]

letras_correctas = []
letras_incorrectas = []

abecedario = "abcdefghijklmnñopqrstuvwxyz"

intentos = 6

aciertos = 0

juego_terminado = False


def elegir_palabra(lista):
    palabra_elegida = choice(lista)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas


def pedir_letra():
    letra = input("Introduce una letra: ")
    if letra in abecedario and len(letra) == 1:
        return letra.lower()
    else:
        print("Por favor, introduce una letra")
        return pedir_letra()


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append("-")

    print(" ".join(lista_oculta))


def comprobar_letra_usuario_es_correcta(
    letra_elegida, palabra_oculta, vidas, coincidencias
):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias


def perder():
    print("Te has quedado sin vidas")
    print(f"La palabra oculta era {palabra}")

    return True


def ganar(palabra_descubierta):
    print("Felicidades, has descubierto la palabra")
    mostrar_nuevo_tablero(palabra_descubierta)

    return True


palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print("\n" + "*" * 20 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letras incorrectas:" + " ".join(letras_incorrectas))
    print(f"Vidas restantes: {intentos}")
    print("\n" + "*" * 20 + "\n")
    letra = pedir_letra()
    intentos, terminado, aciertos = comprobar_letra_usuario_es_correcta(
        letra, palabra, intentos, aciertos
    )

    juego_terminado = terminado
