from collections import Counter, defaultdict, namedtuple

numeros = [8, 8, 8, 4, 3, 2, 4, 7, 8, 3, 4]

texto = "Voy a ir al Mississipi"

refran = "Al pan, pan, y al vino, vino"

serie = Counter([1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4])

print(Counter(numeros))
print(Counter(texto))
print(Counter(refran.split(" ")))
print(serie)
# Así aparecen los dos elementos que más se repiten
print(serie.most_common(2))

mi_diccionario = {"uno": "verde", "dos": "rojo", "tres": "azul"}

mi_nuevo_diccionaro = defaultdict(lambda: "nada")

mi_nuevo_diccionaro["uno"] = "verde"


print(mi_nuevo_diccionaro)
print(mi_nuevo_diccionaro["dos"])


mi_tupla_normal = (500, 18, 65)

print(mi_tupla_normal[1])


Persona = namedtuple("Persona", ["nombre", "altura", "edad"])

ariel = Persona("Ariel", 1.79, 40)

print(ariel.altura)

print(ariel[2])
