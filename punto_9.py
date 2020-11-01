# 9) Realizar un algoritmo que dado un número entero, visualice en pantalla si es par o impar. 
# En el caso de ser 0, debe visualizar “el número no es par ni impar” (para que un numero sea par, 
# se debe dividir entre dos y que su resto sea 0)

num = int(input('Ingrese un numero '))

print('\n')

if num == 0:
    print('El nuumero no es par ni es impar ')
elif num % 2 == 0:
    print('El numero ' + str(num) + ' es par ')
else:
    print('El numero ' + str(num) + ' no es par ')

print('\n')

