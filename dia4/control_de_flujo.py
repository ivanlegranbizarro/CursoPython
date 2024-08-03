# Los controladores de flujo son if, elif y else

a = 10
b = 5

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual que b")

mascota = "tortuga"

match mascota:
    case "perro":
        print("Tienes un perro")
    case "gato":
        print("Tienes un gato")
    case "tortuga":
        print("Tienes una tortuga")
    case _:
        print("No sé qué mascota tienes")
