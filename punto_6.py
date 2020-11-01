#  6) Realizar un algoritmo que lea un número por teclado. En caso de que ese número sea 0 
# o menor que 0, se saldrá del programa imprimiendo antes un mensaje de error. 
# Si es mayor que 0, se deberá calcular su cuadrado y la raiz cuadrada del mismo, 
# visualizando el numero que ha tecleado el usuario y su resultado (“Del numero X, su potencia es X y su raiz X” ). 
# Para calcular la raiz cuadrada se puede usar la función interna RAIZ(X) o con una potencia de 0,5.

import math

num = float(input('Ingrese un numero '))

if num <= 0:
    print('Error')
    exit()
else:
    print('Del numero ' + str(num) + ' su potencia es ' + str(pow(num,2)) + ' y su raiz es ' + str(pow(num, 0.5)))


