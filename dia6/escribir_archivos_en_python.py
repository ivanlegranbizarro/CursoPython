# Escribir archivos en Python

with open("prueba.txt", "r") as f:
    print(f.read())

# Anexar texto, no lo reescribe del todo
with open("prueba.txt", "a") as f:
    f.write("Pues nada. Aquí de tranquis")
