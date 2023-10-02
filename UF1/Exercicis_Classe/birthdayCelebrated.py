"""
Daniel Arco
ASIXc M03-UF1 A2 MANIPULACIÓ DE DADES
Digues si una persona ha celebrat l'aniversari enguany.
"""

diaAniversari = int(input("Quin dia es el teu aniversari? "))
if diaAniversari > 31:
    print("Has introduït un dia invàlid. :p")
    exit(1)
mesAniversari = int(input("Quin mes es el teu aniversari? "))
if mesAniversari > 12:
    print("Has introduït un mes invàlid. :v")
    exit(1)
diaActual = int(input("Quin dia es avui? "))
mesActual = int(input("En quin mes estem? "))

if diaAniversari > diaActual and mesAniversari > mesActual:
    print("El teu aniversari ha passat.")
elif diaActual == diaAniversari and mesActual == mesAniversari:
    print("Es el teu aniversari.")
else:
    print("El teu aniversari no ha passat.")


