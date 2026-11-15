# CASO 10: Cajero automatico (menor cantidad de billetes y monedas)
# Denominaciones: 200, 100, 50, 20, 10, 5, 1

monto: int
restante: int
b200: int
b100: int
b50: int
b20: int
b10: int
m5: int
m1: int

monto = int(input('Digite la cantidad a retirar: '))

restante = monto

b200 = restante // 200
restante = restante % 200

b100 = restante // 100
restante = restante % 100

b50 = restante // 50
restante = restante % 50

b20 = restante // 20
restante = restante % 20

b10 = restante // 10
restante = restante % 10

m5 = restante // 5
restante = restante % 5

m1 = restante

print(f'Billetes de 200: {b200}')
print(f'Billetes de 100: {b100}')
print(f'Billetes de 50: {b50}')
print(f'Billetes de 20: {b20}')
print(f'Billetes de 10: {b10}')
print(f'Monedas de 5: {m5}')
print(f'Monedas de 1: {m1}')