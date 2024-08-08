# Crear o mover archivos
# Enumerar archivos
# Crear rutas basadas en strings

from pathlib import Path

base = Path.home()

guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")

en_europa = guia.relative_to(Path("Europa"))
en_españa = guia.relative_to(Path("Europa", "España"))

print(en_europa)
print(en_españa)
