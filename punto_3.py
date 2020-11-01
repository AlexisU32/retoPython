# 3) Algoritmo que lea dos números y nos diga cual de ellos es mayor 
# o bien si son iguales (recuerda usar la estructura condicional SI)

num1 = float(input('Ingrese el primer numero '))
num2 = float(input('Ingrese el segundo numero '))

if num1 > num2:
    if num1 == num2:
        print('Los dos numeros ingresados son iguales')
    else:
        print('El numero ' + str(num1) + ' es mayor que ' + str(num2))
else:
    if num1 == num2:
        print('Los dos numeros ingresados son iguales')
    else:
        print('El numero ' + str(num2) + ' es mayor que ' + str(num1))
    

    

