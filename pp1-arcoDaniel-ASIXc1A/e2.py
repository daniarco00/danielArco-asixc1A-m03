"""
Daniel Arco Guasch
ASIXc1A
Pp1A Prova Pràctica  UF1 M03 ASIXc
20/10/2023
"""

print("Programa per calcular la nota final de la UF2 del modul03 d'ASIX.")
print("Els criteris d'avaluació seràn de UF2 = 1*RA on RA = (0.15*Pt1.1 + 0.15*Pr1.2 + 0.7*Pp1 )")


pt1_1 = float(input("Introdueix la qualificació de Pt1.1: "))
pr1_2 = float(input("Introdueix la qualificació de Pr1.2: "))
pp1 = float(input("Introdueix la qualificació de Pp1.1: "))


nota_final = ((0.15 * pt1_1) + (0.15 * pr1_2) +(0.7 * pp1))


print(f"La teva nota final de la UF2 es de {nota_final:.2f}")


