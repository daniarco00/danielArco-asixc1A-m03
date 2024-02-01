cadena = str(input("Introdueix una cadena: "))
diccionari = {}

"""
for car in cadena:
    diccionari[car] = 0
"""
for car in cadena:
    if car in diccionari:
        diccionari[car] += 1
    else:
        diccionari[car] = 1

ultim_element = list(diccionari.keys())[-1]

for clave, valor in diccionari.items():
    if diccionari[clave] == valor:
        print(f"{{{clave}:{valor}}}", end="")
    else:
        print(f"{{{clave}:{valor}}}", end=", ")







