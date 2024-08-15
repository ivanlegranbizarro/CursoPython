# Zipfile y shutil sirven para comprimir y descomprimir archivos

import zipfile

# Comprimir
with zipfile.ZipFile("archivo_comprimido.zip", "w") as mi_zip:
    mi_zip.write("mi_texto_A.txt", compress_type=zipfile.ZIP_DEFLATED)
    mi_zip.write("mi_texto_B.txt", compress_type=zipfile.ZIP_DEFLATED)

# Descomprimir
with zipfile.ZipFile("archivo_comprimido.zip", "r") as mi_zip:
    mi_zip.extractall()
