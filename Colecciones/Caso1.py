# CASO 1: Total a pagar en una llantera
# S/ 150 por llanta si compra menos de 5, S/ 120 por llanta si compra 5 o mas

cantidad: int
precio: float
total: float

cantidad = int(input('Digite la cantidad de llantas: '))

if cantidad < 5:
    precio = 150
else:
    precio = 120

total = cantidad * precio

print(f'Precio por llanta: S/ {precio:.2f}')
print(f'El total a pagar es: S/ {total:.2f}')