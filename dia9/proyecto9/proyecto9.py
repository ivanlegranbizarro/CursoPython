import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = (
    "/home/legran/Documentos/Programación/CursoPython/dia9/proyecto9/Mi_Gran_Directorio"
)

mi_patron = r"N\D{3}-\d{5}"

hoy = datetime.date.today()

numeros_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo, patron):
    with open(archivo, "r") as f:
        texto = f.read()
        resultado = re.search(patron, texto)
        return resultado


def crear_listas():
    for carpeta, _, archivos in os.walk(ruta):
        for archivo in archivos:
            archivo_completo = Path(carpeta, archivo)
            resultado = buscar_numero(archivo_completo, mi_patron)
            if resultado is not None:
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(archivo.title())


def mostrar_todo():
    print("-" * 50)
    print(f"Fecha de la búsqueda: {hoy.day}/{hoy.month}/{hoy.year}")
    print("\n")
    print("ARCHIVO\t\t\tNUMERO DE SERIE")
    print("-------\t\t\t--------------")

    for i, archivo in enumerate(archivos_encontrados):
        print(f"{archivo}\t{numeros_encontrados[i]}")

    print("\n")
    print(f"Números encontrados: {len(numeros_encontrados)}")
    fin = time.time()
    duracion = fin - inicio
    print(f"La duración de la búsqueda: {math.ceil(duracion)} segundos")
    print("-" * 50)


crear_listas()
mostrar_todo()
