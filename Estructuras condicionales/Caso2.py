# CASO 2: Numero menor y mayor de tres numeros

num1: float
num2: float
num3: float
menor: float
mayor: float

num1 = float(input('Digite el primer numero: '))
num2 = float(input('Digite el segundo numero: '))
num3 = float(input('Digite el tercer numero: '))

# Se asume que el primero es el menor y el mayor, y se compara con los demas
menor = num1
mayor = num1

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

print(f'El numero menor es: {menor}')
print(f'El numero mayor es: {mayor}')