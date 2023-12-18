"""
Danil Arco Guasch
15/12/2023
ASIXc A M03 UF1 A4
Descripció: MyReplace
"""
try:
    cadena = str(input("Introdueix una cadena de caracters: "))
    cadena_antiga = str(input("Introdueix el caràcter que vols remplaçar: "))
    cadena_nova = str(input("Introdueix el nou caràcter cadena: "))

    if cadena_antiga not in cadena or len(cadena_antiga) > 1 or len(cadena_nova) > 1:
        raise TypeError

    for car in cadena:
        if car == cadena_antiga:
            print(cadena_nova, end="")
        else:
            print(car, end="")

except:
    print("Introdueix be les dades.")