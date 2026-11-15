# CASO 6: Tiempo aproximado vivido segun la edad

edad: int
meses: int
semanas: int
dias: int
horas: int

edad = int(input('Digite la edad: '))

meses = edad * 12
semanas = edad * 52
dias = edad * 365
horas = dias * 24

print(f'Meses vividos: {meses}')
print(f'Semanas vividas: {semanas}')
print(f'Dias vividos: {dias}')
print(f'Horas vividas: {horas}')