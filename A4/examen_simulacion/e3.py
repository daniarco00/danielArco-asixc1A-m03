"""
Danil Arco Guasch
15/12/2023
ASIXc A M03 UF1 A4
Descripció:
Programa que pinta per pantalla un taulell d'escacs marcat amb una B les caselles
blanques, i amb una N les negres.
El programa , haurà de marcar amb * les caselles a les quals es pot moure una torre, des d'una posició concreta, que
cal demanar a l'usuari per al terminal. La posició ha de ser dos n'umeros de l'1 al 8 (ambdós inclosos)
Cal fer el control d'errors.
Un taulell d'escacs, és una matriu de 8x8. És a dir, 8 files i 8 columnes.
La torre és una figura que només permet moviments en horitzontal y en vertical
"""
try:
    numeros_vert = (1,2,3,4,5,6,7,8)
    numeros_horiz = ("   1  2  3  4  5  6  7  8")
    for i in range(8):
        print(f"\n {numeros_vert[i]}", end="")
        for j in range(8):
            if (i + j) % 2 == 0:
                print(" B ", end="")
            else:
                print(" N ", end="")
        if i == 7:
            print()
            print(f"{numeros_horiz}")

    posicio_vert = int(input("Introduix la posicio vertical de la torre (1-8): "))
    posicio_horiz = int(input("Introdueix la posicio horitzontal de la torre (1-8): "))



    for i in range(8):
        if posicio_vert == i+1:
            print(f"\n {numeros_vert[i]}", end="")
            print(f"{' * ' * 8}", end="")
        else:
            print(f"\n {numeros_vert[i]}", end="")
            for j in range(8):
                if posicio_horiz == j+1:
                    print(" * ", end="")
                elif (i + j) % 2 == 0:
                    print(" B ", end="")
                else:
                    print(" N ", end="")
            if i == 7:
                print()
                print(f"{numeros_horiz}")

except:
    print("Error")



