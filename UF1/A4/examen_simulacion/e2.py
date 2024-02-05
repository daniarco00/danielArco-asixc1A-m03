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
    cadena = input("Introdueix una frase: ")
    caracter_antic =input("Introdueix el caracter que vulguis cambiar: ")
    caracter_nou = input("Introdueix el caracter per el qual vols cambiar: ")


    for car in cadena:
        if car == caracter_antic:
            print(caracter_nou, end="")
        else:
            print(car, end="")



except:
    print("Introdueix les dades correctament.")
