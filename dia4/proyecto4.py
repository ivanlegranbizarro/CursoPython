# 1) Preguntar al usuario su nombre
# 2) Piensa un número entre el 1 y el 100
# 3) El usuario debe adivinar el número en 8 intentos

from random import randint

intentos = 8

numero_a_adivinar = randint(1, 100)

nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")

while intentos > 0:
    print(f"Intentos restantes: {intentos}"
    intento = int(input("Adivina el número entre 1 y 100: "))

    match intento:
        case intento if intento < numero_a_adivinar:
            print("Demasiado bajo")
            intentos -= 1
        case intento if intento > numero_a_adivinar:
            print("Demasiado alto")
            intentos -= 1
        case _:
            print("¡Correcto!")
            print(f"El número era {numero_a_adivinar}")
            print(f"Lo adivinaste en {8 - intentos} intentos")
            break
else:
    print("Has perdido")
    print(f"El número era {numero_a_adivinar}")
    print("Se acabaron los intentos")
