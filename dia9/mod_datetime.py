import datetime

mi_hora = datetime.time(17, 30, 0)

mi_dia = datetime.date(2024, 4, 14)

minuto_actual = datetime.datetime.now().minute

print(type(mi_hora))

print(mi_hora)

print(mi_dia)

print(mi_dia.today())

mi_fecha = datetime.datetime(2024, 4, 14, 17, 30, 0)

mi_fecha = mi_fecha.replace(month=8)

nacimiento = datetime.date(1985, 9, 29)
hoy = datetime.date.today()

# Calcula la edad
edad = (
    hoy.year
    - nacimiento.year
    - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
)

# Calcula el próximo cumpleaños
proximo_cumple = nacimiento.replace(year=hoy.year)
if hoy > proximo_cumple:
    proximo_cumple = proximo_cumple.replace(year=hoy.year + 1)

# Calcula los días restantes para el próximo cumpleaños
dias_para_cumple = (proximo_cumple - hoy).days

print(f"Tienes {edad} años. Faltan {dias_para_cumple} días para tu cumpleaños")
