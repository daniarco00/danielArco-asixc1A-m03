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
    notes = [int(x) for x in input("Introdueix les notes d'11 alumnes (sense decimals): ").split()]
    notes_aprovat = []
    notes_suspes = []
    cont_aprovat = 0
    cont_suspes = 0

    for i in notes:
        if i >= 5:
            notes_aprovat.append(i)
            cont_aprovat += 1
        else:
            notes_suspes.append(i)
            cont_suspes += 1

    for i in notes:
        if i < 0 or i > 10:
            raise TypeError

    if (cont_aprovat + cont_suspes) > 11 or (cont_aprovat + cont_suspes) < 11:
        raise TypeError


    print(f":( Suspesos: {cont_suspes} \n"
          f"{notes_suspes} \n"
          f":) Aprovats: {cont_aprovat} \n"
          f"{notes_aprovat}")

except:
    print("Introdueix be les dades. ")


