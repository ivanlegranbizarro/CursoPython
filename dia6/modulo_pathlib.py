# Pathlib es un modulo de Python para trabajar con archivos y directorios
from pathlib import Path

mi_ruta = Path("prueba.txt")

print(mi_ruta.exists())

mi_ruta = Path("/home/legran/Programación/CursoPython/dia6/prueba.txt")

print(mi_ruta.read_text())

print(mi_ruta.name)

if not mi_ruta.exists():
    print("Este archivo no existe")
else:
    print("Este archivo existe")

print(mi_ruta.exists())
