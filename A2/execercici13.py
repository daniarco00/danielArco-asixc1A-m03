import math

print("Benvingut al calculador d'arrels quadrades i arresl cubiques.")

nombre = float(input("Introdueix el valor amb el que vulguis operar: "))

x = math.sqrt(nombre)
y = nombre ** (1/3)

print(f"La arrel quadrada del seu valor es {x} y la arrel cubica es {y}.")