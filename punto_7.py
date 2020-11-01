# 7) Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas hay en el curso actual.
#  Diseñar un algoritmo para este propósito (recuerda que para calcular el porcentaje puedes hacer una regla de 3).

niñas = int(input('Ingrese la cantidad de niñas del curso '))
niños = int(input('Ingrese la cantidad de niños del curso '))

total = int(niños + niñas)

porcNiñas = int((niñas/total) * 100)
porcNiños = int((niños/total) * 100)

print('El porcentaje de niñas del curso es del ' + str(porcNiñas) + '% ')
print('El porcentaje de niños del curso es del ' + str(porcNiños) + '% ')




