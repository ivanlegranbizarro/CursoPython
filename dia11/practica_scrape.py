import bs4
import requests

# URL base sin número de página específico
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# Lista de títulos que tienen más de 4 estrellas

titulos_rating_alto = []

# iterar páginas

for pagina in range(1, 51):
    # crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # seleccionar datos de los libros
    libros = sopa.select(".product_pod")

    # Iterar libros
    for libro in libros:
        # comprobar que los libros tengan al menos 4 estrellas
        if (
            len(libro.select(".star-rating.Four")) != 0
            or len(libro.select(".star-rating.Five")) != 0
        ):
            # guardar título del libro en una variable
            titulo_libro = libro.select("a")[1]["title"]

            # agregar_libro_a_la_lista
            titulos_rating_alto.append(titulo_libro)


# Ver los libros de rating alto en consola
for titulo in titulos_rating_alto:
    print(titulo)

# Ejemplo para obtener el título de un libro
# resultado = requests.get(url_base.format(1))
# sopa = bs4.BeautifulSoup(resultado.text, "lxml")

# libros = sopa.select(".product_pod")

# ejemplo = libros[0].select("a")[1]['title']

# print(ejemplo)
