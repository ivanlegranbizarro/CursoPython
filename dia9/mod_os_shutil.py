# Modos OS y SHUTIL

import os
import shutil

print(os.getcwd())

with open("prueba.txt", "w") as f:
    f.write("Esto es una prueba")

shutil.move("prueba.txt", "pruebas/prueba.txt")
