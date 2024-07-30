# Las tuplas son inmutables: no se pueden modificar (y consumen menos recursos)

mi_tupla = ("a", "b", "c")

mi_tupla2 = ("d", "e", "f")

mi_tupla3 = mi_tupla + mi_tupla2

print(mi_tupla)
print(len(mi_tupla))
