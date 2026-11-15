# CASO 3: Porcentaje de inversion

inversion1: float
inversion2: float
inversion3: float
total: float
porcentaje1: float
porcentaje2: float
porcentaje3: float

inversion1 = float(input('Digite lo que invierte la persona 1: '))
inversion2 = float(input('Digite lo que invierte la persona 2: '))
inversion3 = float(input('Digite lo que invierte la persona 3: '))

total = inversion1 + inversion2 + inversion3

porcentaje1 = inversion1 / total * 100
porcentaje2 = inversion2 / total * 100
porcentaje3 = inversion3 / total * 100

print(f'El total invertido es: S/ {total:.2f}')
print(f'La persona 1 invirtio el {porcentaje1:.2f}%')
print(f'La persona 2 invirtio el {porcentaje2:.2f}%')
print(f'La persona 3 invirtio el {porcentaje3:.2f}%')