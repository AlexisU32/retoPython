# 4) Algoritmo que lea tres números distintos y nos diga cual de ellos es el mayor 
# (recuerda usar la estructura condicional Si y los operadores lógicos).

num1 = float(input('Ingrese el primer numero '))
num2 = float(input('Ingrese el segundo numero '))
num3 = float(input('Ingrese el tercer numero '))

if num1 > num2 and num1 > num3:
    print('El numero mayor ingresado es el ' + str(num1))
elif num2 > num1 and num2 > num3:
    print('El numero mayor ingresado es el ' + str(num2))
elif num3 > num1 and num3 > num2:
    print('El numero mayor ingresado es el ' + str(num3))






