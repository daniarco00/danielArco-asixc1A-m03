"""
Daniel Arco
ASIXc M03-UF1 A2 MANIPULACIÓ DE DADES
Exercici: Demanar un enter a l'usuari que indica el número de més
Retorna el nombre de dies del mes.
Input
1
Output
31
"""


mes = input()

match mes:
    case "1" | "3" | "5" | "7" | "8" | "10" | "12": print("31")
    case "2": print("28")
    case "4" | "6" | "9" | "11": print("30")
    case _: print("Ingresa les dades correctament.")

