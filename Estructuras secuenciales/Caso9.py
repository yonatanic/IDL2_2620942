# CASO 9: Compra con descuento y cambio

montoBase: float
porcentajeDescuento: float
pagaCon: float
descuento: float
totalPagar: float
cambio: float

montoBase = float(input('Digite el monto base: '))
porcentajeDescuento = float(input('Digite el porcentaje de descuento: '))
pagaCon = float(input('Digite con cuanto paga el cliente: '))

descuento = montoBase * porcentajeDescuento / 100
totalPagar = montoBase - descuento
cambio = pagaCon - totalPagar

print(f'El cliente pagara: S/ {totalPagar:.2f}')
print(f'El cambio es: S/ {cambio:.2f}')