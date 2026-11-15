# CASO 4: Colegiatura (S/ 100 por materia)
# Promedio >= 18: 50% de descuento sobre la mitad de los cursos

materias: int
promedio: float
costoMateria: float
total: float
descuento: float

costoMateria = 100

materias = int(input('Digite el numero de materias que cursa: '))
promedio = float(input('Digite el promedio del ultimo periodo: '))

total = materias * costoMateria

if promedio >= 18:
    # Mitad de los cursos * costo * 50%
    descuento = (materias / 2) * costoMateria * 0.5
    total = total - descuento
    print(f'Descuento aplicado: S/ {descuento:.2f}')
else:
    print('No tiene descuento')

print(f'El alumno debe pagar: S/ {total:.2f}')
