import bs4
import requests
import os

# URL de la página de cursos
url = "https://www.escueladirecta.com/courses/"

# Solicitar la página
resultado = requests.get(url)

# Crear el objeto BeautifulSoup
sopa = bs4.BeautifulSoup(resultado.text, "lxml")

# Seleccionar todas las imágenes con la clase 'course-box-image'
imagenes = sopa.select(".course-box-image")

# Crear un directorio para guardar las imágenes
if not os.path.exists("imagenes_cursos"):
    os.makedirs("imagenes_cursos")

# Loop para descargar y guardar cada imagen
for i, img in enumerate(imagenes):
    # Obtener la URL de la imagen
    img_url = img["src"]

    # Solicitar la imagen
    imagen_curso = requests.get(img_url)

    # Guardar la imagen en el directorio creado
    with open(f"imagenes_cursos/imagen_curso_{i+1}.jpg", "wb") as f:
        f.write(imagen_curso.content)

    print(f"Imagen {i+1} guardada.")

print("Descarga completada.")
