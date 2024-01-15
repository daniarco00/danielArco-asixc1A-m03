"""
Danil Arco Guasch
15/12/2023
ASIXc A M03 UF1 A4
Descripció:

L'usuari introduirà una llista d'enters separada per espais. Prèviament dirà quants enters introduirà.
Un cop llegits tots, mostrar per pantalla la suma de tots els valors positius.
Cal fer el control d'errors.

"""
try:
    llista = [int(x) for x in input("Introdueix una llista d'enters separades per espais: ").split()]
    llista_positius = []

    for i in llista:
        if i > 0:
            llista_positius.append(i)
    print(f"La suma dels numeros positius que has introduit es {sum(llista_positius)}")

except:
    print("Introdueix les dades correctament.")

