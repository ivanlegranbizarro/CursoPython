# Los sets son colecciones de elementos únicos

mi_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
mi_set_2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mi_set_3 = {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

mi_set_4 = mi_set.union(mi_set_3)

print(mi_set)
print(mi_set_2)

print(2 in mi_set)

print(mi_set_4)

mi_set_4.add(21)

print(mi_set_4)
