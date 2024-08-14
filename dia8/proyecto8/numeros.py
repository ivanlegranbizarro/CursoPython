# Tres generadores: perfumería, medicina, cosmética


def turno_perfumeria():
    x = 1
    while True:
        yield x
        x += 1


def turno_medicina():
    x = 1
    while True:
        yield x
        x += 1


def turno_cosmetica():
    x = 1
    while True:
        yield x
        x += 1


# Decorador para mensaje en los turnos: Su turno es ... Aguarde para ser atendido


def decorar_turno(funcion_decorada):
    def otra_funcion():
        print("Su número es: ")
        print(next(funcion_decorada))
        print("Aguarde para ser atendido")

    return otra_funcion()
