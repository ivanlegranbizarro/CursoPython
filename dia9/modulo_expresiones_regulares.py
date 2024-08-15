# Las expresiones regulares nos permiten construir patrones
# con los que poder validar datos

import re

# Ejemplo sin expresiones regulares
texto = "Si necesitas ayuda, avísame. Estoy aquí si necesitas ayuda"

palabra = "ayuda" in texto

print(palabra)

patron = "avísame"

busqueda = re.search(patron, texto)

otra_busqueda = re.findall("ayuda", texto)

print(busqueda)

print(f"La palabra ayuda aparece {len(otra_busqueda)} veces en el texto")


nuevo_texto = "Llama al 564-525-6588 ya mismo"

patron_telefono = r"\d{3}-\d{3}-\d{4}"

resultado = re.search(patron_telefono, nuevo_texto)

print(resultado)

password = input("Introduce tu password: ")

patron_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

resultado = re.search(patron_password, password)

print(resultado)
