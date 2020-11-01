# 8) Una tienda ofrece un descuento del 15% sobre el total de la compra durante el mes de octubre.
# Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar al cliente.

mes = input('Ingrese el mes actual ')
compra = float(input('Ingrese el total de la compra '))

print('\n')

if mes == 'octubre' or mes == 'Octubre':
    desc = compra * 0.15
    print('VALOR       ' + str(compra))
    print('DESCUENTO   ' + str(desc))
    print('TOTAL       ' + str(float(compra - desc)))
else:
    desc = 0
    print('VALOR       ' + str(compra))
    print('DESCUENTO   ' + str(desc))
    print('TOTAL       ' + str(float(compra - desc)))


print('\n')