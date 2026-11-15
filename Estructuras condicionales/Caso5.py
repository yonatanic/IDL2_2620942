# CASO 5: Tipo de triangulo (Equilatero, Isosceles o Escaleno)

lado1: float
lado2: float
lado3: float
perimetro: float
s: float
area: float

lado1 = float(input('Digite el lado 1: '))
lado2 = float(input('Digite el lado 2: '))
lado3 = float(input('Digite el lado 3: '))

# Condicion para que los tres lados formen un triangulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 and lado2 == lado3:
        perimetro = lado1 + lado2 + lado3
        print('El triangulo es EQUILATERO')
        print(f'Su perimetro es: {perimetro:.2f}')
    elif lado1 == lado2:
        print('El triangulo es ISOSCELES')
        print('Los lados iguales son: lado 1 y lado 2')
    elif lado1 == lado3:
        print('El triangulo es ISOSCELES')
        print('Los lados iguales son: lado 1 y lado 3')
    elif lado2 == lado3:
        print('El triangulo es ISOSCELES')
        print('Los lados iguales son: lado 2 y lado 3')
    else:
        # Formula de Heron
        s = (lado1 + lado2 + lado3) / 2
        area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5
        print('El triangulo es ESCALENO')
        print(f'Su area es: {area:.2f}')
else:
    print('Con esos lados no se puede formar un triangulo')
