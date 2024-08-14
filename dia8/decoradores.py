# Los decoradores son funciones que se ejecutan antes o después de una función
# y sirven para añadir funcionalidad a una función.


def decorar_saludo(funcion_decorada):

    def otra_funcion(palabra):
        print("Hola")
        funcion_decorada(palabra)
        print("Adiós")

    return otra_funcion


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayuscula)

minuscula_decorada = decorar_saludo(minuscula)

mayuscula("Concha")

minuscula("Concha")


mayuscula_decorada("Concha es hermosa")
