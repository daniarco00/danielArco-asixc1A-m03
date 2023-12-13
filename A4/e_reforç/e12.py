"""
Realitzar un programa que calculi quants diners estalviarà una persona en un any, si al final de cada mes diposita
diferents quantitats de diners.
Per fer això, el programa demanarà per cada mes la quantitat que es pensa estalviar. El programa també haurà de mostrar,
 a mesura que l’usuari va entrant les quantitats, el total estalviat des del començament de l’any fins al mes per al qual
  s’acaba de posar la quantitat.
"""
total_estalviat = 0

for x in range(1,13):
    estalviat = int(input(f"Quants diners pena estalviar el mes {x}: "))
    total_estalviat += estalviat
    print(total_estalviat)