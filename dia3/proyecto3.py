# Programar un analizador de texto
# Pide un texto al usuario
# Cuenta cuántas palabras hay
# Pídele 3 letras y mira si aparecen en el texto y cuántas veces

texto = input("¿Cuál es tu texto? ")

letras = []

letras.append(input("¿Cuál es tu primera letra? "))

letras.append(input("¿Cuál es tu segunda letra? "))

letras.append(input("¿Cuál es tu tercera letra? "))

for letra in letras:
    if letra in texto.lower():
        print(f"La letra {letra} aparece {texto.count(letra)} veces")


print(f"El texto tiene {len(texto.split())} palabras")
print(f"La primera letra del texto es {texto[0]}")
print(f"La última  letra del texto es {texto[-1]}")
print(f'¿El texto contiene la palabra python? {"python" in texto.lower()}')

texto_invertido = texto.split()
texto_invertido.reverse()

oracion_invertida = " ".join(texto_invertido)

print(f"Tu texto invertido sería: {oracion_invertida}")
