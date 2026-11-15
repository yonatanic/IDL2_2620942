# CASO 5: Ganancia de una inversion despues de un año (2% mensual)

capital: float
ganancia: float

capital = float(input('Digite el capital a invertir: '))

# 2% mensual durante 12 meses
ganancia = capital * 0.02 * 12

print(f'La ganancia despues de un año es: S/ {ganancia:.2f}')