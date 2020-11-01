# 10) Modificar el algoritmo anterior, de forma que si se teclea un cero, 
# se vuelva a pedir el número por teclado (así hasta que se teclee un número mayor que cero) 
# (recuerda la estructura mientras).

num = int(0)

while num == 0:
    num = int(input('Ingrese un numero '))

print('\n')

if num == 0:
    print('El nuumero no es par ni es impar ')
elif num % 2 == 0:
    print('El numero ' + str(num) + ' es par ')
else:
    print('El numero ' + str(num) + ' no es par ')

print('\n')