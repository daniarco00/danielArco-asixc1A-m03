#python3
#calculadora

import sys


def suma(a, b):
    return(a + b)
def resta(a, b):
    return(a - b)
def multiplicacion(a, b):
    return(a * b)
def division(a, b):
    return(a / b)

print("Bienvenid@ a la calculadora de Daniel. \n")
opcion = int(input("Introduce el tipo de operación que quieras realizar. 1. Suma 2. Resta 3. Multiplicación 4. División 5. Salir \n -"))

if opcion == 5:
    sys.exit()
elif opcion < 1 or opcion > 5:
    print("Opcion invalida. Porfavor elige entre el 1 y 5")
    sys.exit()

num1 = float(input("Escribe el valor del primer numero: "))
num2 = float(input("Escribe el valor del segundo numero: "))

if opcion == 1:
    print("La respuesta es", suma(num1, num2))
if opcion == 2:
    print("La respuesta es", resta(num1, num2))
if opcion == 3:
    print("La respuesta es", multiplicacion(num1,num2))
if opcion == 4:
    print("La respuesta es", division(num1,num2))