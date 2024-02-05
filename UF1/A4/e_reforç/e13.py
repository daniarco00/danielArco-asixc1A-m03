"""
Una empresa vol enregistrar el nombre d’hores que treballa diàriament un empleat durant la setmana (sis dies laborals) i
determinar-ne el total d’hores treballades, així com el sou que rebrà per aquestes. Escriu el programa que permet
calcular aquestes dades. En concret, el programa:
demanarà per teclat el sou per hora
per cadascú dels 6 dies, demanarà quantes hores s’ha treballat
mostrarà el total d’hores treballades i el sou total a percebre
"""

sou = int(input("Introdueix el sou per hora del treballador: "))
paga_final = 0
hores_treballades = 0
for x in range(1, 7):
    hores = int(input(f"Introdueix la quantitat d'hores que ha fer el dia {x}: "))
    hores_treballades += hores
    paga_final += hores * sou

print(f"La quantitat d'hores treballades de la semana es {hores_treballades} i el sou es de {paga_final}")
