# Calcular las ganancias de unos vendedores(comisiones del 13%)

nombre_vendedor = input("¿Cuál es tu nombre? ")

dinero_por_ventas = float(input("¿Cuánto dinero hiciste hoy con tus ventas? "))

calculo = (dinero_por_ventas * 13) / 100

print(f"{nombre_vendedor} hoy has ganado: {round(calculo,2)} con tus comisiones")
