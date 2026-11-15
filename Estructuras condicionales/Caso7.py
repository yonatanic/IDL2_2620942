# CASO 7: Cobro del estacionamiento

# S/ 5.00 por hora completa y S/ 0.10 por cada minuto restante

minutosTotales: int
horas: int
minutosRestantes: int
cobro: float

minutosTotales = int(input('Digite el tiempo de permanencia en minutos: '))

horas = minutosTotales // 60
minutosRestantes = minutosTotales % 60

cobro = horas * 5.00 + minutosRestantes * 0.10

print(f'Horas: {horas} y minutos restantes: {minutosRestantes}')
print(f'El cobro total es: S/ {cobro:.2f}')