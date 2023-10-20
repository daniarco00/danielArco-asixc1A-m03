"""
Daniel Arco Guasch
ASIXc1A
Pp1A Prova Pràctica  UF1 M03 ASIXc
20/10/2023
"""

import math
print("Programa que calcula l'àrea i el volum d'una piràmide quadrangular. ")

altura = float(input("Introdueix l'alçada de la piramide (en cm): "))
costat = float(input("Introdueix la mida dels costats de la piramide (en cm): "))


area = costat * (costat + math.sqrt(4*(altura*altura) + (costat * costat)))
volum = ((costat * costat) * altura) / 3

print(f"El volum de la piràmide quadrangular serà de {volum:.3f}cm³ i l'àrea serà de {area:.3f}cm².")






