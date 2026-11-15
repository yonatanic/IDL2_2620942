# CASO 4: Sueldo base mas 25% de comision por tres ventas

sueldoBase: float
venta1: float
venta2: float
venta3: float
totalVentas: float
comision: float
totalMes: float

sueldoBase = float(input('Digite el sueldo base: '))
venta1 = float(input('Digite el monto de la venta 1: '))
venta2 = float(input('Digite el monto de la venta 2: '))
venta3 = float(input('Digite el monto de la venta 3: '))

totalVentas = venta1 + venta2 + venta3
comision = totalVentas * 0.25
totalMes = sueldoBase + comision

print(f'La comision del mes es: S/ {comision:.2f}')
print(f'El total que recibira en el mes es: S/ {totalMes:.2f}')