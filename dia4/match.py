# El 'match' sirve para buscar un elemento en una lista

dia_de_la_semana = "miércoles"

match dia_de_la_semana:
    case "lunes":
        print("Hoy es lunes")
    case "martes":
        print("Hoy es martes")
    case "miércoles":
        print("Hoy es miércoles")
    case "jueves":
        print("Hoy es jueves")
    case "viernes":
        print("Hoy es viernes")
    case "sábado":
        print("Hoy es sábado")
    case "domingo":
        print("Hoy es domingo")
    case _:
        print("Hoy no es un día de semana")


cliente = {
    "nombre": "Iván",
    "apellidos": "Legrán Bizarro",
    "edad": 38,
}


pelicula = {
    "nombre": "Leon, el profesional",
    "ficha_tecnica": {
        "director": "Luc Besson",
        "protagonista": "Jean Renau",
        "genero": "Acción",
    },
}

elementos = [cliente, pelicula, "libro"]

for elemento in elementos:
    match elemento:
        case {"nombre": nombre, "apellidos": apellidos}:
            print("Es un cliente")
            print(f"{nombre} {apellidos}")
        case {"nombre": nombre, "ficha_tecnica": {"director": director}}:
            print("Es una película")
            print(f"{nombre} de {director}")
        case _:
            print("Es un elemento")
