# CASO 1: Velocidad final de un auto

velocidadInicialKmh: float
aceleracion: float
tiempo: int
velocidadInicial: float
velocidadFinal: float
velocidadFinalKmh: float

velocidadInicialKmh = 0
aceleracion = 0.8
tiempo = 30

# Convertir km/h a m/s
velocidadInicial = velocidadInicialKmh * 1000 / 3600

# Formula: vf = v0 + a * t
velocidadFinal = velocidadInicial + aceleracion * tiempo

# Convertir m/s a km/h
velocidadFinalKmh = velocidadFinal * 3600 / 1000

print(f'La velocidad final es: {velocidadFinal:.2f} m/s')
print(f'La velocidad final es: {velocidadFinalKmh:.2f} km/h')