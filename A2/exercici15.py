a = float(input("Introdueix el valor del primer numero: "))
b = float(input("Introdueix el valor del segon numero: "))
print(f"El primer valor es {a}")
print(f"El segon valor es {b}")

a, b = b, a

print(f"Ara el primer valor es {a}")
print(f"Ara el segon valor es {b}")
