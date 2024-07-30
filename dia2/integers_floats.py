mi_numero = 7
mi_float = 5.2

try:
    edad_usuario = int(input("¿Cuál es tu edad? "))
except ValueError:
    print("Por favor, introduce un valor numérico")
    exit()


print(mi_float + mi_numero + edad_usuario)

num1 = 7.5

num2 = 2.5

print(type(num1 + num2))
