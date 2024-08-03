# El bucle while es un bucle que se repite hasta que se cumpla una condición

monedas = 5

while monedas >= 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1

respuesta = "s"

# while respuesta == "s":
#     respuesta = input("¿Quieres seguir?(s/n) ")
# else:
#     print("Gracias")

nombre = "Iván"

for letra in nombre:
    if letra == "á":
        continue
    else:
        print(letra)
