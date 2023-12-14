"""
Danil Arco Guasch
15/12/2023
ASIXc A M03 UF1 A4
Descripció:

Enunciado: Programa que implementi la funcionalitat del mètode replace. (sense fer servir el mètode). És a dir un
programa que demani una cadena de caràcters, un caràcter a modificar canviats pel caràcter de substitució
No es pot fer servir cap funció predefinida de Python. Cal fer el control d'errors.
"""
try:
    cadena = str(input("Introudiex una cadena de caracters: "))
    caracter_antic = str(input("Introdueix el caracter de la cadena el qual vols modificar (1 caracter): "))
    caracter_nou = str(input("introdueix el caracter pel qual vols modificar el caracter anteriorment introduit (1 cara"
                             "cter): "))

    if len(caracter_nou) > 1 or len(caracter_antic) > 1 or caracter_antic not in cadena:
        raise TypeError

    for car in cadena:
        if car == caracter_antic:
            print(caracter_nou, end="")
        else:
            print(car, end="")

except:
    print("Introdueix les dades correctament.")
