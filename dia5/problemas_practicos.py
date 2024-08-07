# Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio.


def devolver_distintos(n1, n2, n3):
    nums = [n1, n2, n3]
    suma = sum(nums)

    if suma > 15:
        return max(nums)
    elif suma < 10:
        return min(nums)
    else:
        nums.sort()
        return nums[1]
