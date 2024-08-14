# Match e inicio de variables

from numeros import decorar_turno, turno_cosmetica, turno_medicina, turno_perfumeria

t_medicina = turno_medicina()
t_cosmetica = turno_cosmetica()
t_perfumeria = turno_perfumeria()

while True:
    siguiente_turno = input("¿Para qué desea ser atendido? ")

    match siguiente_turno:
        case "p":
            decorar_turno(t_perfumeria)
        case "c":
            decorar_turno(t_cosmetica)
        case "m":
            decorar_turno(t_medicina)
        case _:
            print(
                "Por favor, introduce 'p' para perfumería, 'm' para medicina o 'c' para cosmetica."
            )
