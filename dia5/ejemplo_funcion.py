precios_cafe = [("capuccino", 1.20), ("latte", 1.00), ("americano", 0.80)]


for precio in precios_cafe:
    print(f"El precio del cafe {precio[0]} es {precio[1]}")


def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe, precio in lista_precios:
        if precio_mayor < precio:
            precio_mayor = precio
            cafe_mas_caro = cafe

    return (cafe_mas_caro, precio_mayor)


cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El café más caro es {cafe} y cuesta {precio}€")
