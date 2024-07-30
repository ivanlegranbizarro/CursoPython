num1 = 38
num2 = 2.5

print(type(num1))

num1 = num1 + num2


print(type(num1))

num1 = int(num1)

print(type(num1))

print(num1)


try:
    edad = int(input("Dime tu edad, estimado usuario: "))

    print(f"Tu edad es {edad} años")
except:
    raise ValueError("No se ha podido convertir la entrada a un valor numérico")
