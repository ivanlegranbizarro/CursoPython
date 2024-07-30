# Los diccionarios son colecciones de pares clave-valor

persona = {"nombre": "Iván", "edad": 38}
consulta = persona["nombre"]


dic = {"clave1": 55, "clave2": [10, 20, 30], "clave3": {"s1": 100, "s2": 200}}
dic2 = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}

print(dic["clave3"]["s2"])

print(dic2["c2"][1].upper())

print(persona)
print(persona.items())
