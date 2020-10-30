
# 1) Dadas dos variables numéricas A y B, que el usuario debe teclear, se 
# pide realizar un algoritmo que intercambie los valores de ambas variables 
# y muestre cuanto valen al final las dos variables (recuerda la asignación). 

varA = float(input("Ingrese un numero para la variable A "))
varB = float(input("Ingrese un numero para la variable B "))
print("\n")

print("El valor de la variable 'A' es " + str(varA))
print("El valor de la variable 'B' es " + str(varB) + "\n")

a = varA 
b = varB
varB = a
varA = b

print("Ahora el valor de la variable 'A' es " + str(varA) + " y el valor de la variable 'B' es " + str(varB) + "\n")




# --------------------------------------------------------------------------------
