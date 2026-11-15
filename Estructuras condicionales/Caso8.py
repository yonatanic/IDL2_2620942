# CASO 8: Area de un terreno con forma A (rectangulo + triangulo)

ladoA: float
ladoB: float
ladoC: float
areaRectangulo: float
areaTriangulo: float
areaTotal: float

ladoA = float(input('Digite el lado A: '))
ladoB = float(input('Digite el lado B: '))
ladoC = float(input('Digite el lado C: '))

# Rectangulo: base B y altura C
areaRectangulo = ladoB * ladoC

# Triangulo: base B y altura (A - C)
areaTriangulo = ladoB * (ladoA - ladoC) / 2

areaTotal = areaRectangulo + areaTriangulo

print(f'El area del terreno es: {areaTotal:.2f} m2')