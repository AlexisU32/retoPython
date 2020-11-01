# 5) Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo, 
# debe imprimir el producto de los tres y si no lo es, imprimirá la suma.


num1 = float(input('Ingrese el primer numero '))
num2 = float(input('Ingrese el segundo numero '))
num3 = float(input('Ingrese el tercer numero '))

if num1 < 0:
    prod = num1 * num2 * num3
    print('El producto de los tres numeros ingresados es de ' + str(prod))
else:
    suma = num1 + num2 + num3
    print('La suma de los tres numeros ingresados es de ' + str(suma))

 
