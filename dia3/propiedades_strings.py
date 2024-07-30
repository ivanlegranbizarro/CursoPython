"""Los strings son inmutables, concatenables,
multiplicables y multilíneas."""

# Esto no se puede hacer
# nombre = "Iván"
# nombre[2] = "a"

# Lo que sí puedo hacer es reescribir la variable

nombre = "Miracle"

verbo = "Es un"

print(verbo + " " + nombre)

print((nombre + "\n") * 10)

poema = """Mil pequeños peces blancos
como si hirivera
el color del agua"""

print(poema)

print("agua" in poema)

print(len(poema))
