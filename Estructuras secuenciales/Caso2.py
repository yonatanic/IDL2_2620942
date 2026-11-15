# CASO 2

nota1: float
nota2: float
nota3: float
nota4: float
promedio: float

nota1 = float(input('Digite la nota del examen 1: '))
nota2 = float(input('Digite la nota del examen 2: '))
nota3 = float(input('Digite la nota del examen 3: '))
nota4 = float(input('Digite la nota del examen 4: '))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

print(f'El promedio es: {promedio:.2f}')