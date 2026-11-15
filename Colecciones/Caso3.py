# CASO 3: Impuesto (mayor de 18 anios e ingresos >= S/ 3000)

edad: int
ingreso: float
impuesto: float

edad = int(input('Digite su edad: '))
ingreso = float(input('Digite su ingreso mensual: '))

if edad > 18 and ingreso >= 3000:
    impuesto = ingreso * 0.05
    print('El usuario SI tiene que tributar')
    print(f'El monto a tributar es: S/ {impuesto:.2f}')
else:
    print('El usuario NO tiene que tributar')