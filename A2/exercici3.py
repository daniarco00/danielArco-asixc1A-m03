import math

print("Programa per calcular la hipotenusa d'un triangle :)")
print("Necessitare que em propoircionis dos valors.")

a = float(input("Escriu el valor del catet a: "))
b = float(input("Escriu el valor del catet b: "))

hipotenusa = math.sqrt(a**2+ b**2)

print("El resultat de la hipotenusa es", hipotenusa)